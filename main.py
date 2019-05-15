import tkinter as tk
import tkinter.ttk as ttk
import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

POKEMON = [
    "Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie",
    "Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate",
    "Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran♀","Nidorina",
    "Nidoqueen","Nidoran♂","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff",
    "Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett",
    "Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag",
    "Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell",
    "Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro",
    "Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder",
    "Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb",
    "Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing",
    "Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu",
    "Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados",
    "Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto",
    "Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"
]

class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Pokemon")
        self.resizable(False, False)

        fileselectframe = tk.Frame(self)
        fileselectframe.grid(row=0, column=0, columnspan=3, sticky="we")
        fileselectframe.columnconfigure(0, weight=2)
        self.poke_rom = tk.StringVar(fileselectframe, value="")
        self.file_selector = tk.Entry(fileselectframe, textvariable=self.poke_rom)
        self.file_button = tk.Button(fileselectframe, text="Select ROM", command=lambda:self.getROM())

        self.poke_one = tk.StringVar(self)
        self.poke_two = tk.StringVar(self)
        self.poke_three = tk.StringVar(self)
        self.poke_one.set(POKEMON[0])
        self.poke_two.set(POKEMON[6])
        self.poke_three.set(POKEMON[3])
        self.l1 = tk.Label(self, text="Pokeball 1")
        self.l2 = tk.Label(self, text="Pokeball 2")
        self.l3 = tk.Label(self, text="Pokeball 3")
        self.ball_one = ttk.Combobox(self, values=POKEMON, textvariable=self.poke_one, state='readonly')
        self.ball_two = ttk.Combobox(self, values=POKEMON, textvariable=self.poke_two, state='readonly')
        self.ball_three = ttk.Combobox(self, values=POKEMON, textvariable=self.poke_three, state='readonly')

        self.columnconfigure(0, minsize=200)
        self.columnconfigure(1, minsize=200)
        self.columnconfigure(2, minsize=200)

        self.file_selector.grid(row=0, column=0, padx=5, pady=5, sticky="we")
        self.file_button.grid(row=0, column=2, padx=5, pady=5)
        self.l1.grid(row=1, column=0, padx=5)
        self.l2.grid(row=1, column=1, padx=5)
        self.l3.grid(row=1, column=2, padx=5)
        self.ball_three.grid(row=2, column=2, padx=5, pady=1, sticky="we")
        self.ball_two.grid(row=2, column=1, padx=5, pady=1, sticky="we")
        self.ball_one.grid(row=2, column=0, padx=5, pady=1, sticky="we")

        def ok():
            confirm = messagebox.askokcancel("Confirm", "The following operation will alter the ROM's memory. Please create a backup copy of your ROM. If you wish to continue, select OK.")
            if confirm is True:
                poke1 = POKEMON.index(self.poke_one.get()) + 1
                poke2 = POKEMON.index(self.poke_two.get()) + 1
                poke3 = POKEMON.index(self.poke_three.get()) + 1
                self.applyChanges([poke1, poke2, poke3])

        self.button = tk.Button(self, text="OK", command=ok, width=5)
        self.button.grid(row=3, column=1, padx=5, pady=5)

    def run(self):
        self.mainloop()

    def getROM(self):
        file = filedialog.askopenfilename(initialdir="C:\\", filetypes=[('GBA ROMS', '*.GBA')])
        self.file_selector.delete(0,END)
        self.file_selector.insert(0,file)

    def applyChanges(self, pokemon):
        offsets = [0x169BB5, 0x169D82, 0x169DB8]
        with open(self.poke_rom.get(), 'r+b') as f:
            for i in range(0, 3):
                f.seek(offsets[i])
                f.write(bytes([pokemon[i]]))

if __name__ == '__main__':
    MainApp().run()
