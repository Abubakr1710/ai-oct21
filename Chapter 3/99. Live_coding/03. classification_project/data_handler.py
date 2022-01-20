import os


class DataHandler:

    def __init__(self, root_dir, train_size=.7) -> None:
        self.train_size = train_size
        self.root_dir = root_dir

    def folder_structure(self, img_folder, dest_folders = ['train', 'test']):
        classes = os.listdir(img_folder)


        for item in dest_folders:
            for i in range(len(classes)):
                os.system(f'mkdir -p {self.root_dir}/datasets/{item}/{str(i)}')

        # folder structure like this:   datasets/train/0
        #                               datasets/train/1
        #                               datasets/test/0
        #                               datasets/test/1
        #                               datasets/val/0
        #                               datasets/val/1

loader = DataHandler('/home/alessio/Desktop')

loader.folder_structure(loader.root_dir + '/img')



    








# loader = DataHandler()

# print(loader.something)

# from sklearn.model_selection import train_test_split

# xtr, xte, ytr, yte = train_test_split(X, y, train_size=.7)