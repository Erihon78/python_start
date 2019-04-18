class Things:
    pass

class Animate(Things):
    def walking_around(self):
        print('Walking around')
# Animals is class
class Animals(Animate):
    def breathe(self):
        print('Breathe!')
    def move(self):
        print('Move!')
    def eat_food(self):
        self.walking_around()
        print('Eat food!')
    
class Giraffes:
    def __init__(self, spots):
        self.giraffe_spots = spots

ozwald = Giraffes(50)

print(ozwald.giraffe_spots)

# Giraffe is object
giraffe = Animals()
# breathe() is functionaly method in Animals class
giraffe.eat_food()

giraffe.walking_around()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is %s and by age is %s" % (self.name, self.age))

p1 = Person("Oleg", 25)
p1.myfunc()