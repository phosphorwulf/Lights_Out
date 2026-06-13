"""
  _________  __  __ _____  _____   ______ __  __ _____  ______ __ __ __ __  __ __     ______
  \_  ___  // / / // __  // ____\ \ __  // / / // __  // __  // // // // / / // /    / ____/
   / /__/ // /_/ // / / // /__   / /_/ // /_/ // / / // /_/ // // // // / / // /    / /__
  / _____// __  // / / / \___ \ / ____// __  // / / // _  _// // // // / / // /    / ___/
 / /     / / / // /_/ /_____/ // /    / / / // /_/ // / \ \ \ V  V // /_/ // /___ / /
/_/     /_/ /_//_____//______//_/    /_/ /_//_____//_/  \_\ \__/\_/\_____//_____//_/
"""
import tkinter as tk


light_array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def restart_btn():
    light_array[0] = 1
    light_array[1] = 1
    light_array[2] = 1
    light_array[3] = 1
    light_array[4] = 1
    light_array[5] = 1
    light_array[6] = 1
    light_array[7] = 1
    light_array[8] = 1
    light_array[9] = 1
    light_array[10] = 1
    light_array[11] = 1
    light_array[12] = 1
    light_array[13] = 1
    light_array[14] = 1
    light_array[15] = 1
    light_array[16] = 1
    light_array[17] = 1
    light_array[18] = 1
    light_array[19] = 1
    light_array[20] = 1
    light_array[21] = 1
    light_array[22] = 1
    light_array[23] = 1
    light_array[24] = 1
    light0.config(image=LightOn)
    light1.config(image=LightOn)
    light2.config(image=LightOn)
    light3.config(image=LightOn)
    light4.config(image=LightOn)
    light5.config(image=LightOn)
    light6.config(image=LightOn)
    light7.config(image=LightOn)
    light8.config(image=LightOn)
    light9.config(image=LightOn)
    light10.config(image=LightOn)
    light11.config(image=LightOn)
    light12.config(image=LightOn)
    light13.config(image=LightOn)
    light14.config(image=LightOn)
    light15.config(image=LightOn)
    light16.config(image=LightOn)
    light17.config(image=LightOn)
    light18.config(image=LightOn)
    light19.config(image=LightOn)
    light20.config(image=LightOn)
    light21.config(image=LightOn)
    light22.config(image=LightOn)
    light23.config(image=LightOn)
    light24.config(image=LightOn)

def quit_btn():
    root.destroy()

def game_over():
    if sum(light_array) == 0:
        print("you win")
        #set window to image
        #sleep few seconds
        root.destroy()

def press_light0():
    if light_array[0]:
        light0.config(image=LightOff)
        light_array[0] = 0
    else:
        light0.config(image=LightOn)
        light_array[0] = 1
    if light_array[1]:
        light1.config(image=LightOff)
        light_array[1] = 0
    else:
        light1.config(image=LightOn)
        light_array[1] = 1
    if light_array[5]:
        light5.config(image=LightOff)
        light_array[5] = 0
    else:
        light5.config(image=LightOn)
        light_array[5] = 1
    game_over()

def press_light1():
    if light_array[1]:
        light1.config(image=LightOff)
        light_array[1] = 0
    else:
        light1.config(image=LightOn)
        light_array[1] = 1
    if light_array[0]:
        light0.config(image=LightOff)
        light_array[0] = 0
    else:
        light0.config(image=LightOn)
        light_array[0] = 1
    if light_array[2]:
        light2.config(image=LightOff)
        light_array[2] = 0
    else:
        light2.config(image=LightOn)
        light_array[2] = 1
    if light_array[6]:
        light6.config(image=LightOff)
        light_array[6] = 0
    else:
        light6.config(image=LightOn)
        light_array[6] = 1
    game_over()

