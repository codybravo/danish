import os,shutil
d = os.getcwd()
for i in range(5):
    os.mkdir(f'new{i}')
    shutil.copy('2.jpeg',f'{d}/new{i}')
