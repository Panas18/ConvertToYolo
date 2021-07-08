import os
from utils import return_tag, convert_to_yolo

global current_dir 
current_dir = os.getcwd()

def main():
    old_dir = os.path.join(current_dir, 'annotations')
    new_dir = os.path.join(current_dir, 'yolo_annotation')
    files = os.listdir(old_dir)
    for file in files:
        file_path = os.path.join(old_dir, file)
        width, height, bndbox = return_tag(file_path)
        pre, ext = os.path.splitext(file)
        out_file = pre + '.txt'
        out_file_path = os.path.join(new_dir , out_file)
        convert_to_yolo(width, height, bndbox, out_file_path)

if __name__  == "__main__":
    main()
