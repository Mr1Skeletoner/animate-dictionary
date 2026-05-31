example_animation = 0: ("---¬   ",
                   "       ",
                   "       ",
                   "       "),

               1: ("---¬   ",
                   "   O   ",
                   "       ",
                   "       "),
               2: ("---¬   ",
                   "   O   ",
                   "   |   ",
                   "       "),
               3: ("---¬   ",
                   "   O   ",
                   "  /|   ",
                   "       "),
               4: ("---¬   ",
                   "   O   ",
                   "  /|\\  ",
                   "       "),
               5: ("---¬   ",
                   "   O   ",
                   "  /|\\  ",
                   "  /    "),
               6: ("---¬   ",
                   "   O   ",
                   "  /|\\  ",
                   "  / \\  ")

}

def animate(animation, delay):
    os.system('cls' if os.name == 'nt' else 'clear')
    for frame_place in animation:
        for frame in animation[frame_place]:
            print(frame)
        time.sleep(delay)
        os.system('cls' if os.name == 'nt' else 'clear')
