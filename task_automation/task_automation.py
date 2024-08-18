import os
import shutil

def organized_files(folder):
    files_types = {
        '.txt': 'Text file',
        '.jpg': 'Images',
        '.png': 'Images',
        '.pdf': 'PDFs'

    }
#create a folder for each type of the files
    for subfolder in set(files_types.values()):
        path = os.path.join(folder, subfolder)
        os.makedirs(path, exist_ok=True)

#move file to their respective folder:
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1]
            target = files_types.get(ext)
            if target:
                shutil.move(file_path, os.path.join(folder, target, filename))
                




