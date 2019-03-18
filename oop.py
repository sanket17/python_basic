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
        DemoClass.__I