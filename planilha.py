from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import pyperclip
import keyboard

pyautogui.PAUSE = 0.3

tecla_sair = 'esc'
x = int(input("quantas linhas quer preencher? "))
print("mova o mouse até o icone da planilha\n")
for seg in range(0,6):
    print(5-seg,"\n")
    time.sleep(1)
    
pos_x, pos_y = pyautogui.position()
i=1
while i < x:
    
    if keyboard.is_pressed(tecla_sair):
        print("Saindo...")
        break
    
    pyautogui.click(pos_x, pos_y) # planilha
    pyautogui.hotkey('down')
    
    i+=1
     
    
    
    
    time.sleep(0.5)

input("Pressione Enter para sair...")

