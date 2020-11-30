from random import randint
import time
import json

class Fake_Data():
    def __init__(self, x=0,y=0,z=0,grid=[5000,5000]):
        self.coordinates= {
            "x" : x,
            "y" : y,
            "z" : z
        }
        
        self.grid = grid

        self.generate_fake_cordinates()


    def generate_fake_cordinates(self):
        self.coordinates['x'], self.coordinates['y'] = randint(0, self.grid[0] - 1), randint(0, self.grid[1]- 1)

    def move_animal_location(self):
        random = randint(1,10)

        if (random % 2) == 0:
            self.coordinates['x'], self.coordinates['y'] = randint(self.coordinates['x'] - 1,(self.coordinates['x'] +15) - 1), randint(self.coordinates['y'] - 1,(self.coordinates['y'] +15) - 1)
        else:
            self.coordinates['x'], self.coordinates['y'] = randint((self.coordinates['x']-15) - 1,(self.coordinates['x'] - 1)), randint((self.coordinates['y']-15) - 1,(self.coordinates['y'] - 1))

        self.save_data_to_json()
        

    def get_Coordinates(self):
        return self.coordinates
    
    def save_data_to_json(self):
        with open('data.json','w') as file:
            json.dump(self.coordinates,file)

def main():
    data = Fake_Data()
    while True:
        print("\nFake data at the moment:")
        print('X: {} Y:{} Z:{}'.format(data.coordinates['x'],data.coordinates['y'],data.coordinates['z']))
        time.sleep(5)
        data.move_animal_location()

if __name__ == "__main__":
    main()
        