import os
from string import ascii_uppercase
import shutil
import datetime
import PIL
from PIL import Image



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
    for r, d, f in os.walk(os.path.normpath(path)):
        for file in f:
            file_ext_lower = os.path.splitext(file)[1].lower()
            if file_ext_lower in image_file_extensions:
                file_path       = os.path.join(r, file)
                file_name       = os.path.splitext(file)[0]
                file_extension  = os.path.splitext(file)[1]
                files.append((file_path, file_name, file_extension, file))
    return files 
    
def copy_images(input_path, output_path):
    image_list = get_list_of_images_to_import(input_path)
    files_moved = []
    for image in image_list:
        shutil.copy2(image[0], output_path)
        files_moved.append((image, datetime.datetime.now()))
    return files_moved

def move_images(input_path, output_path):
    image_list = get_list_of_images_to_import(input_path)
    files_moved = []
    for image in image_list:
        shutil.move(image[0], output_path)
        files_moved.append((image, datetime.datetime.now()))
    return files_moved
    
        
def get_date_taken(image):
    datetime_str = Image.open(image)._getexif()[36867]
    # return datetime_str
    dt_obj = datetime.datetime.strptime(datetime_str, '%Y:%m:%d %H:%M:%S')
    return dt_obj

# Currently works for JPEG.
def set_reorg_dest_folder(image):
    date_taken = get_date_taken(image)
    folder_0 = date_taken.strftime("%Y")
    folder_1 = date_taken.strftime("%Y_%m")
    folder_2 = date_taken.strftime("%Y_%m_%d")
    return (folder_0, folder_1, folder_2)


## test code

# img_file = 'C:\\Users\\world\\Pictures\\Import\\IMG_6484.JPG'

# image_date = get_date_taken(img_file)
# print(image_date.year)
# print(get_date_taken(img_file))
# print("type of date_string =", type(get_date_taken(img_file)))
# print(set_reorg_dest_folder(img_file))
