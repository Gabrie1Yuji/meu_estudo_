# Primeiro processo de automatizacao

#Abrir o google drive no computador
#Entrar na minha area de trabalho 
#Pegar o arquivo e jogar no drive 
import time
import pyautogui

pyautogui.alert("O codigo vai comecar. Nao digite nada enquanto o comando rodar")
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://g1.globo.com/')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'g')





