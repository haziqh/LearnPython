#Weight-Checker
weight = input("What is your weight?: ")
unit = input("(K)g or (L)bs?: ")

# kg to lbs
kg_weight = (float(weight) * 2.2)
if unit == str("K"):
    print(str(kg_weight) + "lbs")

if kg_weight > 100:
    print("You are overweight, consider exercising.")

# lbs to kg
lbs_weight = (float(weight) / 2.2)
if unit == str("L"):
    print(str(lbs_weight) + "kgs")

if lbs_weight > 220:
    print("You are overweight, consider exercising.")

# Weather-Checker
print("Let's check the weather!")
temperature = int(input("What is the temperature?: "))

if temperature >= 30:
    print("It's a hot ass day! Bring sunblock")

if temperature <= 22:
    print("It's cold, bring a jacket")
elif temperature:
    print("Seems like perfect weather outside!")
