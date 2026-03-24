from gpiozero import Button 
import time 

button = Button(2)

oldSw = False 
cnt = 1

try: 
    while True:
        newSw = button.is_pressed 
        if newSw != oldSw: 
            oldSw = newSw
            if newSw: 
                print('Click'+str(cnt))
                cnt += 1
            time.sleep(0.2) 
except KeyboardInterrupt: 
    pass
