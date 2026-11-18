import runpy
import os
import subprocess

filepath = os.getcwd()
path_4 = filepath + '\collections\\outputs'
if not os.path.exists(path_4):
  os.mkdir(path_4)

for j in range(1,11):
    filepath = os.getcwd()
    filename = str(j)
    text_file_name = 'out_'+str(j)
    text_filepath = filepath + '\collections\\outputs'+ '\\'+ text_file_name + '.txt'
    filepath3 = 'collections\\python\\' + filename + '.py'
    with open(text_filepath, "w+") as output:
        subprocess.call(["python", filepath3], stdout=output);
    output.close()
