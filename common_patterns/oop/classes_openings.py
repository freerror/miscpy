class Opening:
    def __init__(self, name, open_state):
        self.name = name
        self.open_state = open_state
    
    def myfunc(self):
        print("The opening, {0}, was {1:.0%} open.".format(self.name, self.open_state))

class Hatch(Opening):
    def __init__(self, name, open_state, damage_level):
        self.damage_level = damage_level
        super().__init__(name, open_state)
    
    def myfunc(self):
        super().myfunc()
        print(f"{self.name} is a hatch, and is {self.damage_level:.0%} damaged.")

def main():
    o1 = Opening("Hallway_1", 0.5)
    o2 = Opening("Hallway_2", 0.2)
    o3 = Opening("Hallway_3", 0.7)
    h1 = Hatch("Bubble_1", 0.9, 0.2)
    openings = (o1, o2, o3, h1)
    for opening in openings:
        opening.myfunc()

if __name__ == '__main__':
    main()