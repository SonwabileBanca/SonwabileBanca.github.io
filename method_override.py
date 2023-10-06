print(
    '======Welcome to the Space Force Academy=======\nCan you please Answer the following:\n\n'
)


# My adult class as a blueprint
class Adult:
  # my four argument are inserted in the constuctor

  def __init__(self, name, age, eye_colour, hair_colour):
    self.name = name
    self.age = age
    self.eye_colour = eye_colour
    self.hair_colour = hair_colour

  def can_drive(self):

    # If statement checking whether the input is old enough
    if self.age >= 18:
      return f'Congratulations, {self.name}, you are old enough to drive.'
    else:
      return f'Sorry, {self.name}, you are too young to drive.'


class Child(Adult):

  def __init__(self, name, age, eye_colour, hair_colour):
    super().__init__(name, age, eye_colour, hair_colour)


name = input('Enter your name: ')
# age variable as an integer
age = int(input('Enter your age: '))
eye_colour = input('Enter the color of your eyes: ')
hair_colour = input('Enter the color of your hair: ')

person1 = Adult(name, age, eye_colour, hair_colour)
result = person1.can_drive()
print(result)
# All of the object instances an instance
offspring1 = Child('Luke Skywalker', 12, 'Blue', 'Blonde')
output = offspring1.can_drive()
print(output)