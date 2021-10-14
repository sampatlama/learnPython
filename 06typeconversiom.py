#str() => to convert into str
#int() => to convert into int
#float() => to convert into float
birth_year =input('Birth year? ')
age=2021 - int(birth_year)
sam=str(age)
print ('You are '+sam+' years old.')
print(type(sam))
print(type(age))
print(type(birth_year))