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

data = {}

if __name__ == '__main__':
    import tkinter as tk
    window = tk.Tk()
    window.title(data['Name'])

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
    
    console.pack(side='bottom')
    #>>> window.destroy()

    window.mainloop()
