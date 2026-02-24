
def kaprekar(a):
        astr=str(a)
        if(a==6174):
              print(a)
              exit()
        if(len(astr)!=4 and astr[0]!='0'):
            print("Must be a 4 digit!")
            exit()
        asc=sorted(astr)
        desc=sorted(astr,reverse=True)
        if(asc==desc):
              print("Same digits not allowed")
              exit()

        ascint=int("".join(asc))
        descint=int("".join(desc))
        res=descint-ascint
        print(descint,"-",ascint,"=",res)
        print("\n")
        kaprekar(res)

b=int(input("Enter a 4 digit number: "))
kaprekar(b)
