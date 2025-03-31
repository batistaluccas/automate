from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui
import pyperclip

pyautogui.PAUSE = 0.3

# WebDriver gerenciado automaticamente
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

pyautogui.click(501, 85)  
pyautogui.write('youtube.com')
pyautogui.press('enter')

pesquisa = navegador.find_element("name", "search_query")
pesquisa.send_keys('processo de solda ponto')
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveTo(500, 500)
pyautogui.scroll(-1300)

pyautogui.hotkey('ctrl', 'n')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

espera = WebDriverWait(navegador, 10)
espera.until(EC.number_of_windows_to_be(2))
janelas = navegador.window_handles
navegador.switch_to.window(janelas[1])

pyautogui.click(501, 85)
pyautogui.write('https://www.convertworld.com/pt/')
pyautogui.press('enter')
time.sleep(2)
pyautogui.moveTo(500, 500)
pyautogui.scroll(-300)
form_lbr = navegador.find_element("id", "conv_weight")
input_lbr = form_lbr.find_element("name", "amount")
input_lbr.send_keys('2')
time.sleep(1)
valor = form_lbr.find_element("tag name", "b").text
pyperclip.copy(valor)

time.sleep(3)

navegador.switch_to.window(janelas[0])

pyautogui.click(501, 85)  
pyautogui.write('https://www.calculadoraonline.com.br/basica')
pyautogui.press('enter')

time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('backspace', presses=2)
pyautogui.write('/0,45')
pyautogui.press('enter')


print(pyautogui.size())


time.sleep(5)



