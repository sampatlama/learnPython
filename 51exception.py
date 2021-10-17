
try:
    age = int(input('Age: '))
    income=200000
    risk =income/age
    print(age)
except ZeroDivisionError:
                        print("Age can't be zero Value")
except ValueError:
                        print("Invalid input value")
