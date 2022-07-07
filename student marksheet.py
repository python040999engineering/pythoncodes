Name=input("enter student name : ")
Number=int(input("enter Roll number : "))
sub1=int(input("enter JAVA marks : "))
sub2=int(input("enter C marks : "))
sub3=int(input("enter python marks : "))
sub4=int(input("enter JSP marks : "))
sub5=int(input("enter Go marks : "))
Total=(sub1 + sub2 + sub3 + sub4 + sub5)
Per=(Total*100/500)
print("======================")
print("Name=",Name)
print("roll Number=", Number)
print("java=",sub1 ,"/100")
print("C=",sub2 ,"/100")
print("python=",sub3 ,"/100")
print("JSP=",sub4 ,"/100")
print("Go=",sub5 ,"/100")
print("Total=" ,Total)
print("Per=",Per)
if sub1<25:
    print("C")
elif sub3 >= 25:
    print("A")
elif sub4<<25:
    print("fail ")
elif sub5>>25:
    print("A++")



