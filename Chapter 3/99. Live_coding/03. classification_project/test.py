import os

img_folder = 'img'

classes = os.listdir(img_folder)

paths = ['train', 'test']

# for f in img_folder:
#     for p in f:
#         print(p)

# for item in paths:
#     for i in range(len(classes)):
#         os.system(f'mkdir -p ./datasets/{item}/{str(i)}')

# os.system('mv /path/to/the/source path/to/destination')
# 'img/person/0_7.png'

# files = os.listdir(img_folder + '/' + classes[0])

path_to_img = 'img'+'/'+'person'

# print(path_to_img)

files = os.listdir(path_to_img)
files = sorted(files)
print(files[1])

# for item in classes:
#     for i in range(len(item)):
#         print(item[i])
