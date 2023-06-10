for i in range(int(input())):
    st=input()
    A=set()
    for i in range(len(st)):
        ct=0
        even=0
        odd=0
        for j in range(i,len(st)):
            if(st[j]=="1"):
                ct+=1
            else:
                if(ct%2==0):
                    even+=1
                else:
                    odd+=1
            A.add((j-i+1,even,odd))
    print(len(A))
    A.clear()