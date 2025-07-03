import os
import pydicom
import nibabel as nib
import numpy as np
from pathlib import Path

def convert_dicom_folder_to_nii(dicom_folder):
    """Convert a folder of DICOM files to a 3D NIfTI image."""
    dicom_files = [pydicom.dcmread(str(dicom_folder / f)) for f in os.listdir(dicom_folder) if f.endswith('.dcm')]
    dicom_files.sort(key=lambda x: float(x.ImagePositionPatient[2]))  # Sort slices

    pixel_arrays = [ds.pixel_array for ds in dicom_files]
    volume = np.stack(pixel_arrays, axis=-1)

    # Get affine (orientation info)
    slice_thickness = float(dicom_files[0].SliceThickness)
    pixel_spacing = list(map(float, dicom_files[0].PixelSpacing))
    affine = np.diag(pixel_spacing + [slice_thickness, 1])

    nii_image = nib.Nifti1Image(volume, affine)
    return nii_image

def main():
    root_dir = Path('.')
    print(f"Scanning in: {root_dir.resolve()}")

    patient_folders = [
        f for f in os.listdir(root_dir)
        if os.path.isdir(f) and f[0].isdigit()
    ]

    if not patient_folders:
        print("No patient folders found ending with '_patient_name'!")
        return

    print(f"Found patient folders: {patient_folders}")

    modalities = ['t1c', 't1n', 't2', 't2_flair']

    for patient_folder in patient_folders:
        print(f"Processing {patient_folder}...")

        input_patient_path = root_dir / patient_folder
        output_patient_folder = f"{patient_folder}_nii"
        output_patient_path = root_dir / output_patient_folder
        output_patient_path.mkdir(exist_ok=True)

        for modality in modalities:
            input_modality_path = input_patient_path / modality
            if not input_modality_path.exists():
                print(f"  Skipping missing modality folder: {input_modality_path}")
                continue

            output_modality_path = output_patient_path / modality
            output_modality_path.mkdir(exist_ok=True)

            try:
                nii_image = convert_dicom_folder_to_nii(input_modality_path)
                output_nii_path = output_modality_path / f"{modality}.nii"
                nib.save(nii_image, str(output_nii_path))
                print(f"  Saved {output_nii_path}")
            except Exception as e:
                print(f"  Failed to convert {input_modality_path}: {e}")


if __name__ == "__main__":
    main()
