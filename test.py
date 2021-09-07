"""def bythree(num):
    return num*3
print(list(map(lambda x: x*3,  [1,2,3,4,5])))"""

"""import sys
player1=input("Insert player 1 name: ")
player2=input("Insert player 2 name: ")
print("First some rules \n 1- The first rule of Fight Club is: you do not talk about Fight Club \n 2-choose with lower case ")
p1=input("%s Choose rock, paper or scissors: " %(player1))
p2=input("%s Choose rock, paper or scissors: " % (player2))

def jankenpon_beta(p1_sel,p2_sel):
    if p1_sel == p2_sel:
        return("DRAW")
    elif p1_sel == "rock":
        if p2_sel=="scissors":
            return("%s Win"%(player1))
        else:
            return("%s Win"%(player2))
    elif p1_sel == "paper":
        if p2_sel=="rock":
            return("%s Win"%(player1))
        else:
            return ("%s Win"%(player2))
    elif p1_sel =="scissors":
        if p2_sel == "paper":
            return ("%s Win" % (player1))
        else:
            return ("%s Win" % (player2))
    else:
        return ("Invalid input! You have not entered rock, paper or scissors, try again.")
    return sys.exit("END")"""

"""def fibonacci(fn):
    if fn == 0:
        return 0
    elif fn == 1:
        return 1
    else:
        return fibonacci(fn-1)+fibonacci(fn-2)

user_input=int(input("How many fibonacci numbers do you wanna bitch: "))
fiboresult = []
for i in range(user_input+1):
    if i==0:
        None
    else:
        fiboresult.append(fibonacci(i))
print(fiboresult)

def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib

print(gen_fib())"""

def bodymass(a,b):
    c=a/b**2
    if (18.5)> c:
        return ("under")
    elif (18.5)<= c <25.0:
        return ("normal")
    elif (25.0)<= c <30.0:
        return ("over")
    elif (30.0)<= c:
        return ("obese")


"""def bodymass(a,b,c):
    if c==y:
        if (18.5)>a/(b)**2:
            print("under")
        elif (18.5)<=a/(b**2)<25.0:
            print("normal")
        elif (25.0)<=a/(b**2)<30.0:
            print("over")
        elif (30.0)<=a/(b**2):
            print("obese")
        return bodymass()
    else:
        print("bye")
a=(float(input("Insert weight: ")))
b=(float(input("Insert height: ")))
c=(str(input("Insert y to continue, anykey to exit")))
print(bodymass(80,1.73))"""

def weightedsum(b):
    counter=0
    ii=1
    for i in str(b):
        c = int(i)*ii
        ii += 1
        counter += c
    return counter

def averagearray(array):
    c=0
    counter=0
    for i in array:
        if i != 0:
            c += i
            counter += 1
        elif i ==0:
            c=c/counter
    return c

def diceroll(n):
    return int((n * 6)) + 1




def rever_str(stringss):
    i = len(stringss)
    accum = ""
    while i > 0:
        i -= 1
        accum = accum+stringss[i]
    return accum

def romeoprimo(n):
    i = 2
    acc=[]
    while n>1:
        if n%i ==0:
            acc.append(i)
            n = n / i
        else:
            i += 1
    return acc[-1]


def checksum(array):
    result = 0
    seed = 113
    limit = 10000007
    for i in range(len(array)):
        result = (result+array[i])* seed
    return result % limit

def arraycounter(woods):
    sort_res=[]
    counter = 0
    for i in range(1,21):
        for ii in woods:
            if i == ii:
                counter += 1
        if counter>0:
            sort_res.append(counter)
        counter = 0
    return sort_res




def linearfunc(xy):
    int_x=int((xy[1]-xy[3])/(xy[0]-xy[2]))
    int_y=(xy[1]-(int_x*xy[0]))
    return int_x,int_y

print(linearfunc((0,0,1,1)),linearfunc((1,0,0,1)))