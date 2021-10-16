customer={
"name":"Sampat Lama",
"age":"20",
"religion":"buddhist",
}
customer["age"]=25
print(customer["age"])
print(customer.get("religion"))
print(customer.get("job","Student"))
