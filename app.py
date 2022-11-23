import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from urllib import request
from io import BytesIO
from random import randint
import requests
import PIL.Image
import json
from tkinter import *
from tkinter import ttk

root = tk.Tk()

root.title('Esprit de la foret')
root.geometry('805x485+0+0')

Destinations = {'Svweren' : 10,
                'Cabane du Marabout' : 15,
                'Domaine du Baron': 10,
                'Cabane de la Voyante': 15,
                'Cabana Coco': 10,
                '-----' : 0}

# Nature, Survival
players = {'Tom'    : [4, 1],
           'Samuel' : [0, -2],
           'Lucie'  : [-2, 5]}


def destination(input):

    with open('voyages.txt') as f:
        data = f.read()
    Voyages = json.loads(data)

    mean_player_stat = sum(sum(list(players.values()), [])) / len(sum(list(players.values()), []))
    if randint(0, 20) + mean_player_stat >=  Destinations[input] - Voyages[input]*2:
        Voyages[input] =  Voyages[input] + 1
        Destination['text'] = "Destination : " + input
    else:
        rnd = randint(0, len(Destinations)-2)
        Voyages[list(Destinations.keys())[rnd]] =  Voyages[list(Destinations.keys())[rnd]] + 1
        Destination['text'] = "Destination : " + list(Destinations.keys())[rnd]

    with open('voyages.txt', 'w') as convert_file:
     convert_file.write(json.dumps(Voyages))

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

ipadding = {'ipadx': 10, 'ipady': 10}

img_url = "https://ns328286.ip-37-187-113.eu/ew/wallpapers/800x480/02441_800x480.jpg"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(PIL.Image.open(BytesIO(img_data)))

tk.Label(root, image=img).place(x = 0, y = 0)

tk.Label(root, text="", bg='#101420').grid(column=1, row=0)

titre = tk.Label(root, text="BAGNA", fg='#101420', font= ('Helvetica 18 bold'))
titre.grid(column=1, row=1)

tk.Label(root, text="", bg='#101420').grid(column=1, row=2)

message = tk.Label(root, text="Ou souhaitez vous aller ?", fg='#101420', font= ('Helvetica 18 bold'))
message.grid(column=1, row=3)

tk.Label(root, text="", bg='#101420').grid(column=1, row=4)

Svweren = tk.Button(root, text='Svweren', fg='#101420', command=lambda: destination(Svweren['text']))
Svweren.grid(column=0, row=5)

Marabout = tk.Button(root, text='Cabane du Marabout', fg='#101420', command=lambda: destination(Marabout['text']))
Marabout.grid(column=1, row=5)

Baron = tk.Button(root, text='Domaine du Baron', fg='#101420', command=lambda: destination(Baron['text']))
Baron.grid(column=2, row=5)

tk.Label(root, text="", bg='#101420').grid(column=1, row=6)

Voyante = tk.Button(root, text='Cabane de la Voyante', fg='#101420', command=lambda: destination(Voyante['text']))
Voyante.grid(column=0, row=7)

Cabana = tk.Button(root, text='Cabana Coco', fg='#101420', command=lambda: destination(Cabana['text']))
Cabana.grid(column=1, row=7)

Autre = tk.Button(root, text='-----', fg='#101420', command=lambda: destination(Autre['text']))
Autre.grid(column=2, row=7)

tk.Label(root, text="", bg='#101420').grid(column=1, row=8)

Destination = tk.Label(root, text="Destination :", fg='#101420')
Destination.grid(column=1, row=9)

root.mainloop()
