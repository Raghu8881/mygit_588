class Duck:
    def sound(self):
        print("quack quack")
class Dog:
    def sound(self):
        print("howh howh")
class Cat:
    def sound(self):
        print("meow meow")
def All_sounds(obj):
    obj.sound()

x=Dog()
All_sounds(x)

x=5
x='puppy'
print(x)