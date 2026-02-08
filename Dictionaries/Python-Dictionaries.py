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
