import random
def game(op):
    if op==1:
        print("#repitative")
        
        n=int(input("enter the number of digits u want to play for"))
        lower_limit="1"
        upper_limit="10"
        for i in range(n-1):
            lower_limit+="0"
            upper_limit+="0"
        a=str(random.randrange(int(lower_limit),int(upper_limit)))                       #generate number 
        if a.isdigit():
            l=list(a)
            if len(l)==n:
                i=1
                while True:
                    d=input("enter the number")
                    if d.isdigit():
                        l1=list(d)
                        if len(l1)==n:
                            bull=0
                            cow=0
                            l=list(a)                                          #undo changes made in l n every iteration
                            for j in range(n):                                    #if l has a nuber more repetition than l1                                        
                                if l.count(l1[j])>=l1.count(l1[j]):
                                    if l[j]==l1[j]:
                                        bull+=1
                                        l[j]="a"
                                        l1[j]="a"                                   # it wont disturb the count 
                                    elif (l1[j] in l):
                                        cow+=1
                            for j in range(n):                                       #if l has a nubmer repeted less number of times than l1
                                if l1[j].isdigit():
                                    if l1[j] in l:
                                        if l.count(l1[j])<l1.count(l1[j]):                            
                                            if l[j]==l1[j]:
                                                    bull+=1
                                                    l[j]="a"
                                                    l1[j]="a"
                            for j in range(n):
                                if l1[j].isdigit():
                                    if l.count(l1[j])<l1.count(l1[j]):                                      #cows when l1 has more repetition than l
                                        if l1[j] in l:
                                            cow+=l.count(l1[j])                                   
                                            for i in range(n):
                                                if l[i]==l1[j]:
                                                    l[i]="a"
                            
                            if cow==0 and bull==0:
                                print("none")
                            else:
                                print(cow," cows and ",bull," bulls ")
                            i+=1

                            

                        else:
                            print("pls enter a number with ",n," digits")
                        if d==a:
                            return("Congrats you won")
                            break
            else:
                print("pls enter a number with ",n," digits")

    elif op==2:
        #without repetion

        print("#without repetion")

        n=int(input("enter the number of digits u want to play for"))
        a=""
        for i in range(n):
            bull=str(random.randrange(0,10))
            while bull in a:
                b=str(random.randrange(0,10))
            a+=bull    
        l=list(a)
        if len(l)==n:
            i=1
            d="0"
            while d!=a:
                d=input("enter a number")
                l1=list(d)
                if len(l1)==n:
                    bull=0
                    cow=0
                    for j in range(n):
                        if l.count(l1[j])==l1.count(l1[j]):
                            if l[j]==l1[j]:
                                bull+=1
                                l[j]="a"
                                l1[j]="a"
                            elif l1[j] in l:
                                cow+=1
                                l1[j]="a"
                                for i in range(n):
                                    if l1[j]==l[i]:
                                        l[i]="a"
                    for j in range(n):     
                        if l1[j].isdigit():
                            if l1[j] in l:
                                if l.count(l1[j])<l1.count(l1[j]):
                                    if l[j]==l1[j]:
                                        bull+=1
                                        l[j]="a"
                                        l1[j]="a"
                    for j in range(n):
                        if l1[j].isdigit():
                            if l.count(l1[j])<l1.count(l1[j]):
                                if l1[j] in l:
                                    cow+=l.count(l1[j])
                                    for i in range(n):
                                        if l[i]==l1[j]:
                                            l[i]="a"
                    l=list(a)
                    if cow==0 and bull==0:
                        print("none")
                    else:
                        print(cow," cows and ",bull," bulls ")
                    i+=1
                else:
                    print("pls enter a ",n," digit number only")
        else:
            print("pls enter a ",n," digit number only")

    elif op==3:
        #without repetion(in original number as well as user guesses)

        print("#without repetion(in original number as well as user guesses)")
        n=int(input("enter the number of digits u want to play for"))
        a=""
        for i in range(n):
            bull=str(random.randrange(1,10))
            while bull in a:
                bull=str(random.randrange(1,10))
            a+=bull
        l=list(a)
        if len(l)==n:
            d=""
            while a!=d:
                Cond=True                                       #change the value of d in line 152
                while Cond:
                    d=input("enter a four digit number")
                    for i in d:
                        Cond=False
                        if d.count(i)!=1:                       #VALUE OF d IS FIXED IN FOR LOOP
                            print("Numbers can not be repeated")
                            Cond=True
                            break
                l1=list(d)
                if len(l1)==n:
                    bull=0
                    cow=0
                    for j in range(n):
                        if l[j]==l1[j]:
                            bull+=1
                        elif l1[j] in l:
                            cow+=1
                    if cow==0 and bull==0:
                        print("none")
                    else:
                        print(cow," cows and ",bull," bulls ")                    
                else:
                    print("pls enter a ",n," digit number only")
            print("concrats",n,"is the correct number")
        else:
            print("pls enter a ",n," digit number only")

    else:
        print("Invalid input")
        


print("""                                       MENU 
1. Repetative (Full)
2. Repetive questions Non-Repetative Answer
3. Non-Repetative(Full)
""")
op=int(input("Enter your choice"))
game(op)
