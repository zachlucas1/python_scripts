#level 1 torch
first_answer = input('''You are walking through a dark part of town and find an old abandoned manor. You decide to do some exploration. 
You find three items at the front door: a TORCH, FLASHLIGHT, and a MACHETE. Which one do you want to pick up? ''').lower()
if first_answer == 'torch':
    second_answer = input('''You pick up the torch and light it. You walk in but a gust of wind blows your torch out. Do you want to LEAVE, 
or continue to EXPLORE in the dark? ''').lower()
    if second_answer == 'leave':
        third_answer = print('The dark is very scary. You leave the house, but you never find out what secrets are held within.')
        print('GAME OVER...')
    if second_answer == 'explore':
        third_answer = input('''You walk in completely blind, but fearless. You feel your way around and you hear something scratching to your left and it doesn't
sound too friendly. Would you like to FIGHT or RUN? ''').lower()
        if third_answer == 'fight':
            print('''You charge the beast but end up falling through the floor, crashing into the basement. The fall knocked you out making you prey to the beast
You don't make it home that night and become one of the ghouls to haunt the manor for eternity.''')
            print('GAME OVER...')
        if third_answer == 'run':
            print('You find a nearby window and you jump through it. You run home, scared for your life, but alive to tell the tale.')
            print('GAME OVER...')
            
#level 2 flashlight
elif first_answer == 'flashlight':
    second_answer = input('''You pick up the flashlight and turn it on. You see the inside of the house lit up in front of you. 
Do you want to go to the BASEMENT or the KITCHEN ''').lower()
    if second_answer == 'basement':
        third_answer = input('''You go down the creaking steps and it feels eerily cold. You reach the bottom of the steps and you notice the furnace is on, 
but the house is freezing. You also notice something moving in the corner. Do you want to investigate the FURNACE or the CORNER? ''').lower()
        if third_answer == 'furnace':
            fourth_answer = input('''You walk to the furnace and you finally feel warmth. You hear some sounds coming from the furnace that don't sound natural. 
Do you want to OPEN the furnace or investigate the CORNER? ''').lower()
            if fourth_answer == 'open':
                print('''You open and peer into the strange furnace. You see something that takes your breath away. You see a portal into another dimension.
A force is pulling you in, too strong to fight. You get sucked in and the portal to the world you know closes. The dimension is dark and 
dreary, similar to the world you were used to, but different. You are never found again and become a legend in the town.''')
                print('GAME OVER...')
        if third_answer == 'corner':
            fourth_answer = input('''You investigate the corner with your flashlight and you see something under a tarp moving around. You lift the tarp and find a 
dog and it is happy to see you. The dog begins to walk upstairs, do you FOLLOW it or continue to SEARCH the basement for clues? ''').lower()
            if fourth_answer == 'follow':
                fifth_answer = input('''You follow it, but the dog starts barking and snarling. It runs upstairs and you find it fighting a big furry beast. 
Do you HIT the beast with your flashlight or HIDE and let the dog do the work? ''').lower()
                if fifth_answer == 'hit':
                    print('''You hit the beast with your flashlight, knocking it out. You notice it's a werewolf! You take a picture, and call the police
to report your findings. You save the town by finding the elusive werewolf.''')
                print('GAME OVER...')
                if fifth_answer == 'hide':
                    print('''You hide while the dog and the beast fight. The beast is much larger and throws the dog. It approaches you and it's a werewolf!
He finds you and kills you.''')
                print('GAME OVER...')
            if fourth_answer == 'search':
                print(''''You search the basement, find nothing cool, and leave out a basement window. You hear some ruckus in the house, but don't think anything
of it. You walk home.''')
            print('GAME OVER...')
    if second_answer == 'corner':
        third_answer = input('''You investigate the corner with your flashlight and you see something under a tarp moving around. You lift the tarp and find a 
dog and it is happy to see you. The dog begins to walk upstairs, do you FOLLOW it or continue to SEARCH the basement for clues? ''').lower()
        if fourth_answer == 'follow':
                fifth_answer = input('''You follow it, but the dog starts barking and snarling. It runs upstairs and you find it fighting a big furry beast. 
Do you HIT the beast with your flashlight or HIDE and let the dog do the work?''').lower()
                if fifth_answer == 'hit':
                    print('''You hit the beast with your flashlight, knocking it out. You notice it's a werewolf! You take a picture, and call the police
to report your findings. You save the town by finding the elusive werewolf''')
                print('GAME OVER...')
                if fifth_answer == 'hide':
                    print('''You hide while the dog and the beast fight. The beast is much larger and throws the dog. It approaches you and it's a werewolf!
He finds you and kills you.''')
                print('GAME OVER...')
    if second_answer == 'search':
                print(''''You search the basement, find nothing cool, and leave out a basement window. You hear some ruckus in the house, but don't think anything
of it. You walk home.''')
                print('GAME OVER...')
    if second_answer == 'kitchen':
        third_answer = input('You enter the kitchen and notice a soup boiling. Do you TRY it or DONT try it?').lower()
        if third_answer == 'try':
            print('You try the soup and instantly you are poisoned and die.')
            print('GAME OVER...')
        if third_answer == 'dont':
            print('''You end up dying of hunger, I guess you'll never know what that soup tasted like.''')
            print('GAME OVER...')

#level 3 machete
elif first_answer == 'machete':
    second_answer = input('''You pick up the machete, but it's a little hard to see. But in the reflection of your blade you see the eye of a beast. Do you
FIGHT it or RUN away?''').lower()
    if second_answer == 'fight':
        print('''You take some swings at the beast and notice it's a werewolf! It almost overpowers you but you manage to defeat the werewolf! 
You take a picture, and call the police to report your findings. You save the town by finding the elusive werewolf''')
    print('GAME OVER...')
    if second_answer == 'run':
        print('You manage to run, but the beast is faster than you and defeats you. You are never found again and become a legend in the town.')
        print('GAME OVER...')   