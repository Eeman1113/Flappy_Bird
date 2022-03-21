import keyboard
quit_game = False
while True:  # making a loop
    print("HIIII")   
    try:  # used try so that if user pressed other than the given key error will not 
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                quit_game=True
                break  # finishing the loop
    except:
        break
    if quit_game:
        break