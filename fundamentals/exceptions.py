# try:
# except:
# else:

def main():
    x = get_int("Enter x: ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
