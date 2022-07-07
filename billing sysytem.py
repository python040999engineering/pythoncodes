product = []
price =[]
total = 0
GST=0
size = int(input("enter list size \n"))

for i in range(size):
    i = str(input("enter food product\n"))
    product.append(i)
for i in range(size):
    i = int(input("enter food price\n"))
    price.append(i)



print("===================")
for i in range(size):

    print("{}. - {} {}".format(i+1,product[i],price[i]))
    total=total+price[i]
print("total=",total)
GST = total / 100 * 18
print("====================")
print("if you want to Add GST Press Y / N")
y = ("y")
n = ("n")
ans = input("")
if ans == n:
    print("total =", total)
else:
    GST = int(input("Enter GST%= "))
    GST_total = (total / 100) * 18
    print("totalbill =", total + GST)



