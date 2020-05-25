from tkinter import *
from tkinter import messagebox
ispvp = False
game_continue = True
match_count = 21
pc_turn = 0
player_count = 1
root = Tk()
messagebox.showinfo("Rules","Each player can pick (0-5) matchsticks. \n One who has to pick the last one, loses.")


# Configuring window
root.title("MatchStick Trouble")
root.resizable(width=False, height=False)
root.geometry("800x641")
root.iconbitmap('sources\icon_Oqc_icon.ico')


# Setting background
backgroundimage = PhotoImage(file=r"sources\bg1.png")
background_label = Label(root, image=backgroundimage)
background_label.pack()


# Main menu functions
def hidepcbutton():
    locx, locy = vsPC_button.winfo_x(), vsPC_button.winfo_y()
    vsPC_button.place(x=-locx, y=-locy)


def vspcfun():
    print("Vs PC")

#VS PC mode
def callbothpc():
    toggle_menu()
    hideplayerbutton()
    hidepcbutton()
    vspcfun()
    toggle_entry()

#Hides versus player button
def hideplayerbutton():
    locx, locy = vsPlayer_button.winfo_x(), vsPC_button.winfo_y()
    vsPlayer_button.place(x=-locx, y=-locy)


def vsplayerfun():
    print("Vs player")

#Launches 2 player mode
def callbothplayer():
    global ispvp
    ispvp = True
    toggle_menu()
    hidepcbutton()
    hideplayerbutton()
    vsplayerfun()
    toggle_entry()
    toggle_player_text()

#Entry box toggle
def toggle_entry():
    locx, locy = entryfield1.winfo_x(), entryfield1.winfo_y()
    entryfield1.place(x=-locx, y=-locy)
    entryheading.place(x=-locx, y=(-locy)-20)
    submit_button.place(x=-submit_button.winfo_x(), y=-submit_button.winfo_y())
    toggle_match_count()
    toggle_pc_picked_count_label()

#PC picked x matchsticks toggle
def toggle_pc_picked_count_label():
    locx, locy = pc_picked_count_label.winfo_x(), pc_picked_count_label.winfo_y()
    pc_picked_count_label.place(x=-locx, y=-locy)

#Remaining match count toggle
def toggle_match_count():
    locx, locy = match_count_label.winfo_x(), match_count_label.winfo_y()
    match_count_label.place(x=-locx, y=-locy)

#Label denoting Player 1
def toggle_player_text():
    locx, locy = player_one_label.winfo_x(), player_one_label.winfo_y()
    player_one_label.place(x=-locx, y=-locy)

#Label denoting PLayer 2
def toggle_player2_text():
    locx, locy = player_two_label.winfo_x(), player_two_label.winfo_y()
    player_two_label.place(x=-locx, y=-locy)


#Taking input from the user.
def submit_called():
    global player_count, match_count
    entered = int(entryfield1.get())
    if entered < 0 or entered > 5 or match_count - entered <= 0:
        pc_picked_count_label.config(text="Invalid Entry!")
        return
    if ispvp:
        pc_picked_count_label.config(text="")
    if ispvp:
        vs_player_reduce_count(entryfield1.get())
        player_count = player_count + 1
        if game_continue:
            toggle_player_text()
            toggle_player2_text()
    else:
        vs_pc_reduce_count(entryfield1.get())

# Single player reduce matchstick count
def vs_pc_reduce_count(string_value):
    print(string_value)
    global match_count, pc_turn

    num = int(string_value)
    if match_count == 6 and num == 5:
        match_count_label.config(text="You won :)")
        pc_picked_count_label.config(text="I have to pick the last MatchStick")
        return

    pc_turn = 5 - num
    match_count = match_count - (num + pc_turn)
    print(match_count)
    if match_count == 1:
        match_count_label.config(text="You Lost :(")
        return
    match_count_label.config(text="No of MatchSticks left: %s" % match_count)
    entryfield1.delete(0, 'end')
    pc_picked_count_label.config(text="I picked %s MatchSticks" % pc_turn)


