def collatz(number):
    if(number<0):
        print("Negative number")
        exit()
    elif(number==0):
        print("Number is zero")
        exit()
    elif (number==1):
        exit() 
    else:
        if(number%2==0):
            #print(number,"is even")
            res=number//2
            print(int(res))
            collatz(res)
        elif(number%2==1):
            #print(number,"is odd")
            res=3*number+1
            if(res==0):
                return 1
            else:
                print(int(res))
                collatz(res)
        else:
            print("The number is zero")
            exit()

a=int(input("Enter a number:"))
collatz(a)
