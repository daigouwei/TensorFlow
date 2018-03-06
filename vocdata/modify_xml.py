import os

path = r'D:/Pycharm/models/research/object_detection/own_train_model/data/VOC2007/Annotations'
files = os.listdir(path)
lines = []
for file in files:
    with open(path+'/'+file, 'r') as fo:
        lines = fo.readlines()
        lines[1] = r'    <folder>VOC2007</folder>'+'\n'
        print(lines)

    with open(path+'/'+file, 'w') as fo:
        fo.writelines(lines)
