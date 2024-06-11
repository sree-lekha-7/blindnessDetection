import os
from PIL import Image
def resize_images_in_folder(input_folder, output_folder, new_size=(256, 256)): 
  try:
    if not os.path.exists(output_folder): 
      os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
      input_path = os.path.join(input_folder, filename)
      if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        output_path = os.path.join(output_folder, filename) with Image.open(input_path) as img:
          resized_img = img.resize(new_size) 
          resized_img.save(output_path)
          print(f"Image '{filename}' resized and saved to {output_path}") except Exception as e:
  print(f"Error: {e}")
input_folder_path = "C:\\Users\\mnsle\\Downloads\\aptos2019-blindness- detection\\classification\\4"
output_folder_path = "C:\\Users\\mnsle\\Downloads\\aptos2019-blindness- detection\\resized_classification\\4_resized" resize_images_in_folder(input_folder_path, output_folder_path)