def press_light2():
    if light_array[2]:
        light2.config(image=LightOff)
        light_array[2] = 0
    else:
        light2.config(image=LightOn)
        light_array[2] = 1
    if light_array[1]:
        light1.config(image=LightOff)
        light_array[1] = 0
    else:
        light1.config(image=LightOn)
        light_array[1] = 1
    if light_array[3]:
        light3.config(image=LightOff)
        light_array[3] = 0
    else:
        light3.config(image=LightOn)
        light_array[3] = 1
    if light_array[7]:
        light7.config(image=LightOff)
        light_array[7] = 0
    else:
        light7.config(image=LightOn)
        light_array[7] = 1
    game_over()

def press_light3():
    if light_array[3]:
        light3.config(image=LightOff)
        light_array[3] = 0
    else:
        light3.config(image=LightOn)
        light_array[3] = 1
    if light_array[2]:
        light2.config(image=LightOff)
        light_array[2] = 0
    else:
        light2.config(image=LightOn)
        light_array[2] = 1
    if light_array[4]:
        light4.config(image=LightOff)
        light_array[4] = 0
    else:
        light4.config(image=LightOn)
        light_array[4] = 1
    if light_array[8]:
        light8.config(image=LightOff)
        light_array[8] = 0
    else:
        light8.config(image=LightOn)
        light_array[8] = 1
    game_over()

def press_light4():
    if light_array[4]:
        light4.config(image=LightOff)
        light_array[4] = 0
    else:
        light4.config(image=LightOn)
        light_array[4] = 1
    if light_array[3]:
        light3.config(image=LightOff)
        light_array[3] = 0
    else:
        light3.config(image=LightOn)
        light_array[3] = 1
    if light_array[9]:
        light9.config(image=LightOff)
        light_array[9] = 0
    else:
        light9.config(image=LightOn)
        light_array[9] = 1
    game_over()

def press_light5():
    if light_array[5]:
        light5.config(image=LightOff)
        light_array[5] = 0
    else:
        light5.config(image=LightOn)
        light_array[5] = 1
    if light_array[0]:
        light0.config(image=LightOff)
        light_array[0] = 0
    else:
        light0.config(image=LightOn)
        light_array[0] = 1
    if light_array[6]:
        light6.config(image=LightOff)
        light_array[6] = 0
    else:
        light6.config(image=LightOn)
        light_array[6] = 1
    if light_array[10]:
        light10.config(image=LightOff)
        light_array[10] = 0
    else:
        light10.config(image=LightOn)
        light_array[10] = 1
    game_over()

def press_light6():
    if light_array[6]:
        light6.config(image=LightOff)
        light_array[6] = 0
    else:
        light6.config(image=LightOn)
        light_array[6] = 1
    if light_array[1]:
        light1.config(image=LightOff)
        light_array[1] = 0
    else:
        light1.config(image=LightOn)
        light_array[1] = 1
    if light_array[5]:
        light5.config(image=LightOff)
        light_array[5] = 0
    else:
        light5.config(image=LightOn)
        light_array[5] = 1
    if light_array[7]:
        light7.config(image=LightOff)
        light_array[7] = 0
    else:
        light7.config(image=LightOn)
        light_array[7] = 1
    if light_array[11]:
        light11.config(image=LightOff)
        light_array[11] = 0
    else:
        light11.config(image=LightOn)
        light_array[11] = 1
    game_over()

def press_light7():
    if light_array[7]:
        light7.config(image=LightOff)
        light_array[7] = 0
    else:
        light7.config(image=LightOn)
        light_array[7] = 1
    if light_array[2]:
        light2.config(image=LightOff)
        light_array[2] = 0
    else:
        light2.config(image=LightOn)
        light_array[2] = 1
    if light_array[6]:
        light6.config(image=LightOff)
        light_array[6] = 0
    else:
        light6.config(image=LightOn)
        light_array[6] = 1
    if light_array[8]:
        light8.config(image=LightOff)
        light_array[8] = 0
    else:
        light8.config(image=LightOn)
        light_array[8] = 1
    if light_array[12]:
        light12.config(image=LightOff)
        light_array[12] = 0
    else:
        light12.config(image=LightOn)
        light_array[12] = 1
    game_over()

