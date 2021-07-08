import os
import xml.etree.ElementTree as et

global old_annotation 
global yolo_annotation
old_annotation= 'annotations'
yolo_annotation = 'yolo_annotation'

def return_tag(xml_file):
    test_file = os.path.join(old_annotation, xml_file)
    doc = et.parse(test_file)
    root = doc.getroot()
    bndbox= []
    for obj in root.findall('object'):
        for val in obj.find('bndbox'):
            bndbox.append(int(val.text))

    for size in root.findall('size'):
        width = size.findall('width')
        height = size.findall('height')
    return int(width[0].text), int(height[0].text), bndbox


def convert_to_yolo(width, height, bndbox ,yolo_file, obj_class=0):
    while bndbox:
        xmin = bndbox.pop(0)
        ymin = bndbox.pop(0)
        xmax = bndbox.pop(0)
        ymax = bndbox.pop(0)
        
        x = ((xmax -xmin) / 2 + xmin)/ width
        y = ((ymax - ymin) / 2 + ymin)/ height
        w =((xmax - xmin))/height
        h = ((ymax-ymin))/height

        file_path = os.path.join(yolo_annotation,yolo_file) 
        with open (file_path, 'a') as f:
           f.write(f"{obj_class},{x},{y},{w},{h}\n") 

if __name__ == "__main__":
    width, height, bndbox = return_tag('Cars71.xml')
    convert_to_yolo(width, height, bndbox, 'Cars0.txt')
