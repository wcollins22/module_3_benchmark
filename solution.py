from typing import List

class DogBoarder():
    def __init__(self, total_slots, daily_rate) -> None:
        self.total_slots = total_slots
        self.daily_rate = daily_rate
        self.dogs : List[str] = []


    def board(self, dog, breed, owner):
        if len(self.dogs) / 3 < self.total_slots:
            self.dogs.append(dog)
            self.dogs.append(breed)
            self.dogs.append(owner)
        else:
            raise ValueError

            
        
    def pick_up(self, dog, breed, owner, days):
        if dog[-1] != breed[-1]:
            raise ValueError
        elif dog in self.dogs and breed in self.dogs and owner in self.dogs:
            self.dogs.remove(dog)
            self.dogs.remove(breed)
            self.dogs.remove(owner)
        else:
            raise ValueError
        return days * self.daily_rate
        
        

    def is_full(self):
        if len(self.dogs) / 3 == self.total_slots:
            return True
        else:
            return False
        

    def slots_occupied(self):
        return len(self.dogs) / 3