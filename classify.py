import pandas as pd import os
import shutil
excel_file_path = r'C:\Users\mnsle\Downloads\aptos2019-blindness-detection\train.xlsx' source_folder = r'C:\Users\mnsle\Downloads\aptos2019-blindness-detection\train_images' destination_folder = r'C:\Users\mnsle\Downloads\aptos2019-blindness-detection\0'
df = pd.read_excel(excel_file_path) num_categories = 4
for index, row in df.iterrows():
  image_name = row['Image'] 
  category = row['Category']
  if 0 <= category <= num_categories:
    category_folder = os.path.join(destination_folder, f'Category_{category}') 
    os.makedirs(category_folder, exist_ok=True)
    source_path = os.path.join(source_folder, image_name) 
    destination_path = os.path.join(category_folder, image_name) 
    shutil.move(source_path, destination_path)
print("Images segregated into 5 categories based on the information from the Excel file.")
