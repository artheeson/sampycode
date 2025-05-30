# list

cars=["BMW","AUDI","RR"]
print(cars[0])

cars[1]="BUGADI"
print(cars)

cars.append("TATA")
print(cars)

cars.insert(2,"KIA")
print(cars)

cars.remove("RR")
print(cars)

cars.pop(2)
print(cars)

for car in cars:
    print(car)

# slicing

name = "slicinginputhon"

print(name[1:5])

print(name[1:6:2])

print(name[:6])

print(name[2:]) 

print(name[::2])

print(name[::-1])

# tuple

T=(10,20,30,40,50,60)
T=(30,)
print(type(T))

for item in T:
    print(item)

t=(30,50,20,10,40)
asending=tuple(sorted(t))
print(asending)

desending=tuple(sorted(t,reverse=True))
print(desending)

# dictionary

person_data={"name":"artheeson","age":25,"place":"chennai"}

print(person_data)

print(person_data.get("age"))

person_data["age"]=26
print(person_data.get("age"))

person_data.pop("place")
print(person_data)

print(len(person_data))

if"name"in person_data:
    print("yes")
else:
    print("no")

# Exception handling

number=int(input("enter the number:"))
value=10/number
print(value)

try:
    number=int(input("enter the number:"))
    value=10/number
    print(value)
except ZeroDivisionError:
    print("cannot divided by zero")

try:
    number=int(input("enter value:"))
except ValueError:
    print("enter in number.")

try:
    value=input("enter value:")
    result = "5" + 2 
except TypeError:
    print("enter valid type operations.")

try:
    data = {"name": "Artheeson"}
    print(data["age"])
except KeyError:
    print("enter correct key.")

try:
    my_list = [10, 20, 30]
    print(my_list[1])
except IndexError:
    print("enter correct index value.")

try:
    with open("openfile.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("file not found,enter correct folder.")


finally:
    print("end")
