height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

print(type(height))
print(type(weight))

new_height = int(height)
new_weight = int(weight)

print(type(new_height))
print(type(new_weight))

BMI = print (int(new_height / (new_weight ** 2)))
