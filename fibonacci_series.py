user_input = int(input("Enter upper limit for fibonacci series: "))
a = 0
b = 1
print(a, b, end=" ")

for i in range(2, user_input + 1):
    c = a + b
    a = b
    b = c
    print(c, end=" ")