'=============полиморфизм это принцип в разных классах методы называютя'
'''одинаково но имеют разный вункционал другая логика реаизации кода
преимущества полиморфизма 
код не зависит от типов обьектов что делает его более гибким 
и пригодным для повторного использования
код становится более читаемым т к как методы с одинаковыми названиями выполняют логические 
похожие действия но с учетом специфики разных типов
'''
class Dog:
    def speak(self):
        print('gav')
class Cat:
    def speak(self):
        print('meow') 
class Fish:
    def speak(self):
        print('op op')        
object=[Dog(),Cat(),Fish()]
for obj in object:
    obj.speak()

class TelBook:
    def __init__(self,name,surname,phonenum):
        self.name=name
        self.surname=surname
        self.phonenum=phonenum
def get_info(self):
    print (f'контакт {self.name}, {self.surname} телефон {self.phonenum} ') 
bob = TelBook('Bob', 'Tyler', 5535456)  
get_info(bob)   

class PythonCourse:
    def __init__(self,opp):

        self.opp=opp
    def add(self):
        self.a[5]='abs'    
    def learn(self):
        pass
de= PythonCourse()

a={1:'opp',2:'inner',3:'poly',4:'enc'}
de.add(a)
print(dir(dict))


'============естественный полиморфизм '
'''оператор сложения +
num1=1
num2=2'''
num1=1
num2=2










