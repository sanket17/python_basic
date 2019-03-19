class DemoClass():
  # Class Object attribute
    desg = 'Mr.'
    def __init__(self, name):
        self.name = name
    
    def show_name(self):
        print(DemoClass.desg+ '' +self.name)


demoObj = DemoClass('SAnket')
demoObj.show_name()

#Inheritance
#base class - DemoClass
class ProgClass(DemoClass):
    def __init__(self, lang):
        DemoClass.__init__(self, name='Sanket')
        self.lang = lang

    def show_info(self):
        DemoClass.show_name(self)
        print(f'Likes {self.lang}')

stud = ProgClass('C++')
stud.show_info()
stud.show_name()

# magic or dunder method

my_list = [1,3,4,5]
print(len(my_list))

print(f'Printing Prog class {stud}')

class DangerMethodDemo():

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'My name is '+self.name
    
    def __len__(self):
        return 10
    
    def __del__(self):
        print('This statement is printed before deletion of object')


danger_obj = DangerMethodDemo('Sanket')
print(danger_obj)
print(len(danger_obj))
del danger_obj