def press_light8():
    if light_array[8]:
        light8.config(image=LightOff)
        light_array[8] = 0
    else:
        light8.config(image=LightOn)
        light_array[8] = 1
    if light_array[3]:
        light3.config(image=LightOff)
        light_array[3] = 0
    else:
        light3.config(image=LightOn)
        light_array[3] = 1
    if light_array[7]:
        light7.config(image=LightOff)
        light_array[7] = 0
    else:
        light7.config(image=LightOn)
        light_array[7] = 1
    if light_array[9]:
        light9.config(image=LightOff)
        light_array[9] = 0
    else:
        light9.config(image=LightOn)
        light_array[9] = 1
    if light_array[13]:
        light13.config(image=LightOff)
        light_array[13] = 0
    else:
        light13.config(image=LightOn)
        light_array[13] = 1
    game_over()

def press_light9():
    if light_array[9]:
        light9.config(image=LightOff)
        light_array[9] = 0
    else:
        light9.config(image=LightOn)
        light_array[9] = 1
    if light_array[4]:
        light4.config(image=LightOff)
        light_array[4] = 0
    else:
        light4.config(image=LightOn)
        light_array[4] = 1
    if light_array[8]:
        light8.config(image=LightOff)
        light_array[8] = 0
    else:
        light8.config(image=LightOn)
        light_array[8] = 1
    if light_array[14]:
        light14.config(image=LightOff)
        light_array[14] = 0
    else:
        light14.config(image=LightOn)
        light_array[14] = 1
    game_over()

def press_light10():
    if light_array[10]:
        light10.config(image=LightOff)
        light_array[10] = 0
    else:
        light10.config(image=LightOn)
        light_array[10] = 1
    if light_array[5]:
        light5.config(image=LightOff)
        light_array[5] = 0
    else:
        light5.config(image=LightOn)
        light_array[5] = 1
    if light_array[11]:
        light11.config(image=LightOff)
        light_array[11] = 0
    else:
        light11.config(image=LightOn)
        light_array[11] = 1
    if light_array[15]:
        light15.config(image=LightOff)
        light_array[15] = 0
    else:
        light15.config(image=LightOn)
        light_array[15] = 1
    game_over()

def press_light11():
    if light_array[11]:
        light11.config(image=LightOff)
        light_array[11] = 0
    else:
        light11.config(image=LightOn)
        light_array[11] = 1
    if light_array[6]:
        light6.config(image=LightOff)
        light_array[6] = 0
    else:
        light6.config(image=LightOn)
        light_array[6] = 1
    if light_array[10]:
        light10.config(image=LightOff)
        light_array[10] = 0
    else:
        light10.config(image=LightOn)
        light_array[10] = 1
    if light_array[12]:
        light12.config(image=LightOff)
        light_array[12] = 0
    else:
        light12.config(image=LightOn)
        light_array[12] = 1
    if light_array[16]:
        light16.config(image=LightOff)
        light_array[16] = 0
    else:
        light16.config(image=LightOn)
        light_array[16] = 1
    game_over()

def press_light12():
    if light_array[12]:
        light12.config(image=LightOff)
        light_array[12] = 0
    else:
        light12.config(image=LightOn)
        light_array[12] = 1
    if light_array[7]:
        light7.config(image=LightOff)
        light_array[7] = 0
    else:
        light7.config(image=LightOn)
        light_array[7] = 1
    if light_array[11]:
        light11.config(image=LightOff)
        light_array[11] = 0
    else:
        light11.config(image=LightOn)
        light_array[11] = 1
    if light_array[13]:
        light13.config(image=LightOff)
        light_array[13] = 0
    else:
        light13.config(image=LightOn)
        light_array[13] = 1
    if light_array[17]:
        light17.config(image=LightOff)
        light_array[17] = 0
    else:
        light17.config(image=LightOn)
        light_array[17] = 1
    game_over()

