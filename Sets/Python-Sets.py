Set_Data={12,34,'ali',True}
print(Set_Data)
#adding an data to the  Set data type (for single items)
Set_Data.add(23)
print(Set_Data)
 #adding multiple values
Set_Data.update(['sd','sdsd',43])
print(Set_Data)
#finding the common set
Set_b={'21',33,True,'sd'}
New_common=Set_b & Set_Data
print(New_common)

New_common=Set_b ^ Set_Data
print(New_common)