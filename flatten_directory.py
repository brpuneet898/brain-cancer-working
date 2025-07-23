import os
import shutil

def flatten_patient_folder(patient_dir):
    subfolders = ['t1c', 't1n', 't2', 't2_flair']
    for sub in subfolders:
        sub_path = os.path.join(patient_dir, sub)
        if os.path.exists(sub_path) and os.path.isdir(sub_path):
            for filename in os.listdir(sub_path):
                file_path = os.path.join(sub_path, filename)
                if os.path.isfile(file_path):
                    target_path = os.path.join(patient_dir, filename)
                    print(f"Moving: {file_path} -> {target_path}")
                    shutil.move(file_path, target_path)
            os.rmdir(sub_path)
            print(f"Deleted empty folder: {sub_path}")

def main():
    root_dir = '.'
    for patient_folder in os.listdir(root_dir):
        patient_dir = os.path.join(root_dir, patient_folder)
        if os.path.isdir(patient_dir):
            print(f"Processing patient folder: {patient_dir}")
            flatten_patient_folder(patient_dir)

if __name__ == "__main__":
    main()