#2 Player mode reduce matchStick count
def vs_player_reduce_count(entry):
    global match_count, player_count, game_continue
    num = int(entry)
    match_count = match_count - num
    match_count_label.config(text="No of MatchSticks left: %s" % match_count)
    entryfield1.delete(0, 'end')
    if match_count == 1:
        game_continue = False
        if player_count % 2 == 0:
            pc_picked_count_label.config(text="Player 1 has to pick the last MatchStick")
            match_count_label.config(text="Player 2 Wins")
            return
        else:
            pc_picked_count_label.config(text="Player 2 has to pick the last MatchStick")
            match_count_label.config(text="Player 1 Wins")
            return

#Exits the game
def killprocess():
    root.destroy()

#Funciton to make menu button visible
def toggle_menu():
    locx, locy = menu_button.winfo_x(), menu_button.winfo_y()
    menu_button.place(x=locx+180, y=locy+180)


#function to hide the menu button
def hide_menu():
    locx, locy = menu_button.winfo_x(), menu_button.winfo_y()
    menu_button.place(x=locx-180, y=locy-180)


#Menu click button action
def menu_clicked():
    reset_entries()
    hide_menu()
    hidepcbutton()
    hideplayerbutton()
    toggle_entry()
    if player_one_label.winfo_x() > 0:
        toggle_player_text()
    if player_two_label.winfo_x() > 0:
        toggle_player2_text()


#resetting entries
def reset_entries():
    global ispvp, match_count, game_continue
    game_continue = True
    match_count = 21
    ispvp = False
    pc_picked_count_label.config(text="")
    entryfield1.delete(0, 'end')
    match_count_label.config(text="No of MatchSticks left: %s" % match_count)


# Versus Buttons
vsPC = PhotoImage(file=r"sources\vspc.png")
vsPC_button = Button(root, image=vsPC, command=callbothpc)
vsPC_button.place(x=30, y=220)

vsPlayer = PhotoImage(file=r"sources\vsplayer.png")
vsPlayer_button = Button(root, image=vsPlayer, command=callbothplayer)
vsPlayer_button.place(x=600, y=220)


# Entry field
entryheading = Label(root, text="Pick MatchStick (0-5)", bg="#3a1e20", foreground="white")
entryheading.place(x=-320, y=-240)
entryfield1 = Entry(root, width=30)
entryfield1.place(x=-320, y=-250)

# Player heading
player_one_label = Label(root, text="Player 1", bg="#3a1e20", foreground="white")
player_one_label.place(x=-320, y=-210)

player_two_label = Label(root, text="Player 2", bg="#3a1e20", foreground="white")
player_two_label.place(x=-320, y=-210)


# Submit button
submit_button = Button(root, text="Submit", bg="#3a1e20", foreground="white", command=lambda: submit_called())
submit_button.place(x=-380, y=-275)


# Menu button
menu_button = Button(root, text="Menu", bg="#3a1e20", foreground="white", command=menu_clicked)
menu_button.place(x=-140, y=-140)
menu_button.config(font=("Copperplate Gothic Bold", 24))


# Exit button
exit_button = Button(root, text="Exit", bg="#0e021d", foreground="white", font=("Copperplate Gothic Bold Regular", 24))
exit_button.config(command=killprocess)
exit_button.place(x=650, y=40)


# Print MatchStick Count
match_count_label = Label(root, text="No of MatchSticks left: %s" % match_count)
match_count_label.config(bg="#371b21", foreground="white")
match_count_label.place(x=-320, y=-325)


# PC picked Count
pc_picked_count_label = Label(root)
pc_picked_count_label.place(x=-320, y=-305)
pc_picked_count_label.config(bg="#3e2021", foreground="white")

root.mainloop()
