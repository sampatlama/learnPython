from Calc import *      
try:
                        a=int(input("Enter a: "))
                        b=int(input("Enter b: "))
                        sum(a,b)
                        print(f'The sum is {sum(a,b)}')
                        print(f'The difference is {subtract(a,b)}')
                        print(f'The multiple is {multiply(a,b)}')
                        print(f'The division is {divide(a,b)}')

except:
                        print('Input error')