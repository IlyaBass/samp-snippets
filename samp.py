import pyautogui
import keyboard

lock_command = '/lock'
god_command = '/god'
v_command = '/v'
t_command = '/t'
go_command = '/go '
lcar_command = '/lcar'
w_command = '/w'
jp_command = '/jp'
para_command = '/para'

def lock(): 
    pyautogui.press('f6')
    pyautogui.write(lock_command)
    pyautogui.press('enter') 

def god(): 
    pyautogui.press('f6')
    pyautogui.write(god_command)
    pyautogui.press('enter') 

def cars(): 
    pyautogui.press('f6')
    pyautogui.write(v_command)
    pyautogui.press('enter') 

def teleport(): 
    pyautogui.press('f6')
    pyautogui.write(t_command)
    pyautogui.press('enter') 

def go(): 
    pyautogui.press('f6')
    pyautogui.write(go_command)  

def lcar(): 
    pyautogui.press('f6')
    pyautogui.write(lcar_command)
    pyautogui.press('enter')
    pyautogui.press('enter')

def guns(): 
    pyautogui.press('f6')
    pyautogui.write(w_command)
    pyautogui.press('enter')
    pyautogui.press('enter')

def jetpack(): 
    pyautogui.press('f6')
    pyautogui.write(jp_command)
    pyautogui.press('enter')

def para(): 
    pyautogui.press('f6')
    pyautogui.write(para_command)
    pyautogui.press('enter')

def close():
	print('The programm has stoped')
	quit()	

keyboard.add_hotkey('0 + L', lock)
keyboard.add_hotkey('0 + Z', god)
keyboard.add_hotkey('0 + B', cars)
keyboard.add_hotkey('0 + U', teleport)
keyboard.add_hotkey('0 + N', go)
keyboard.add_hotkey('0 + I', lcar)
keyboard.add_hotkey('0 + M', guns)
keyboard.add_hotkey('0 + J', jetpack)
keyboard.add_hotkey('0 + P', para)
keyboard.add_hotkey('0 + K', close)

# вписать это в консоль для запуска скрипта ===> py -i samp.py