def press_light13():
    if light_array[13]:
        light13.config(image=LightOff)
        light_array[13] = 0
    else:
        light13.config(image=LightOn)
        light_array[13] = 1
    if light_array[8]:
        light8.config(image=LightOff)
        light_array[8] = 0
    else:
        light8.config(image=LightOn)
        light_array[8] = 1
    if light_array[12]:
        light12.config(image=LightOff)
        light_array[12] = 0
    else:
        light12.config(image=LightOn)
        light_array[12] = 1
    if light_array[14]:
        light14.config(image=LightOff)
        light_array[14] = 0
    else:
        light14.config(image=LightOn)
        light_array[14] = 1
    if light_array[18]:
        light18.config(image=LightOff)
        light_array[18] = 0
    else:
        light18.config(image=LightOn)
        light_array[18] = 1
    game_over()

def press_light14():
    if light_array[14]:
        light14.config(image=LightOff)
        light_array[14] = 0
    else:
        light14.config(image=LightOn)
        light_array[14] = 1
    if light_array[9]:
        light9.config(image=LightOff)
        light_array[9] = 0
    else:
        light9.config(image=LightOn)
        light_array[9] = 1
    if light_array[13]:
        light13.config(image=LightOff)
        light_array[13] = 0
    else:
        light13.config(image=LightOn)
        light_array[13] = 1
    if light_array[19]:
        light19.config(image=LightOff)
        light_array[19] = 0
    else:
        light19.config(image=LightOn)
        light_array[19] = 1
    game_over()

def press_light15():
    if light_array[15]:
        light15.config(image=LightOff)
        light_array[15] = 0
    else:
        light15.config(image=LightOn)
        light_array[15] = 1
    if light_array[10]:
        light10.config(image=LightOff)
        light_array[10] = 0
    else:
        light10.config(image=LightOn)
        light_array[10] = 1
    if light_array[16]:
        light16.config(image=LightOff)
        light_array[16] = 0
    else:
        light16.config(image=LightOn)
        light_array[16] = 1
    if light_array[20]:
        light20.config(image=LightOff)
        light_array[20] = 0
    else:
        light20.config(image=LightOn)
        light_array[20] = 1
    game_over()

def press_light16():
    if light_array[16]:
        light16.config(image=LightOff)
        light_array[16] = 0
    else:
        light16.config(image=LightOn)
        light_array[16] = 1
    if light_array[11]:
        light11.config(image=LightOff)
        light_array[11] = 0
    else:
        light11.config(image=LightOn)
        light_array[11] = 1
    if light_array[15]:
        light15.config(image=LightOff)
        light_array[15] = 0
    else:
        light15.config(image=LightOn)
        light_array[15] = 1
    if light_array[17]:
        light17.config(image=LightOff)
        light_array[17] = 0
    else:
        light17.config(image=LightOn)
        light_array[17] = 1
    if light_array[21]:
        light21.config(image=LightOff)
        light_array[21] = 0
    else:
        light21.config(image=LightOn)
        light_array[21] = 1
    game_over()

def press_light17():
    if light_array[17]:
        light17.config(image=LightOff)
        light_array[17] = 0
    else:
        light17.config(image=LightOn)
        light_array[17] = 1
    if light_array[12]:
        light12.config(image=LightOff)
        light_array[12] = 0
    else:
        light12.config(image=LightOn)
        light_array[12] = 1
    if light_array[16]:
        light16.config(image=LightOff)
        light_array[16] = 0
    else:
        light16.config(image=LightOn)
        light_array[16] = 1
    if light_array[18]:
        light18.config(image=LightOff)
        light_array[18] = 0
    else:
        light18.config(image=LightOn)
        light_array[18] = 1
    if light_array[22]:
        light22.config(image=LightOff)
        light_array[22] = 0
    else:
        light22.config(image=LightOn)
        light_array[22] = 1
    game_over()

