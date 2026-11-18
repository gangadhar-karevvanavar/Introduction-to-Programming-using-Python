
import nbformat
from nbconvert import PythonExporter
import os

import os

x = os.listdir(os.getcwd())
print(x)

def convertNotebook(notebookPath, modulePath):

  with open(notebookPath) as fh:
    nb = nbformat.reads(fh.read(), nbformat.NO_CONVERT)

  exporter = PythonExporter()
  source, meta = exporter.from_notebook_node(nb)

  with open(modulePath, 'w+') as fh:
    fh.write(source)

# names = ['220020006.ipynb']
final_arr = []

for names in x:
  print(names)
  print('running........')
  if names[-6:] != ".ipynb":
        continue

  user_name = names[:-6]

  py_file_name = os.getcwd() + '\\Results\\' + user_name + '.py'



  try:
    convertNotebook(names, py_file_name)
  except:
    continue


  txt_file_name = os.getcwd() + '\\Results\\' + user_name + '.txt'




  with open(txt_file_name,"wb") as fout:
      with open(py_file_name,"rb") as fin:
           fout.write(fin.read())



  arr = []
  with open(txt_file_name,'r') as firstfile:
    for i, line in enumerate(firstfile):
      if '# In[' in line:
        arr.append(i)

      if 'Question' in line:
        arr.append(i)


  # print(arr)              


  fin_arr = []
  for j in range(len(arr)-1):
    m = arr[j]
    n = arr[j+1]
    temp_arr = []
    l = m
    while(l < n+1):
      if l not in arr:
        temp_arr.append(l)
      l = l + 1


    # print('-----------')
    fin_arr.append(temp_arr)

  # print(arr)

  last = arr[-1]

  l = last+1
  new_temp_arr = []
  while(l < last+50):
    new_temp_arr.append(l)
    l = l + 1

  fin_arr.append(new_temp_arr)
  # print(fin_arr)




  i = 1

  filepath = os.getcwd() + '\\Results'
  path = filepath + '\\'+ user_name
  path_2 = filepath + '\\' + user_name + '\\text'
  path_3 = filepath + '\\'+ user_name + '\\python'

  if not os.path.exists(path):
    os.mkdir(path)
  if not os.path.exists(path_2):
    os.mkdir(path_2)
  if not os.path.exists(path_3):
    os.mkdir(path_3)


  for line_num in range(len(fin_arr)):
    # print(fin_arr[z])
    if line_num%2 != 0:
      specified_lines = fin_arr[line_num]
      file = open(txt_file_name)

      filepath = os.getcwd() + '\\Results'
      filename = str(i)

      
      filepath2 = filepath + '\\' + user_name + '\\text'+ '\\'+ filename + '.txt'
      
      f2 = open(filepath2, "w")
      f3 = open("libraries.txt", "r")
      for line in f3:
          f2.write(line)
      f2.close()


      with open(filepath2, "a") as f1:
        for pos, l_num in enumerate(file):
        
          if pos in specified_lines:
            f1.write(l_num)
      f1.close()

      # fin = open(filepath2)
      # for line in fin:
      #     if 'input_string' in line:
      #       line.replace('0110O010101', 'bar')

      # fin.close()


      file = open(filepath2, "r")
      replaced_content = ""
      #looping through the file
      flag = 0
      for line in file:

          if 'input(' in line:
            flag = 1
          
          #stripping line break
          # line = line.strip()
          #replacing the texts
          if 'input_string' in line:
            line = line.replace('0110O010101', '0110010101')
          if 'test_list' in line:
            line = line.replace('[90, 67, -34]', '[90, 77, -34]')
          if 'n=6' in line:
            line = line.replace('n=6', 'n=7')
          if 'n = 6' in line:
            line = line.replace('n = 6', 'n = 7')
          if '9774011326' in line:
            line = line.replace('9774011326', '5774011326')
          if 'racecar' in line:
            line = line.replace('racecar', 'race5car')
          




          #concatenate the new string and add an end-line break
          replaced_content = replaced_content + line
          
      #close the file
      file.close()
      #Open file in write mode
      write_file = open(filepath2, "w")
      #overwriting the old file contents with the new/replaced content
      if flag == 1:
        replaced_content = ""

      write_file.write(replaced_content)
      #close the file
      write_file.close()



      filepath3 = filepath + '\\' + user_name+ '\\python'+ '\\'+ filename + '.py'
      with open(filepath3,"wb") as fout:
        with open(filepath2,"rb") as fin:
             fout.write(fin.read())
      fout.close()
      fin.close()



     

      # print('---------------------')
      i = i + 1


  import os
  import subprocess

  filepath = os.getcwd() + '\\Results'
  path_4 = filepath + '\\' + user_name+ '\\outputs'
  if not os.path.exists(path_4):
    os.mkdir(path_4)


  print(user_name)

  for j in range(1,6):
      print(j)
      filepath = os.getcwd() + '\\Results'
      filename = str(j)
      text_file_name = 'out_'+str(j)
      text_filepath = filepath + '\\' + user_name+ '\\outputs'+ '\\'+ text_file_name + '.txt'
      filepath3 = filepath + '\\' + user_name+ '\\python\\' + filename + '.py'

      
      with open(text_filepath, "w+") as output:
          try:
            subprocess.call(["python", filepath3], stdout=output);
          except CalledProcessError:
            print("An exception occurred") 
      output.close()
        

  arr_1 = []
  arr_1.append(user_name)
  for j in range(1, 6):
    filepath = os.getcwd() + '\\Results'
    filename = str(j)
    text_file_name = 'out_'+str(j)
    text_filepath = filepath + '\\' + user_name+ '\\outputs'+ '\\'+ text_file_name + '.txt'
    file = open(text_filepath, "r")
    for line in file:
      # if user_name == '220010015':
      #   print(line)
      if j == 1 and ('Yes' in line) :
        arr_1.append(j)

      if j == 1 and ('yes' in line) :
        arr_1.append(j)


      if j == 1 and ('YES' in line) :
        arr_1.append(j)


       

      if j == 2 and ('[133, -34, 80]' in line):
        arr_1.append(j)
  
    
      if j == 3 and ('140' in line):
        arr_1.append(j)
  
    
      if j == 4 and ('0112345677' in line):
        arr_1.append(j)
    
      # if j == 5 and ('Not' or 'not' or 'No' or 'no' or 'NO' in line) :
      #   arr_1.append(j)

      if j == 5 and ('not'in line) :
        arr_1.append(j)

      if j == 5 and ('No' in line) :
        arr_1.append(j)

      if j == 5 and ('no' in line) :
        arr_1.append(j)

      if j == 5 and ('NO' in line) :
        arr_1.append(j)

      
  print(arr_1)

  new_list = []
  for item in arr_1:
      if item not in new_list:
          new_list.append(item)
      else:
          print(' ')



  final_arr.append(new_list)





  print('----- done----')


filepath = os.getcwd()
import shutil
for k in final_arr:
  if len(k) == 6:
    print(k)
    file = filepath + '\\'+ k[0]+'.ipynb'
    new_path = filepath + '\\5'
    shutil.move(file, new_path)


print('-----------------')
for k in final_arr:
  if len(k) == 5:
    print(k)
    file = filepath + '\\'+ k[0]+'.ipynb'
    new_path = filepath + '\\4'
    shutil.move(file, new_path)

print('---------------------')

for k in final_arr:
  if len(k) == 4:
    print(k)

    file = filepath + '\\'+ k[0]+'.ipynb'
    new_path = filepath + '\\3'
    shutil.move(file, new_path)

print('---------------------')

for k in final_arr:
  if len(k) < 4:
    print(k)

    file = filepath + '\\'+ k[0]+'.ipynb'
    new_path = filepath + '\\unevaluated'
    shutil.move(file, new_path)


