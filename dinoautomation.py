import pyautogui
import time
import keyboard

# while True:
#     print(pyautogui.position())
#72,748

pyautogui.click(72,748)
time.sleep(3)
pyautogui.typewrite("chrome")
time.sleep(2)
pyautogui.typewrite(["enter"])
time.sleep(7)
pyautogui.click(250,53)
pyautogui.typewrite("chrome://dino")
pyautogui.typewrite(["enter"])

time.sleep(3)
pyautogui.typewrite(["space"])
pyautogui.click(684,408)


while True:
    ss = pyautogui.screenshot()

    x1 = ss.getpixel((400,480))
    x2 = ss.getpixel((366,480))
    x3 = ss.getpixel((228,480))


    y1 = ss.getpixel((410,426))
    y2 = ss.getpixel((366,426))
    y3 = ss.getpixel((228,426))


    if x1[0]<240 or x2[0]<240 or x3[0]<240 or y1[0]<240 or y2[0]<240 or y3[0]<240:
        pyautogui.keyDown('space')
        time.sleep(0.3)
        pyautogui.keyUp('space')

    if keyboard.is_pressed('esc'):
         break

    # if y3[0]<240 and x3[0]>240:
    # else:
    #     pyautogui.keyDown('down')
    #     # time.sleep(0.5)
    #     # pyautogui.keyUp('down')


    # else:
    #     pyautogui.hold('down')