import os
from string import ascii_uppercase
import shutil
import datetime


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
        

## Test Code
# test_list = get_list_of_images_to_import(input_path)
# move_images(test_list)
        
# input_path = 'C:\\Users\\world\\Pictures\\Import\\'
# output_path = 'C:\\Users\\world\\Pictures\\Export\\'
# move_images(input_path, output_path)

# print(get_list_of_images_to_import('e:\\'))



# path = '\\\\DISKSTATION\\photo\\2021\\2021_08_17\\'
# path = 'e:/'
# path = 'c:/Users/world/Pictures/Import'
# output_path = 'c:/Users/world/Pictures/Export'
# a = get_list_of_images_to_import(path)
# for i in a:
#     print(i)
#     print(i[0])
#     print(os.path.getsize(i[0]))
#     shutil.copy(i[0], output_path)



# def set_output_folder():
#     pass



