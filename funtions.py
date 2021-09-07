def sumoftwo(a,b): # from http://www.codeabbey.com/index/task_view/sum-of-two
    suma= a + b
    return suma

def suminloop(lista): # http://www.codeabbey.com/index/task_view/sum-in-loop
    for i in lista:
        return sum(lista)

def sumsinloop (list1,list2): #http://www.codeabbey.com/index/task_view/sums-in-loop
    lista=[]
    for i in range(len(list1)):
        lista.append(list1[i] + list2[i])
    return lista

def minoftwo(list1,list2): #http://www.codeabbey.com/index/task_view/min-of-two
    list3 =[]
    for i in range(len(list1)):
        if list1[i] > list2[i]:
            list3.append(list2[i])
        else:
            list3.append(list1[i])
    return list3

def minofthree(list1,list2,list3): #http://www.codeabbey.com/index/task_view/min-of-three
    list4 = []
    for i in range(len(list1)):
        if not len(list1)==len(list2)==len(list3):
            break
        if list1[i] < list2[i] and list1[i]<list3[i]:
            list4.append(list1[i])
        else:
            if list2[i] < list1[i] and list2[i]<list3[i]:
                list4.append(list2[i])
            else:
                list4.append(list3[i])
    return list4

def max_array(lista): #http://www.codeabbey.com/index/task_view/maximum-of-array
    maximo = lista[0]
    minimo = lista[0]
    for num in range(len(lista)):
        if maximo<lista[num]:
           maximo=lista[num]
        elif minimo>lista[num]:
            minimo=lista[num]
    return maximo,minimo

def rounding(lista1,lista2): #http://www.codeabbey.com/index/task_view/rounding
    lista3 = []
    for elem in range(len(lista1)):
        res = lista1[elem]/lista2[elem]
        lista3.append(ceiling(res))
    return lista3

def ceiling(res): #http://www.codeabbey.com/index/task_view/rounding
    int_part = int(res)
    dec_part = res - int_part
    if dec_part ==0:
        ceil = int_part
    elif dec_part >=0:
        ceil=int_part + 1
    return ceil

def rounding_beta(list1,list2): #http://www.codeabbey.com/index/task_view/rounding
    list3 = []
    for elem in range(len(list1)):
        result = list1[elem]/list2[elem]
        int_part= int(result)
        dec_part= result - int_part
        if dec_part >= 0.5:
           result = int_part + 1
        else:
           result = int_part
        list3.append(result)
    return list3

def rounding_beta1(list1,list2): #http://www.codeabbey.com/index/task_view/rounding
    list3 = []
    for elem in range(len(list2)):
        if not len(list1)==len(list2):
           break
        try:
            result = list1[elem]/list2[elem]
            decimal= result - int(result)
            list3.append(int(result)+1 if (decimal >= 0.5) else int(result))
        except:
            list3.append("Cannot divide by ZERO")
    return list3

def farenheittocelsius(faren): #http://www.codeabbey.com/index/task_view/fahrenheit-celsius
    celsius = []
    for i in range(len(faren)):
        convert=(faren[i]-32)*(5/9)
        decimal=convert-int(convert)
        celsius.append(int(convert)+1 if decimal>=0.5 else int(convert)) if convert>=0 else celsius.append(int(convert)-1 if decimal<=-0.5 else int(convert))
    return celsius

def vowelcount(listwords): #http://www.codeabbey.com/index/task_view/vowel-count
    vowels="aeiou" ; countedvowel=[]
    for words in range(len(listwords)):
        counter = 0
        for letter in listwords[words]:
            if letter in vowels:
                counter = counter + 1
        countedvowel.append(counter)
    return countedvowel

def sumofdigits(a,b,c): #http://www.codeabbey.com/index/task_view/sum-of-digits
    finalresult=[]
    for n in range(len(a)):
        if not len(a)==len(b)==len(c):
            break
        try:
            result=((a[n]*b[n])+ c[n])
            preresult = 0
            for i in str(result):
                preresult += int(i)
            finalresult.append(preresult)
        except:
            print("list problem")
    return finalresult

