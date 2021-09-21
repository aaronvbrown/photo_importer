import os
from string import ascii_uppercase
import shutil
from tkinter.filedialog import askdirectory
# from PIL import Image

image_file_extensions = [
    '.jpeg'
    ,'.jpg'
    ,'.cr2'
    ,'.png'
    ,'.bmp'
    ,'.mov'
    ,'.mp4'
    ,'.avi'
]
input_path = 'e:\\'
output_path = 'C:\\Users\\world\\Pictures\\Import\\'



def get_drive_list():
    available_drives = [f'{d}:' for d in ascii_uppercase if os.path.exists(f'{d}:')]
    return available_drives

def get_mount_drive_list():
    mount_drives = [f'{d}' for d in get_drive_list() if os.path.ismount(d)]
    return mount_drives

def get_non_mount_drive_list():
    non_mount_drives = [f"{d}" for d in get_drive_list() if not os.path.ismount(d)]
    return non_mount_drives


# Create a list of image filepaths, names and extensions.
def get_list_of_images_to_import(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            file_ext_lower = os.path.splitext(file)[1].lower()
            if file_ext_lower in image_file_extensions:
                file_path       = os.path.join(r, file)
                file_name       = os.path.splitext(file)[0]
                file_extension  = os.path.splitext(file)[1]
                files.append((file_path, file_name, file_extension))
    return files 


    
    
    
def move_images(image_list):
    for image in image_list:
        shutil.copy(image[0], output_path)
        
# test_list = get_list_of_images_to_import(input_path)
# move_images(test_list)

# print(get_list_of_images_to_import('e:\\'))
# path = '\\\\DISKSTATION\\photo\\2021\\2021_08_17\\'
# path = 'e:\\'
# a = get_list_of_images_to_import(path)
# for i in a:
#     print(i)



# def set_output_folder():
#     pass



