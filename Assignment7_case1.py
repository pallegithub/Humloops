class Car: 
    def __init__(self,model,brand,color): 
        self.model=model
        self.brand=brand 
        self.color=color
    def start(self):
        print("Car Started")
    def move(self):
        print("Car is Moving")
    def stop(self):
        print("Car stopped")
class BMW(Car): 
    def __init__(self,model,brand,color): 
        super().__init__(model,brand,color) 
    def autoPilot(self):
        print("Car is autopilot")
    def autoGear(self):
        print("Car having autoGear system")
    def BMWInfo(self): 
        print("Car Model    :",self.model) 
        print("Car Brand    :",self.brand) 
        print("Car Color    :",self.color) 
print("")
d=BMW('BMW X5',"BMW","Black")
print("")
d.BMWInfo()
d.start()
d.move() 
d.stop() 
d.autoPilot()
d.autoGear()
print()