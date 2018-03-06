import os


class BatchRename():
    '''
    批量重命名文件夹中的图片文件名
    '''

    def __init__(self):
        # 我的图片文件夹路径
        self.path = r'C:/Users/guowei/Desktop/train_model_myself/train'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        n = 6
        for item in filelist:
            if item.endswith('.jpg'):
                n = 6 - len(str(i))
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(0) * n + str(i) + '.jpg')
                try:
                    os.rename(src, dst)
                    print('converting {} to {} ...'.format(src, dst))
                    i += 1
                except:
                    continue
            print('total {} to rename and converted {} jpgs'.format(total_num, i))


if __name__ == '__main__':
    app = BatchRename()
    app.rename()
