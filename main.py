import os
import shutil
import re


def main():    
    desktop_path = '/mnt/c/Users/IWDNO/Desktop' if os.name == 'posix' else 'C:\\Users\\IWDNO\\Desktop'
    files = os.listdir(desktop_path)

    groups = {
        
        # files containing "лр" and "захаров"

        '__Лаборатрные работы мои__': r'(?=.*лр)(?=.*захаров)',

        # media files

        '__Медиа__': r'\.(jpg|png|gif|mp4|avi|mp3|wav|webm)',

        # installers (.exe)
        
        '__Установщики__': r'\.(exe)',

        # PDF files (.pdf)
        
        '__PDF__': r'\.(pdf)',

        # archives (.zip, .rar, .7z) 

        '__Архивы__': r'\.(zip|rar|7z)',

        # all Microsoft Office files + text files + mathcad 
        
        '__Рабочие файлы__': r'\.(docx|doc|pptx|ppt|xls|xlsx|vsdx|xmcd|xml|txt)',
    }    

    for file in files:
        for directory in groups.keys():
            if not re.search(groups[directory], file.lower()):
                continue
            
            new_directory = os.path.join(desktop_path, directory)
            if not os.path.exists(new_directory):
                os.mkdir(new_directory)
            
            shutil.move(
                os.path.join(desktop_path, file),
                os.path.join(new_directory, file)
            )

            break


if __name__ == "__main__":
    main()
    