def press_light18():
    if light_array[18]:
        light18.config(image=LightOff)
        light_array[18] = 0
    else:
        light18.config(image=LightOn)
        light_array[18] = 1
    if light_array[13]:
        light13.config(image=LightOff)
        light_array[13] = 0
    else:
        light13.config(image=LightOn)
        light_array[13] = 1
    if light_array[17]:
        light17.config(image=LightOff)
        light_array[17] = 0
    else:
        light17.config(image=LightOn)
        light_array[17] = 1
    if light_array[19]:
        light19.config(image=LightOff)
        light_array[19] = 0
    else:
        light19.config(image=LightOn)
        light_array[19] = 1
    if light_array[23]:
        light23.config(image=LightOff)
        light_array[23] = 0
    else:
        light23.config(image=LightOn)
        light_array[23] = 1
    game_over()

def press_light19():
    if light_array[19]:
        light19.config(image=LightOff)
        light_array[19] = 0
    else:
        light19.config(image=LightOn)
        light_array[19] = 1
    if light_array[14]:
        light14.config(image=LightOff)
        light_array[14] = 0
    else:
        light14.config(image=LightOn)
        light_array[14] = 1
    if light_array[18]:
        light18.config(image=LightOff)
        light_array[18] = 0
    else:
        light18.config(image=LightOn)
        light_array[18] = 1
    if light_array[24]:
        light24.config(image=LightOff)
        light_array[24] = 0
    else:
        light24.config(image=LightOn)
        light_array[24] = 1
    game_over()

def press_light20():
    if light_array[20]:
        light20.config(image=LightOff)
        light_array[20] = 0
    else:
        light20.config(image=LightOn)
        light_array[20] = 1
    if light_array[15]:
        light15.config(image=LightOff)
        light_array[15] = 0
    else:
        light15.config(image=LightOn)
        light_array[15] = 1
    if light_array[21]:
        light21.config(image=LightOff)
        light_array[21] = 0
    else:
        light21.config(image=LightOn)
        light_array[21] = 1
    game_over()

def press_light21():
    if light_array[21]:
        light21.config(image=LightOff)
        light_array[21] = 0
    else:
        light21.config(image=LightOn)
        light_array[21] = 1
    if light_array[16]:
        light16.config(image=LightOff)
        light_array[16] = 0
    else:
        light16.config(image=LightOn)
        light_array[16] = 1
    if light_array[20]:
        light20.config(image=LightOff)
        light_array[20] = 0
    else:
        light20.config(image=LightOn)
        light_array[20] = 1
    if light_array[22]:
        light22.config(image=LightOff)
        light_array[22] = 0
    else:
        light22.config(image=LightOn)
        light_array[22] = 1
    game_over()

def press_light22():
    if light_array[22]:
        light22.config(image=LightOff)
        light_array[22] = 0
    else:
        light22.config(image=LightOn)
        light_array[22] = 1
    if light_array[17]:
        light17.config(image=LightOff)
        light_array[17] = 0
    else:
        light17.config(image=LightOn)
        light_array[17] = 1
    if light_array[21]:
        light21.config(image=LightOff)
        light_array[21] = 0
    else:
        light21.config(image=LightOn)
        light_array[21] = 1
    if light_array[23]:
        light23.config(image=LightOff)
        light_array[23] = 0
    else:
        light23.config(image=LightOn)
        light_array[23] = 1
    game_over()

def press_light23():
    if light_array[23]:
        light23.config(image=LightOff)
        light_array[23] = 0
    else:
        light23.config(image=LightOn)
        light_array[23] = 1
    if light_array[18]:
        light18.config(image=LightOff)
        light_array[18] = 0
    else:
        light18.config(image=LightOn)
        light_array[18] = 1
    if light_array[22]:
        light22.config(image=LightOff)
        light_array[22] = 0
    else:
        light22.config(image=LightOn)
        light_array[22] = 1
    if light_array[24]:
        light24.config(image=LightOff)
        light_array[24] = 0
    else:
        light24.config(image=LightOn)
        light_array[24] = 1
    game_over()

