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



