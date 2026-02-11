def Main(func):
    def Login():
        print('Intiating Login')
        func()
        print('Logic Success')
        return Login()
    

@Main
def Login():
    print("Login Done")

Main('hello')
#dacorator function is a function that is ueed for making a a funtion is another function 
#such that fucntion inside the funciton executes than the fucnton of the man thing executes
#mainly used in middlewares 



