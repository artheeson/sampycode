print(int(3.14))
print(int("10"))
print(int(3.99))

print(float("10"))

print(str(100))

print(list("abc")) 
print(list((1, 2, 3)))

print(tuple("abc"))

print(set((1, 2, 2, 3)))

print(bool("abcd"))
print(bool(""))

# for loop

product1 = ["cream", "chocolate"]
product2 = ["cake", "biscuit"]
for snack1 in product1:
    for snack2 in product2:
        print(snack1, snack2)

for i in range(5):
    print(i)
else:
    print("Loop finished!")   

# while loop

i = 1
while i <= 5:
    print(i)
    i += 1     

i = 2
while True:
    print(i)
    if i == 6:
        break
    i += 1

i = 3
while i < 10:
    i += 1
    if i == 6:
        continue
    print(i)