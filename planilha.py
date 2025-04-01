from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import pyperclip

pyautogui.PAUSE = 0.3


for i in range(1, 6):
    
    
    pyautogui.click(1150, 1051) # planilha
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('down')
    pyautogui.click(975, 1051) # google
    pyautogui.moveTo(1730, 260)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.moveTo(27, 70)
    pyautogui.click()
    print(i)
     
    
    
    
    time.sleep(0.5)


