def multiplication_table(num):
    for i in range(1, 11):
        print(str(num) + " X " + str(i) + " = " + str(num * i))
num = int(input("Enter a number: "))
multiplication_table(num)