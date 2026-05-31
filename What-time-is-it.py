time = float(input("What time is it? (Write : as .)\n"))
name = input("What is your name?\n").strip().lower()
def times(a, b) :
    return f"Good {a} {b}"
if time >= 0.00 and time <= 12.59 :
    print(times("morning", name))
elif time >= 13.00 and time <= 17.59 :
    print(times("afternoon", name))
elif time >= 18.00 and time <= 23.59 :
    print(times("evening", name))
else :
    print("Enter a valid time")
