number=[5,2,1,7,4]
print(number)
number.sort()
#.sort() to sort the list
#number.clear()
#.clear() to clear all the element of the lists
print (number.count(7))
#.count() takes an arg
#.count() function to count the element in the list
print(number)
print(7 in number)
#element in number will result in boolean value
number.append(0)
#.append() to add number in list
#.append()takes an arg
print(number)
number.reverse()
print(number)
numbers=number.copy()
#copy is used to copy the original content for future uses
number.pop(4)
#pop to delete element from list
#it take an arg for location
print(number)
print(numbers)