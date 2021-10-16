# write a program to find largest number in list
list = [10,20,12,86,41,35]
max = list[0]
for number in list:
    if number > max:
      max = number
print(max)