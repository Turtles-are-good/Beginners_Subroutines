time = float(input("What time is it (Write : as .)?   :      "))
name = input("What is your name?  :   ").strip().lower()
def morning(a, name) :
    return "Good ", a, name
def afternoon(b, name) :
    return "Good" , b, name
def evening(c, name) :
    return "Good" , c, name

if time >= 0 or time < 13 :
    a = "morning"
elif time >= 13 or time < 17 :
    b = "afternoon"
elif time >= 17 or time <= 23.59 :
    c = "evening"
