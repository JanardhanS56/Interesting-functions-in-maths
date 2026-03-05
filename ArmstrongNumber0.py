def is_armstrong(n):
    digits = str(n)
    k = len(digits)

    total = 0
    for d in digits:
        total += int(d) ** k

    return total == n

num = int(input("Enter number: "))

if is_armstrong(num):
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
print()
print("Prinitng armstrong numbers within 10000: ")

def is_armstrong1(n):
    digits = str(n)
    k = len(digits)

    total = 0
    for d in digits:
        total += int(d) ** k

    return total == n


for i in range(1, 10000):
    if is_armstrong(i):
        print(i)
