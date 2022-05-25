from pynput import keyboard
import os
import time
import random
points = 0
wholegame = [
    [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
    [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
    [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
    [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
    [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
    [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
    [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
]
apple = [random.randint(0, len(wholegame)-1),
         random.randint(0, len(wholegame[0])-1)]
pos = [1, 2]


wholegame[pos[0]][pos[1]] = " 🧍 "
wholegame[apple[0]][apple[1]] = " 🍎 "

while True:
    for i in range(len(wholegame)):
        wholegame[pos[0]][pos[1]] = " 🧍 "
        wholegame[apple[0]][apple[1]] = " 🍎 "
        os.system("clear")
        print("snake without a tail lmao")
        print("and you have to move yourslef")
        print("and its infinitely shittier than the snake game")
        for i in range(len(wholegame)):
            print(str("".join(wholegame[i])))
        print("pos: " + str(pos))
        print("apple: " + str(apple))
        print("points: " + str(points))
        time.sleep(.3)
        with keyboard.Events() as events:
            event = events.get(1e6)
            if event.key == keyboard.KeyCode.from_char('w'):
                pos[0] -= 1
            elif event.key == keyboard.KeyCode.from_char('s'):
                pos[0] += 1
            elif event.key == keyboard.KeyCode.from_char('a'):
                pos[1] -= 1
            elif event.key == keyboard.KeyCode.from_char('d'):
                pos[1] += 1
            else:
                move = None
        wholegame = [
            [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
            [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
            [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
            [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
            [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
            [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
            [" 🄰 ", " 🄼 ", " 🄾 ", " 🄽 ", " 🄶 ", " 🅄 ", " 🅂 "],
        ]

        if pos[0] < 0:
            pos[0] = 0
        if pos[0] > len(wholegame)-1:
            pos[0] = len(wholegame)-1
        if pos[1] < 0:
            pos[1] = 0
        if pos[1] > len(wholegame[0])-1:
            pos[1] = len(wholegame[0])-1

        wholegame[pos[0]][pos[1]] = " 🧍 "
        wholegame[apple[0]][apple[1]] = " 🍎 "
        if apple == pos:
            points += 1
            apple = [random.randint(0, len(wholegame)-1),
                     random.randint(0, len(wholegame[0])-1)]
            os.system("clear")
            print(
                "CONGRATS YOU GOT AN APPLE!!11111 HOLY SHIT!!11111 \nI CAN NEVER GET AN APPLE!111!1111")
            time.sleep(3)
