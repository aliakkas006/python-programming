x = int(input("Enter a num: "))
y = int(input("Enter another num: "))

if x < y:
    print("x is less than y")
elif x > y:
    print('x is greater than y')
else:
    print("x is equal to y")


def show_grade(grade):
    print(f"Your grade is: {grade}")


marks = int(input("Enter your marks: "))
print(type(marks))

if marks >= 80:
    show_grade('A+')
elif marks >= 70:
    show_grade('A')
elif marks >= 60:
    show_grade('A-')
elif marks >= 50:
    show_grade('B')
elif marks >= 40:
    show_grade('C')
elif marks >= 35:
    show_grade('D')
else:
    show_grade('F')


def main():
    x = int(input('Enter a number: '))
    if is_even(x):
        print('Even')
    else:
        print('Odd')


def is_even(n):
    return n % 2 == 0


main()


def find_place():
    name = input("Enter your name: ")

    match name:
        case "Ali" | "Anis" | "Arif":
            print("Chandpur")
        case "Zidan":
            print("Lakshmipur")
        case _:
            print("Didn't know")


find_place()


