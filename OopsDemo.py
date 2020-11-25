#class is a user defined blueprint or prototype,

#for e.g to develop a calculator-multiples operators is needed(sum,divison,multiplication). all these functions are defined in class.

class calculator:
    num = 100 #class variable

    #default constructor
    # self keyword is mandatory for calling variable names into method

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print("i am called automatically when object is created")

    def getData(self):
        print("i am now executing as method in class")
    def summation(self):
        return  self.firstnumber + self.secondnumber + calculator.num

obj = calculator(2, 3)
obj.getData()
print(obj.num)
print(obj.summation())

obj = calculator(7, 9)
obj.getData()
print(obj.num)
print(obj.summation())