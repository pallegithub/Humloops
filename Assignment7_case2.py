class TV: 
    def __init__(self,model,brand): 
        self.model=model
        self.brand=brand 
    def features(self):
        print("Color TV with remote control")
class SmartTV(TV): 
    def __init__(self,model,brand,screenSize,price,resolution): 
        super().__init__(model,brand)
        self.screenSize=screenSize
        self.price=price 
        self.resolution=resolution
    def newFeatures(self):
        print("WiFi facility, LED Display, CPU interface etc...")
    def TVInfo(self): 
        print("TV Model     :",self.model) 
        print("TV Brand     :",self.brand) 
        print("TV screenSize:",self.screenSize)
        print("TV price     :",self.price) 
        print("TV resolution :",self.resolution)  
print("")
d=SmartTV("43FIF","ONIDA","43","23149","4K")
print("TV Features")
d.features()
print("SmartTV Features")
d.newFeatures()
d.TVInfo()
print("")
