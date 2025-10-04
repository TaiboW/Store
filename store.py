print("Welcome to the store")
Fruits = ["apple", "banana", "orange", "cherry","peach"]
Price = [" 3$ each"," 2$ each"," 3.50$ each"," 1.25$ each"," 2.50$ each"]
print("You can buy:")
i = 0
for x in Fruits :
   print(i+1,Fruits[i],"-",Price[i])
   i += 1
print("If you buy:")
print("three items 10% off")
print("four items 20% off")
print("five items 30% off")
print("six or more items 50% off")
answer = int(input("Enter the fruit number you wanna buy:"))
a = []
a.append(answer)
buy_more = input("Do you want to buy more? yes or no:  ")
while buy_more == "yes" :
   answer = int(input("Enter the fruit number you wanna buy:"))
   a.append(answer)
   buy_more = input("Do you want to buy more? yes or no:  ")
print("This is your receipt:")
total = 0
for i in a :
    print(Fruits[i-1], "--", Price[i-1].split(" ")[1])
    total += float(Price[i-1].split(" ")[1].split("$")[0])
print("Total without discount:",total,"$")
nomb = len(a)
if nomb < 3:
   print("Total after discount:  ",total,"$")
elif nomb == 3:
   print("Total after discount:  ",total * 0.9,"$")
elif nomb == 4:
   print("Total after discount:  ",total * 0.8,"$")
elif nomb == 5:
   print("Total after discount:  ",total * 0.7,"$")
else:
   print("Total after discount:  ",total * 0.5,"$")
print("Thank you for coming!!!")
print("See you next time.")