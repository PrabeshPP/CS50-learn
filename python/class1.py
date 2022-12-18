class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]
    
    def add_passemger(self,name):
        if(self.checkIfSeatAvailable()):
            print("Seats not available")
        else:
            self.passengers.append(name)
    
    def checkIfSeatAvailable(self):
        if(self.capacity==len(self.passengers)):
            return True
        else:
            return False