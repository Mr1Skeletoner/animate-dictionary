you make each individual frames in a dictionary like this: 

animation = {0: ("FRAMES GO HERE",
                             "FRAMES GO HERE",
                             "FRAMES GO HERE"),
                        1: ("FRAMES GO HERE",
                             "FRAMES GO HERE",
                             "FRAMES GO HERE"),
                        2: ("FRAMES GO HERE",
                             "FRAMES GO HERE",
                             "FRAMES GO HERE"),

call the function, animate(animation,delay)

try different delay times until one is good

for the example animation in the code (hangman), i think 0.5 seconds is good
