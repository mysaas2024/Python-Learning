Logon_Info={
    "username":'asasfd',
    "password":'eefefef'
}
print(Logon_Info)

#accesssing using Key
print(Logon_Info['password'])

#for safe accessing the passwaord we use 
print(Logon_Info.get("username","unknown"))

#Experimenting other functions
print(Logon_Info.keys())

#updating the values

Logon_Info["username"]=True
print(Logon_Info)

#updating in bulk
Logon_Info.update({
    'password':'ali'
})
print(Logon_Info)


#removing thr items for the dictionaries
Logon_Info.pop("password")
print(Logon_Info)

#other functions for for dictionaries
#print the iteams
print(Logon_Info.items())
#print keys
print(Logon_Info.keys())
#print values
print(Logon_Info.values())