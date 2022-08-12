def main():
    while True:
        try:
            height = int(input("Please enter your height in cm: "))
            weight = int(input("Please enter your weight in kg: "))
        except:
            print("Let's try again but with NUMBERS only")

        bmi = body_mass_index(height, weight)

        if bmi < 18.5:
            print("You're underweight.")
        elif 18.5 <= bmi <= 24.9:
            print("You have normal weight.")
        elif bmi > 24.9:
            print("You're overweight.")

        repeat = input("Do you want to calculate more? (type 'off' to exit) \n?> ").lower()
        if repeat == "off":
            break
        else:
            continue

def body_mass_index(height, weight):
    return weight / (height/100)**2

if __name__ == '__main__':
    main()
