i = 0

while i < 3:
    print("Print in while loop")
    i += 1


for _ in range(3):
    print("Print in for loop")


students = ["Ali", "Anis", "Alauddin"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i, students[i])


# Dictionary:
students = {
    "Ali": "Chandpur",
    "Ratul": "Manikgonj",
    "Faruk": "Comilla",
    "Zidan": "Chattogram",
}

for student in students:
    print(
        student, students[student], sep=", "
    )  # when we itetate over an object we find the key of this object


# printing block:


def main():
    width = int(input("Enter the width of the block: "))
    print_block(width)


def print_block(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


main()
