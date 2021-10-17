from Exercise import *
i = 1
list = []
while i <= 5:
    n = int(input("Enter elements: "))
    list.append(n)
    i += 1
max=max(list)
print(f'The max element is {max}')