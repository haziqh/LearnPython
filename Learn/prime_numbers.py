print("\n" + "------------------------------------------------")

count = 0
input = input("What is your number?: ")
for number in range(1, int(input)):
    if number / int(range(1, int(input))) > 1:
        print(number)
        count_even += 1
print(f"We have {count} prime numbers.")

print("\n" + "------------------------------------------------")
