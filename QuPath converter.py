import os
import subprocess

image_directory = "./in"
output_directory = './out'
qupath = "C:/Users/ZHH/AppData/Local/QuPath-0.5.1/QuPath-0.5.1 (console).exe"

series = 2  # specify the image index in the image series to export

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

for file in os.listdir(image_directory):
    if file.endswith('.vsi'):
        input_file = os.path.join(image_directory, file)
        output_file = os.path.join(output_directory, os.path.splitext(file)[0] + '.ome.tif')
        
        try:
            subprocess.run([
                qupath, 
                "convert-ome", 
                input_file, 
                output_file, 
                "-y=4", 
                "-p", 
                "--series", str(series)
            ], check=True)
            print(f"Successfully converted {file}")
        except subprocess.CalledProcessError as e:
            print(f"Error converting {file}: {e}")
        
        # If you want to delete the original file after successful conversion:
        # os.remove(input_file)
