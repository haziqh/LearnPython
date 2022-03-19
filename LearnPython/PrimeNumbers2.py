print("\n" + "------------------------------------------------")

count = 0
input = int(input("What is your number?: "))

for number in range(2, input):
    if (input % number) == 0:
        print(number)
        count += 1
print(f"We have {count} prime numbers.")

print("\n" + "------------------------------------------------")
