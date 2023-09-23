#Loops

#for Loop
fruits = ["Apple", "Oranges", "Grapes"]

for fruit in fruits:
     print("Would you like some {}?".format(fruit))

#range

for number in range (1,11):
    print("Number: {}".format(number))

#while loop

temp_f = 40

while temp_f > 32:
    print("The water is {} degrees".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break

for x in range(1,11):
    if(x == 7):
        print("X is equal 7, so will be skipped")
        continue
    print("x equals {}".format(x))

for y in range(1,11):
    if(y == 3):
        pass
    else:
        print("y equals {}".format(y))