class animal():
    def __init__(self,name,type):
        self.name = name
        self.type =type
    def breed(self):
        print("cho tôi ăn,cho tôi ăn!")
class dog(animal):
    def __init__ (self,name,type,sound):
        super().__init__(name,type)
        self.sound = sound
    def breed(self):
        print("gâu gâu")
class cat(animal):
    def __init__(self,name,type):
        super().__init__(name,type)

dog_1 = dog("Corgi","chó cảnh","ẳn")
print(f"đây là {dog_1.name} thuộc loại {dog_1.type}")