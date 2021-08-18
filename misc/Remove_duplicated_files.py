"""
Created on Tue Dec 17 11:13:30 2019

"""

import os

path = 'C:/Users/'

os.chdir(path)

print('Currend Directory: ' + str(os.getcwd()))

picture_png = []
remove_list = []

copy_marker = [' - Copy', ' (1)']

for f in os.listdir():
    if '.png' in f:
        picture_png.append(f)

for pic in picture_png:
    copy_pic = pic
    pic_name, pic_ext = os.path.splitext(pic)
    if any(x in pic_name for x in copy_marker):
        for marker in copy_marker:
            copy_pic = copy_pic.replace(marker, '')
        if copy_pic in picture_png:
            remove_list.append(pic)
            os.remove(pic)
            
print('Originale Anzahl an png Bilder: ' + str(len(picture_png)))
print('Anzahl gelöschte Bilder: ' + str(len(remove_list)))
