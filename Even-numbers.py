def getEven(list) :
    even = []
    for n in list :
        if n % 2 == 0:
            even.append(n)
    print("Your numbers are : \n", list, "\n and the even numbers are : \n", even)
list = []
count = 0
while count <= 20 :
    n = int(input("Enter a number : \n"))
    if n % n == 0 :
        list.append(n)
        count += 1
getEven(list)