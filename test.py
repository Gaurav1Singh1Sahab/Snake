class Animal():
    def __init__(self):
        self.num_eyes = 2
        self.nose = 1

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater !!!")


    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.breathe()
nemo.swim()
print(nemo.nose)