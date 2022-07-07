name = input(" Enter your name : ")
salary = int(input(" Enter a salary : "))
id = int(input(" Enter ID : "))
leave = int(input(" Enter leave : "))
month = int(input(" Enter month : "))
year = int(input(" Enter year : "))
bonus = int(input(" Enter bonus : "))

is_leap = False
if year % 4 == 0 or year % 100 != 0:
    is_leap = True

if month in (1, 3, 5, 7, 8, 10, 12):
    total_days = 31
elif month in (4, 6, 9, 11):
    total_days = 30
elif month == 2 and is_leap:
    total_days = 29
else:
    total_days = 28

per_day = salary / total_days

total_days_year = 365
if is_leap:
    total_days_year = 366


def info():
    print("Emp_name : ", name)


def empid():
    print("Emp_ID : ", id)


def monthly_salary():
    print("Month salary:", salary)


print("=====================")

info()
empid()
monthly_salary()

salary = salary * 12
print("CTC (Yearly Salary):", (salary))

final_salary = per_day * (total_days - leave)
final_salary = final_salary + bonus
print("final salary:", (final_salary))


def get_month(m):
    if m == 1:
        return 'Jan'
    if m == 2:
        return 'Feb'
    if m == 3:
        return 'Mar'
    if m == 4:
        return 'Apr'
    if m == 5:
        return 'May'
    if m == 6:
        return 'Jun'
    if m == 7:
        return 'Jul'
    if m == 8:
        return 'Aug'
    if m == 9:
        return 'Sep'
    if m == 10:
        return 'Oct'
    if m == 11:
        return 'Nov'
    if m == 12:
        return 'Dec'


print(get_month(month), "/", year)

