#class with __init_ method
class Login:
    def __init__(self,UserName,Password):
        self.UserName=UserName
        self.Password=Password
    
    def DisplayLogin(self):
        print(self.UserName)
        print(self.Password)

login_1=Login('ali','hamza')
login_1.DisplayLogin()

#class __str__ methodes

class Peron:
    def __init__(self,Name):
        self.Name=Name
    def __str__(self):
        return f"{(self.Name)}"

Man=Peron("Hamza")
print(Man.__str__)


#super function is used in python to call the __init__ function of the Super class 


    

        

    