#wap where you check the length of name and comment accordingly
'''
i.e
for name < 5 => Name mustbe at least 5 characters long
for name < 10 => Name must be Maximum 10 characters
otherwise
name looks good
'''
lname=input('what is your name? ')
name=len(lname)
if name < 5:
    print("Name must be at least 5 characters")
elif name > 10:
    print("Name must be maximum of 10 characters")
else:
    print("Name Looks good")
                        
