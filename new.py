import os,shutil
print("wait for 2 to 3 minutes")
d = os.getcwd()
for i in range(5):
    os.mkdir(f'new{i}')
    shutil.copy('2.jpeg',f'{d}/new{i}')
