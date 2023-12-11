"""
Compulsory Task 1: 
------------------

Use the code provided copied to a new file named compulsory_task_1.py: 
1. Add another method in the Course class that prints the head office location: Woodstock, Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

On a side note, this task covers single inheritance. multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course
"""
print('Hello There, Are you interested in the following content?\nWell there is a book that can assist you in obtaining the sufficient Knowlege about Computer Science and its applications\n')
class Course:
  name = "Fundamentals of Computer Science"
  contact_website = "www.hyperiondev.com"
  head_office = 'Woodstock, Cape Town'
  
  

  def contact_details(self):
      print("Please contact us by visiting\t", self.contact_website)
  
  def location(self):
    print('Our Head Office is situated at:\t', self.head_office)

class OOPCourse(Course):
  def __init__(self, description, trainer):
    #constructor of parent class
    super().__init__() 
    self.description = description
    self.trainer = trainer

  def trainer_details(self):
    print(f'The following course is about {self.description} and the trainer is {self.trainer}')
    
  def __str__(self):
    return f'The Name of the book is \t{self.name}'
  def show_course_id(self):
    print('The Item is catalogued as:\n232243:\t', self.name)
course_1 = OOPCourse('OOP Fundamentals', 'Mr Anon A. Mouse')

course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
course_1.location()

print(course_1)
