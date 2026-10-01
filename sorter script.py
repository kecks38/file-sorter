from pathlib import Path
import shutil
path = Path(r"C:\TEST")

def all_files():
    files = [x for x in path.iterdir() if x.is_file()]
    return files

files = all_files()

folders = {".abc": "abc_files", ".bmp": "bmp_files", ".txt": "txt_files",
           ".zip": "zip_files"
}

for file in (files):
    
    folder = folders.get(file.suffix.lower(), "other_files" )  

    papka = path / folder
    papka.mkdir(exist_ok=True)

    try:
        shutil.move(file, papka)
    except(shutil.Error):
        print(f"Пропущен {file.name} файл")