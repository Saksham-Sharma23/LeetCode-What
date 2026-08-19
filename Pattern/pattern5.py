def pattern5(n):

    for i in range(n , 0 , -1):
        for j in range(1 , i+1):
            print(j , end = "")

        print()


pattern5(5)


#OR

def pattern5b(n):
    for i in range(1, n+1) :
        for j in range(1, n-i+2):
            print(j , end = "")

        print()

pattern5b(5)