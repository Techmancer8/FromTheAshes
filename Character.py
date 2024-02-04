from Game import *
from json import load,dump
import tkinter as tk

class Char():
    def __init__(self,data):
        #self.str,self.dex,self.fort,self.int,self.per,self.char
        self.stats=data['stats']#.values()
        self.rations=data['Rations']
        self.speed=data['Speed']
        self.profstat,self.prof=data['Proficiency']
        #self.ac
        self.hp=data['Hit Points']
        #self.init=data['Initiative']
        self.name=data['Name']
    def __str__(self):
        return f'''
{self.name}:
    Stats:
        Strength: {self.str}
        Dexterity: {self.dex}
        Fortitude: {self.fort}
        Intelligence: {self.int}
        Perception: {self.per}
        Charm: {self.char}
'''
    def console_roll(self,name:str):
        stat = self.stats[name]
        dice = roll(20)
        modif = mod(stat)
        total = dice+modif
        if dice == 20: dice = 'NAT 20!'
        outstr = f'\n{name}: {dice} + {modif} '
        if self.profstat == name:
            outstr += f'+ {self.prof}'
            total += self.prof
        
        return f'{outstr} = {str(total)}'

data = load(open('./Artyom.json'))
PC = Char(data)
window = tk.Tk()
window.title(PC.name)
console_frame = tk.Frame()
console = tk.Text()
name = tk.Label(master=console_frame,text='Console')
name.pack()

#Title
character_frame = tk.Frame()
name = tk.Label(master=character_frame,text='Name: '+PC.name)#font=
name.pack(side='left')
#quitbutton = tk.Button(master=character_frame, text='Quit',command=window.destroy())
#quitbutton.pack(side='right')
character_frame.pack(side='top')

#Stats

stats_frame = tk.Frame()
stats_txt = tk.Label(master=stats_frame, text='Stats')
stats_txt.pack()
statbtn=list()
for stat in PC.stats:
    statbtn.append(tk.Button(master=stats_frame, text=stat+': '+str(PC.stats[stat]),command=lambda i=stat:console.insert(tk.END,PC.console_roll(i))))
    console.insert(tk.END,'Loading '+stat+'\n')
    
for i in statbtn:i.pack()

stats_frame.pack(side='left')    

console.pack(side='bottom')
#>>> 

window.mainloop()
