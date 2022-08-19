while True:
    r = int(input("Enter red value from 0 to 255: "))
    g = int(input("Enter green value from 0 to 255: "))
    b = int(input("Enter blue value from 0 to 255: "))
    if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
        break
    else:
        print("Please re-enter the values but within 0-255")

rgb = (r, g, b)

print("RGB:", rgb)
