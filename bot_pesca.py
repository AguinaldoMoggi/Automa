import keyboard
import my_keyboard
from time import sleep
from actions import minigame, set_fishing_rod, wait_bubble



keyboard.wait('~')
while True:
    fishing_position = set_fishing_rod()
    wait_bubble(fishing_position)
    minigame()
    my_keyboard.press('f11')
    sleep(1)
    
    
    
                                                  
