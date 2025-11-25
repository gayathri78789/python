import os
from PIL import Image

# --- Configuration ---
input_folder = "images"      # Folder containing images
output_folder = "resized"    # Folder to save resized images
new_width = 800              # Desired width
new_height = 600             # Desired height
convert_to_format = "JPEG"   # Set None if you don't want format conversion (e.g., "PNG", "JPEG")

# --- Create output folder if it doesn't exist ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- Process each image in the input folder ---
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        # Full path for input image
        input_path = os.path.join(input_folder, filename)
        
        # Open the image
        img = Image.open(input_path)
        
        # Resize image
        img_resized = img.resize((new_width, new_height))
        
        # Determine output filename and format
        name, ext = os.path.splitext(filename)
        if convert_to_format:
            output_filename = f"{name}.{convert_to_format.lower()}"
        else:
            output_filename = filename
        
        output_path = os.path.join(output_folder, output_filename)
        
        # Save the resized image
        img_resized.save(output_path, convert_to_format if convert_to_format else None)
        print(f"Processed: {filename} -> {output_filename}")

print("All images resized successfully!")