def press_light24():
    if light_array[24]:
        light24.config(image=LightOff)
        light_array[24] = 0
    else:
        light24.config(image=LightOn)
        light_array[24] = 1
    if light_array[19]:
        light19.config(image=LightOff)
        light_array[19] = 0
    else:
        light19.config(image=LightOn)
        light_array[19] = 1
    if light_array[23]:
        light23.config(image=LightOff)
        light_array[23] = 0
    else:
        light23.config(image=LightOn)
        light_array[23] = 1
    game_over()


root = tk.Tk()  #           (m)
root.title("Lights Out")  #  ū

#YouWin = tk.PhotoImage(file='LightsOutYouWin.png')
LightOn = tk.PhotoImage(file='LightOn.png')
LightOff = tk.PhotoImage(file='LightOff.png')

btn_frame = tk.Frame(root)
btn_frame.columnconfigure(0 , weight=1)
btn_frame.columnconfigure(1 , weight=1)
btn_frame.columnconfigure(2 , weight=1)
btn_frame.columnconfigure(3 , weight=1)
btn_frame.columnconfigure(4 , weight=1)
btn_frame.pack(fill='x')

light0 = tk.Button(btn_frame, image=LightOn, command=press_light0)
light0.grid(column=0, row=0)
light1 = tk.Button(btn_frame, image=LightOn, command=press_light1)
light1.grid(column=1, row=0)
light2 = tk.Button(btn_frame, image=LightOn, command=press_light2)
light2.grid(column=2, row=0)
light3 = tk.Button(btn_frame, image=LightOn, command=press_light3)
light3.grid(column=3, row=0)
light4 = tk.Button(btn_frame, image=LightOn, command=press_light4)
light4.grid(column=4, row=0)
light5 = tk.Button(btn_frame, image=LightOn, command=press_light5)
light5.grid(column=0, row=1)
light6 = tk.Button(btn_frame, image=LightOn, command=press_light6)
light6.grid(column=1, row=1)
light7 = tk.Button(btn_frame, image=LightOn, command=press_light7)
light7.grid(column=2, row=1)
light8 = tk.Button(btn_frame, image=LightOn, command=press_light8)
light8.grid(column=3, row=1)
light9 = tk.Button(btn_frame, image=LightOn, command=press_light9)
light9.grid(column=4, row=1)
light10 = tk.Button(btn_frame, image=LightOn, command=press_light10)
light10.grid(column=0, row=2)
light11 = tk.Button(btn_frame, image=LightOn, command=press_light11)
light11.grid(column=1, row=2)
light12 = tk.Button(btn_frame, image=LightOn, command=press_light12)
light12.grid(column=2, row=2)
light13 = tk.Button(btn_frame, image=LightOn, command=press_light13)
light13.grid(column=3, row=2)
light14 = tk.Button(btn_frame, image=LightOn, command=press_light14)
light14.grid(column=4, row=2)
light15 = tk.Button(btn_frame, image=LightOn, command=press_light15)
light15.grid(column=0, row=3)
light16 = tk.Button(btn_frame, image=LightOn, command=press_light16)
light16.grid(column=1, row=3)
light17 = tk.Button(btn_frame, image=LightOn, command=press_light17)
light17.grid(column=2, row=3)
light18 = tk.Button(btn_frame, image=LightOn, command=press_light18)
light18.grid(column=3, row=3)
light19 = tk.Button(btn_frame, image=LightOn, command=press_light19)
light19.grid(column=4, row=3)
light20 = tk.Button(btn_frame, image=LightOn, command=press_light20)
light20.grid(column=0, row=4)
light21 = tk.Button(btn_frame, image=LightOn, command=press_light21)
light21.grid(column=1, row=4)
light22 = tk.Button(btn_frame, image=LightOn, command=press_light22)
light22.grid(column=2, row=4)
light23 = tk.Button(btn_frame, image=LightOn, command=press_light23)
light23.grid(column=3, row=4)
light24 = tk.Button(btn_frame, image=LightOn, command=press_light24)
light24.grid(column=4, row=4)

restart = tk.Button(root, text="Restart", command=restart_btn)
restart.pack()
close = tk.Button(root, text="Quit", command=quit_btn)
close.pack()

root.mainloop()
