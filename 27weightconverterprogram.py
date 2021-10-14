#Weight Converter
weight = input('Weight: ')
weight_type = input('(L)bs or (K)g: ')
kgs=float(weight)*0.453592
pounds=float(weight)*2.20462
if weight_type.upper() == "K":
    print(f"You are {pounds} pounds")
elif weight_type.upper() == "L":
    print(f"You are {kgs} Kg")
else:
    print("Please,Enter correct letter")