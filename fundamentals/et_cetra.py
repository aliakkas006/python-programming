# 1:
balance = 0
def main():
    print("Previous Balance: ", balance)
    deposit(500)
    withdraw(50)
    print("Current Balance: ", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == '__main__':
    main()


# 2:
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


def main():
    account = Account()
    print("Prev balance: ", account.balance)
    account.deposit(500)
    account.withdraw(50)
    print("New balance: ", account.balance)


if __name__ == "__main__":
    main()


# 3: variable type
def cat(n: int) -> str:
    return "Cat\n" * n


number: int = int(input("Number: "))
cats: str = cat(number)
print(cats, end="")


# 4: variable number of arguments
def func(*args, **kwargs):
    print("Positional: ", args)
    print("Named: ", kwargs)


func(5, 10, 15)
func(galleons=100, sickles=50, knuts=25)


# 5: map(function, iterable), list comprehensions
def main():
    yell("This", "is", "mine")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())

    uppercased = map(str.upper, words)

    uppercased = [word.upper() for word in words]
    print(*uppercased)      # unpacking the list


if __name__ == "__main__":
    main()

students = [
    {"name": "Ali", "house": "Chandpur"},
    {"name": "Alauddin", "house": "Chandpur"},
    {"name": "Anis", "house": "Chattogram"},
    {"name": "Arif", "house": "Comilla"},
    {"name": "Zidan", "house": "Chandpur"},
]

chandpurs = [
    student["name"] for student in students if student["house"] == "Chandpur"
]

for chandpur in sorted(chandpurs):
    print(chandpur)


# 6: filter(function, iterable)
chandpurs = filter(lambda st: st["house"] == "Chandpur", students)      # lamda function

for chandpur in sorted(chandpurs, key=lambda st: st["name"]):
    print(chandpur["name"])


# 7: dictionary comprehensive
students = ["Ali", "Anis", "Zidan"]

chandpurs = []
for student in students:
    chandpurs.append({"name": student, "house": "Chandpur"})

chandpurs = [{"name": student, "house": "Chandpurs"} for student in students]

chandpursDict = {student: "Chandpur" for student in students}
print(chandpurs)


# 8: enumerate(iterable, start=0)
students = ["Ali", "Anis", "Zidan"]

for i in range(len(students)):
    print(i + 1, students[i])

for i, student in enumerate(students):
    print(i + 1, student)


# 9: iterator, generator
def main():
    n = int(input("What's n?"))
    for s in star(n):
        print(s)


def star(n):
    for i in range(n):
        yield "*" * i


if __name__ == "__main__":
    main()