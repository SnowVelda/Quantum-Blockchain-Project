import zipfile
import os

def create_zip_archive(source_dir, output_filename):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Ensure the archive path is relative to the source_dir
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
    print(f"Successfully created {output_filename}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    output_zip_name = "t1m3_m4ch1n3_c0d3.zip"
    create_zip_archive(current_directory, output_zip_name)
