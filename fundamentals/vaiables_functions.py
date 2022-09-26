# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

name = input("Enter your name: ").strip().title()

print(f"Asslamualaikum, {name}")

x = int(input("Enter x's value: "))
y = int(input("Enter y's value: "))

z = x + y

print(f"The result = {z}")

x1 = float(input("Enter a number: "))
y1 = float(input("Enter a number: "))

z1 = round(x1 + y1)

print(f"The result = {z1:,}")   # comma before triple zero


def main():
    x = int(input("Enter a number: "))
    print(f"Square of this number = {square(x)}")


def square(n):
    return pow(n, 2)


main()


