import math
def pythCheck():
    
    l1 = []
    l2 = []
    n = int(input("\nEnter number of elements: "))
    for i in range(n):
        num = int(input("\nEnter number: "))
        l1.append(num)
    l1.sort(reverse=True)
    flag = 0
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            c = (l1[i]**2)-(l1[j]**2)
            sqrc = math.sqrt(c)
            sqr1 = int(math.ceil(sqrc))
            sqr2 = int(math.floor(sqrc))
            if sqr1==sqr2:
                for e in range(j+1,n):
                    if l1[e]==sqr1:
                        flag = 1
                        count+=1
                        print("\na,b,c can be ",sqr1,l1[j],l1[i])
                        
    if flag==0:
        print("\nNo Pythogorean Triplet here!")
    else:
        print("\nTotal count = ",count)
                        
                
pythCheck()