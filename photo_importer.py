import os    
from string import ascii_uppercase
import shutil
import datetime
import PIL
from PIL import Image

class FileImport:
    def __init__(self, input_path, output_path):
        self._name = self
        self.input_path = input_path
        self.output_path = output_path
    
    actions     = ['Move', 'Copy', 'Reorg', 'Rename', 'RemoveEmpty']
    filetype    = ['images', 'videos', 'documents', 'sounds', 'downloads', 'archives']
    ext_file_archive = [
        '.zip',
        '.7z',
    ]

    ext_document = [
        '.pdf',
        '.docs',
        '.xlsx',
        '.doc',
        '.xls',
    ]

    ext_download = [
        '.crdownload',
    ]

    ext_sound = [
        '.mp3',
        '.wav',
    ]

    ext_video = [
        '.mp4',
        '.m2ts',
        '.mpeg',
        '.mov',
        '.avi',
    ]

    ext_image = [
        '.jpeg',
        '.jpg',
        '.cr2',
        '.png',
        '.gif',
        '.bmp',
        '.mov',
        '.mp4',
        '.avi',
    ]


    def get_drive_list(self):
        available_drives = [f'{d}:' for d in ascii_uppercase if os.path.exists(f'{d}:')]
        return available_drives

    def get_mount_drive_list(self):
        mount_drives = [f'{d}' for d in get_drive_list() if os.path.ismount(d)]
        return mount_drives

    def get_non_mount_drive_list(self):
        non_mount_drives = [f"{d}" for d in get_drive_list() if not os.path.ismount(d)]
        return non_mount_drives


    # Create a list of filepaths, names and extensions to import.
    def get_import_folder_files(self, path):
        files = []
        # r=root, d=directories, f=files
        for r, d, f in os.walk(os.path.normpath(path)):
            for file in f:
                file_path       = os.path.join(r, file)
                file_name       = os.path.splitext(file)[0]
                file_extension  = os.path.splitext(file)[1]
                files.append((file_path, file_name, file_extension, file))
        return files 
    
    def get_list_of_images_to_import(self):
        files = [f for f in self.get_import_folder_files(self.input_path) if f[2].lower() in (self.ext_image + self.ext_video)]
        return files 
        
    def copy_images(self):
        image_list = self.get_list_of_images_to_import(self.input_path)
        files_moved = []
        for image in image_list:
            shutil.copy2(image[0], self.output_path)
            files_moved.append((image, datetime.datetime.now()))
        return files_moved

    def move_images(self):
        image_list = self.get_list_of_images_to_import()
        files_moved = []
        for image in image_list:
            shutil.move(image[0], self.output_path)
            files_moved.append((image, datetime.datetime.now()))
        return files_moved
    

    # #  Below is a feature addition for reorganizing folder in the future. 
            
    # Returns the date taken as a datetime object.
    def get_date_taken(self, image):
        if image.lower.endswith(".jpg"):
            return get_date_taken_jpeg(image)

    # Returns the date taken as a datetime object for JPEG files.
    def get_date_taken_jpeg(self, image):
        datetime_str = Image.open(image)._getexif()[36867]
        dt_obj = datetime.datetime.strptime(datetime_str, '%Y:%m:%d %H:%M:%S')
        return dt_obj

    def get_date_taken_cr2(self, image):
        # TODO:  replace with functional cr2 code 
        datetime_str = Image.open(image)._getexif()[36867]
        dt_obj = datetime.datetime.strptime(datetime_str, '%Y:%m:%d %H:%M:%S')
        return dt_obj

    def get_destination_folder(self):
        # if reorg_flag == False:
        #     return base_export_folder
        # else: 
        #     if: reorg_flag == date_taken:
        #         return set(return base_export_folder
        print("get_dest_folder Not yet implemented")
    
    def set_dest_folder_date_taken(self, image):
        date_taken = get_date_taken(image)
        folder_0 = date_taken.strftime("%Y")
        folder_1 = date_taken.strftime("%Y_%m")
        folder_2 = date_taken.strftime("%Y_%m_%d")
        return (folder_0, folder_1, folder_2)

    def set_dest_folder_date_today(self, image):
        pass

    def set_dest_folder_date_created(self, image):
        pass

    def set_dest_folder_date_modified(self, image):
        pass



# Test Code
# input_folder = 'C:\\Users\\world\\Pictures\\Export\\'
# output_folder = 'C:\\Users\\world\\Pictures\\Import\\'
# session = FileImport(input_folder, output_folder)