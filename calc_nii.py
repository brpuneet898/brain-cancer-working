import os

def count_nii_files(root_dir):
    count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.nii'):
                count += 1
    return count

if __name__ == "__main__":
    dataset_dir = '.'
    total_nii_files = count_nii_files(dataset_dir)
    print(f"Total number of .nii files in '{dataset_dir}': {total_nii_files}")
