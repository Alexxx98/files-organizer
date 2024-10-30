import os
import argparse
import shutil
import time



class FileOrganizer():
    def __init__(self, start_directory: str, time_limit_in_years: int):
        self.start_directory = start_directory
        self.time_limit_in_years = time_limit_in_years
        self.extensions = {
            'Documents': ('pdf', 'odt', 'ods', 'csv', 'docx'),
            'Pictures': ('jpg', 'png', 'jpeg', 'gif', 'webp'),
            'Music': ('mp3', 'wav', 'm4a'),
            'Videos': ('mp4', 'mov', 'webm'),
            'Applications': ('exe', )
        }

        try:
            os.mkdir(os.path.join(os.path.expanduser('~'), 'Applications'))
            os.mkdir(os.path.join(os.path.expanduser('~'), 'Others'))
        except FileExistsError:
            pass


    def organize(self):
        current_time = time.time()
        for file in os.listdir(self.start_directory):
            file_path = os.path.join(self.start_directory, file)

            # Get file last modification time
            file_mod_time = os.path.getmtime(file_path)

            #Limit time in seconds
            limit_time = self.time_limit_in_years * 365 * 3600 * 24

            # Delete file if older than 2 years
            if current_time - file_mod_time > limit_time:
                try:
                    os.remove(file_path)
                    print(f'removed {file_path.split('\\')[-1]}')
                    continue
                except PermissionError:
                    continue

            if not self.move_file(file_path):
                destination_dir =  os.path.join(os.path.expanduser('~'), 'Others')
                shutil.move(file_path, os.path.join(destination_dir, file))

    
    def move_file(self, file_path: str) -> bool:
        file_name = file_path.split('\\')[-1]
        for file_type, extensions in self.extensions.items():
            if file_name.split('.')[-1] in extensions:
                destination_dir = os.path.join(os.path.expanduser('~'), file_type)
                shutil.move(file_path, os.path.join(destination_dir, file_name))
                return True
        return False
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-dp', '--dir_path',
        type=str,
        default=os.path.join(os.path.expanduser('~'), 'Downloads'),
        help='Specify the full directory path for the directory to organize'
    )
    parser.add_argument(
        '-tl', '--time_limit',
        type=int,
        default=2,
        help='Specify the number of years, after which files will be deleted'
    )
    
    args = parser.parse_args()

    fo = FileOrganizer(start_directory=args.dir_path, time_limit_in_years=args.time_limit)
    fo.organize()
