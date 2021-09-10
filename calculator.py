import math
import time

def addition():
    add0=input("Number 0? ")
    add1=input("Number 2? ")
    answadd=float(add0)+float(add1)
    print("The answer is: ", float(answadd)) if float(answadd)>answadd else print("The answer is ", int(answadd))


def subtraction():
    sub0= input("Number 0? ")
    sub1= input("Number 1? ")
    answsub=float(sub0)-float(sub1, base=0)
    print("The answer is: ", answsub)

def multiplication():
    mul0= input("Number 0? ")
    mul1= input("Number 1? ")
    answmul=float(mul0)*float(mul1)
    print("The answer is: ", int(answmul)) if int(answmul)==float(answmul) else print(float(answmul))

def division():
    div0=input("Number0? ")
    if float(div0)==0.0: 
        print("Føkk deg, den går ikke")
        return
    div1=input("Number1? ")
    if float(div1)==0: 
        print("Føkk deg, den går ikke")
        return
    
    answdiv=float(div0)/float(div1)
    print(int(answdiv)) if int(answdiv) == answdiv else print(answdiv)

def sqrt():
    sqrt0=input("Number? ")
    anssqrt=math.sqrt(float(sqrt0))
    print(int(anssqrt)) if int(anssqrt) == anssqrt else print(anssqrt)

def fac():
    fac0=input("Number? ")
    #Do not look at this
    fac1=float(fac0)
    fac1=int(fac1)
    if float(fac0)>float(fac1):
        print("Føkk deg, feil input")
        return fac()
    else: ansfac=math.factorial(int(fac0))
    print(ansfac)

#Wordlists
addlist=["add","addition","plus","sum","+",]
sublist=["minus","subtraction","subtract","difference","-"]
mullist=["multiply","multiplication","mult","multi","times","*"]
divlist=["Divide","division","fraction","div","/",":"]
sqrtlist=["square root","sqrt","sqrrot",]
faclist=["factorial","!"]
exilist=["exit","esc","sisu"]

def calculate():
    type=input("What type of calculation? ")

    if type in addlist:
        addition()
        exitt=False
    elif type in sublist:
        subtraction()
        exitt=False
    elif type in mullist:
        multiplication()
        exitt=False
    elif type in divlist:
        division()
        exitt=False
    elif type in sqrtlist:
        sqrt()
        exitt=False
    elif type in faclist:
        fac()
        exitt=False
    elif type in exilist:
        exitt=True
        print("Exit")
        exitt=True
    else: 
        print("Føkk deg, prøv noe annet")
        exitt=False
    
    if exitt==True:
        exit
    else:
        more=input("More calculation (y/n)? ")
        if "y" in more:
            return calculate()
        elif "n" in more:
            print("Exit")
            exit
        else:
            print("Føkk deg, feil svar")
            return calculate()


calculate()