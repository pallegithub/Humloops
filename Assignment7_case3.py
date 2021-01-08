class Memory: 
    def __init__(self,internal, secondary, ram): 
        self.internal=internal
        self.secondary=secondary
        self.ram=ram 
    def getinfo(self): 
        print("Internal Memory :{} , Secondary Memory :{} and RAM :{}".format(self.internal,self.secondary,self.ram)) 
class Mobile: 
    def __init__(self,model, brand, price, memory): 
        self.model=model 
        self.brand=brand
        self.price=price
        self.memory=memory 
    def mobileinfo(self): 
        print("Mobile Model:",self.model) 
        print("Mobile Brand:",self.brand)
        print("Mobile Price:",self.price)
        print("Mobile Info:",end=" ") 
        self.memory.getinfo() 
print("")
c=Memory("2GB","1TB","32GB") 
e=Mobile('Note7',"Redmi","7000",c) 
e.mobileinfo()
print("")