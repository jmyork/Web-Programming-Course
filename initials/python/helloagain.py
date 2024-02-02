class Fligth:
    def __init__(self,capacity,passengers=[]) -> None:
        self.capacity=capacity
        self.passengers=passengers
        
    def add_passenger(self,name):
        if(self.capacity <= len(self.passengers)):
            print(f"there is no more open seats to :{name}")
            return False
        else:
            self.passengers.append(name)
            return True
            
    def open_seats(self):
        return self.capacity-len(self.passengers)
    def get_passengers(self):
        return self.passengers
    def flight_infos():
        return {
            'name':"881",
            'origin':'South Korea',
            'destiny':'Angola',
            'pilotsPreference':["burguer",'american burger','humburgo','alaska','russia','nuk soap']
        }

        

myFligth= Fligth(4)
myFligth.add_passenger("bene")
myFligth.add_passenger("ivo")
myFligth.add_passenger("ig")

print(Fligth.flight_infos())
print(f"There is :{myFligth.open_seats()} open seat(s)")
print(f'Those are the passengers:{myFligth.get_passengers()}')