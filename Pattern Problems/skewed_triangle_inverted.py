def pattern(n):
    for i in range(n, 0 , -1):
        for j in range(i):
            print("*" , end= "")
        print()


def pattern1(n):
    for i in range(n):
        for j in range(i):
            print(" " , end = "")


        for k in range(n, i , -1):
            print("*" , end = "")

        print()




pattern(5)
pattern1(5)