def arithmeticprogression(a): #http://www.codeabbey.com/index/task_view/arithmetic-progression
    result=[]
    preresult = 0
    for ii in range(a[2]):
        preresult += a[0] + (a[1]*ii)
    result.append(preresult)
    return result

def sums(num):
    return num+num

def arithmeticprogressionbeta(list):#ok final
    a=[]
    for i in range(list[-1]):
        a.append(list[0]+i*list[1])
    return sum(a)

def multiples(lista): # from https://projecteuler.net/problem=1
    l=[] #here, de list is stored
    for i in range(lista):
        if i%3==0 or i%5==0: #where 3 or 5 , it's the multiple
            l.append(i)
    return sum(l)

def collatz(n): 
    count = 0
    if n ==1:
        return count
    count += 1
    if n%2 == 0:
        return count + collatz(n//2)
    else:
        return count + collatz(3*n+1)

def checklist(a,b): 
	c = []
	for i in a:
		if i in b:
			c.append(i)
	return c

def checklist_b(a,b): 
    c = []
    for i in a:
        if i in b :
            if i not in c:
                c.append(i)
    d = sorted(c)
    return d

def notrepeat(a): 
    new_list=[]
    for i in range(len(a)):
        if a[i] not in new_list:
            new_list.append(a[i])
    return new_list

def medianofthree(list1,list2,list3): #http://www.codeabbey.com/index/task_view/median-of-three
    list4=[]
    list1=sorted(list1)
    list2=sorted(list2)
    list3=sorted(list3)
    list4.append(list1[1]),list4.append(list2[1]),list4.append(list3[1])
    return list4

def triangles(lists): #http://www.codeabbey.com/index/task_view/triangles
    result=[]
    for i in lists:
        if i[0] > 0 and i[1] > 0 and i[2] >0:
            if i[0]+i[1]>i[2]:
                result.append(1)
            else:
                result.append(0)
        else:
            result.append("error negativo")
    return result

def upperandlowerbeta(inputstr):
    countupper=0
    countlower=0
    for i in inputstr:
        if 65<=ord(i)<=90:
            countupper+=1
        elif 97<=ord(i)<=122:
            countlower+=1
    return countlower,countupper

def fizzbuzz():
    for i in range(1,51):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
    return ""

def fizzbuzzwhile():
    i=0
    while i<50:
        i += 1
        if i%3==0 and i%5==0:
            print("fizzbuzz")
            continue
        elif i%3==0:
            print("fizz")
            continue
        elif i%5==0:
            print("buzz")
            continue
    return ""

def jankenpon_beta2():
    player1=input("Insert player 1 name: ")
    player2=input("Insert player 2 name: ")
    print("First some rules \n 1- The first rule of Fight Club is: you do not talk about Fight Club \n 2-choose with lower case ")
    choices=[]
    choices.append(int(input("%s Select \n1-rock\n2-paper\n3-scissors\nYour choice is number: " %(player1))))
    choices.append(int(input("%s Select \n1-rock\n2-paper\n3-scissors\nYour choice is number: " %(player1))))
    for sel in choices:
        if choices[0]==choices[1]:
            print("It's a tie")
        elif choices[0]==1 and choices[1]==2:
            print("Player 2 wins")
        elif choices[0] == 1 and choices[1] == 3:
            print("Player 1 wins")

    print(choices)

    return sys.exit("END")

def numtodigits(numbers):
    result=0
    while numbers > 0:
        result=(numbers/10)
    return result
print(numtodigits(10))

def bythree(num):
    return num*3
    
print(list(map(lambda x: x*3,  [1,2,3,4,5])))

def fibonacci(fn):
    if fn == 0:
        return 0
    elif fn == 1:
        return 1
    else:
        return fibonacci(fn-1)+fibonacci(fn-2)

user_input=int(input("How many fibonacci numbers do you want: "))
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

print(gen_fib())

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

def primenumber(n):
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



