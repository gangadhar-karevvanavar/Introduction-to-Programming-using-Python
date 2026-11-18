# import pandas lib as pd
import pandas as pd
import numpy as np
 
# read by default 1st sheet of an excel file
df = pd.read_excel('marks.xlsx')
 
# print(dataframe1)
# df.fillna(0)
df['Q1'] = df['Q1'].fillna(0)
df['Q2'] = df['Q2'].fillna(0)
df['Q3'] = df['Q3'].fillna(0)
df['Q4'] = df['Q4'].fillna(0)
df['Q5'] = df['Q5'].fillna(0)
df['TOTAL'] = df['TOTAL'].fillna(0)

l = df.values.tolist()

# web_link = 'https://classroom.google.com/g/tg/NTg3ODk3ODcxMTgx/NTE2MDA5MzMxNDA3#u=' + 'NTg4MTU5Njc4MjIy' + '&t=f'



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# def browser_function(weblink):
#     driver_path = './chromedriver.exe'
#     chr_options = Options()
#     chr_options.add_experimental_option("detach", True)
#     chr_driver = webdriver.Chrome(driver_path, options=chr_options)
#     chr_driver.get(weblink)

# driver_path = './chromedriver.exe'
# chr_options = Options()
# chr_options.add_experimental_option("detach", True)
# chr_driver = webdriver.Chrome(driver_path, options=chr_options)

# import System

# System.setProperty("webdriver.chrome.driver","path of chromedriver.exe");
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui

from selenium.webdriver.common.action_chains import ActionChains

def browser_function(weblink, num, marks_details):
    options = webdriver.ChromeOptions() 
    options.add_argument("user-data-dir=C:/Users/Gangadhar13/AppData/Local/Google/Chrome/User Data") 
    options.add_experimental_option("detach", True)#Path to your chrome profile
    w = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options) 
    w.get(weblink)

    act = ActionChains(w)
    
    element = w.find_element(By.CLASS_NAME, 'FtBNWb').click()
    
    


    pyautogui.moveTo(1730, 610)
    pyautogui.click()
    pyautogui.click()
 
    pyautogui.write(num)  


    

    
   
    pyautogui.moveTo(1747, 763)
    pyautogui.click()
    pyautogui.click()
    pyautogui.write(marks_details)

    # time.sleep(5)
    # print(pyautogui.position())

    


    pyautogui.moveTo(1860, 863)
    pyautogui.click()

    # pyautogui.moveTo(1860, 873)
    # pyautogui.click()

    time.sleep(2)

    # time.sleep(5)
    # print(pyautogui.position())

    



    pyautogui.moveTo(1794, 247)
    pyautogui.click()

    # time.sleep(5)
    # print(pyautogui.position())

    # time.sleep(5)

    # print(pyautogui.position())
    
    pyautogui.moveTo(1183, 681)
    pyautogui.click()


    time.sleep(4)

  


    w.close()

for j in l[63:]:
    print(l.index(j), '--', j[1], '--', j[1])

    batch = j[10]
    Id_name = j[9]
   
    if batch == 4:



        web_link = 'https://classroom.google.com/g/tg/NTg3ODk3ODcxMTgx/NTE3NDU4Mjc4NjQ3#u=' + Id_name + '&t=f'

    # if batch == 2:
    #     web_link = 'https://classroom.google.com/g/tg/NTg3ODk3ODcxMTgx/NTE2MDg0OTg1MTAx#u=' + Id_name + '&t=f'
    # if batch == 3:
    #     web_link = 'https://classroom.google.com/g/tg/NTg3ODk3ODcxMTgx/NTkzNTc2MjA0MTA2#u=' + Id_name + '&t=f'
    # if batch == 4:
    #     web_link = 'https://classroom.google.com/g/tg/NTg3ODk3ODcxMTgx/NTE2MDE3Nzg1OTkw#u=' + Id_name + '&t=f'

    mark = str(j[8])

 
    comment = '('+ str(j[3]) + '/2)' + '('+str(j[4])+ '/3)'+ '('+str(j[5])+ '/3)'+ '('+str(j[6])+ '/2)'
    # print(comment)
    browser_function(web_link, mark, comment)
