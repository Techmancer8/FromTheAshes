def mod(stat):
    ret = -5
    for i in range(1,30,2):
        if stat <= i: return ret
        ret+=1
    return ret

backpacks={
    'Normal':4,
    'Survival':6
}
weapons={

}

class Char():
    def __init__(self,data):
        self.str,self.dex,self.fort,self.int,self.per,self.char=data['stats'].values()
        self.rations=data['Rations']
        self.speed=data['Speed']
        #self.prof=data['proficiency']
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
    def add(self,item,amount=1):
        #https://realpython.com/python-gui-tkinter/#getting-user-input-with-entry-widgets
        pass

data = {
    'Name':'Artyom',
    'stats':{
        'Strength':16,
        'Dexterity':18,
        'Fortitude':10,
        'Intelligence':12,
        'Perception':11,
        'Charm':7
    },
    'Speed':35,
    'Hit Points':{
        'Current':14,
        'Max':16,
        'Temp':3
    },
    'Class':'Scout (Alley Cat)',
    'Nationality':'American',
    'Armor Class':13,
    'Radiation Points':0.5,
    'Sanity':93,
    'Passive Perception':12,
    'Personality Traits':'Crazy? I was crazy once. They locked me in a room. A rubber room. A rubber room with rats. And rats make me crazy. Crazy? I was…',
    'Ideals':'Return to America',
    'Bonds':'Lampshade',
    'Traits':[
        'Way of the Scout',
        'Out of Sight',
        'Well-Balanced'
    ],
    'Gear':'Basic Winter Gear',
    'Hands':('',''),
    'Pockets':('Knife (4)','Rifle (1)'),
    'Invintory':['Dynomite','High-Caliber Bullets x3','',''],
    'Backpack':'Normal',
    'Rations':2
}


if __name__ == '__main__':
    import tkinter as tk
    window = tk.Tk()
    window.title(data['Name'])
    #greeting = tk.Label(text=str(Char(data)),foreground='white',background='black')#"Hello, Tkinter")
    #greeting.pack()

    console_frame = tk.Frame()
    name = tk.Label(master=console_frame,text='Console')
    name.pack()
    console = tk.Text()

    #Stats
    stats_frame = tk.Frame()
    stats_txt = tk.Label(master=stats_frame, text='Stats')
    stats_txt.pack()
    for name in data['stats']:
        val = data['stats'][name]
        button = tk.Button(master=stats_frame, text=f'{name}: {val}')
        button.pack()
    stats_frame.pack(side='left')

    '''#Invintory
    inv_frame = tk.Frame()
    #Hands
    hands = tk.Label(master=inv_frame, text='Hands')
    hand1 = tk.Entry(master=inv_frame)
    hand2 = tk.Entry(master=inv_frame)
    hand1.insert(0,data['Hands'][0])
    hand2.insert(0,data['Hands'][1])
    hands.pack()
    hand1.pack()
    hand2.pack()
    #Pockets
    pockets = tk.Label(master=inv_frame, text='Pockets')
    pocket1 = tk.Entry(master=inv_frame)
    pocket2 = tk.Entry(master=inv_frame)
    pocket1.insert(0,data['Pockets'][0])
    pocket2.insert(0,data['Pockets'][1])
    pockets.pack()
    pocket1.pack()
    pocket2.pack()
    #Backpack
    bp_txt = tk.Label(master=inv_frame, text='Backpack')
    bp_txt.pack()
    n = backpacks[data['Backpack']]
    for i in range(n):
        entry = tk.Entry()
        entry.insert(0,data['Invintory'][i])
        entry.pack()
    inv_frame.pack(side='right')
    '''
    
    
    console.pack(side='bottom')
    #>>> window.destroy()

    window.mainloop()
