#This really is a mess of aproject, it was one of my first 
#"large" projects and i really had no experience.

import math
#Hmm yes, i will import math for calculator project

# Safe number input
def safe_float_input(prompt):
    result = None

    # Loop while no result has been accuired
    while result == None:
        # Prompt user for input
        userinput = input(prompt)

        # Attempt to cast to float
        try:
            result = float(userinput)
        except:
            # Ensure that result is stil None
            result = None
            
            # Print an error message
            print("Error: invalid input.")

    # Return the result
    return result

def addition():
    #Addition could be modeled better as with all other functions
    add0 = safe_float_input("Number 0? ")
    add1 = safe_float_input("Number 1? ")
    answadd=add0+add1
    print("The answer is: ", float(answadd)) if float(answadd)>answadd else print("The answer is ", int(answadd))
    #I definetly wrote the code above

def subtraction():
    sub0 = safe_float_input("Number 0? ")
    sub1 = safe_float_input("Number 1? ")
    answsub=float(sub0)-float(sub1, base=0)
    print("The answer is: ", answsub)

def multiplication():
    mul0 = safe_float_input("Number 0? ")
    mul1 = safe_float_input("Number 1? ")
    answmul=float(mul0)*float(mul1)
    print("The answer is: ", int(answmul)) if int(answmul)==float(answmul) else print(float(answmul))

def division():
    div0 = safe_float_input("Number0? ")
    if float(div0)==0.0: 
        print("Føkk deg, den går ikke")
        return
    div1 = safe_float_input("Number1? ")
    if float(div1)==0: 
        print("Føkk deg, den går ikke")
        return
    
    answdiv=float(div0)/float(div1)
    print(int(answdiv)) if int(answdiv) == answdiv else print(answdiv)
    #You didnt see anything

def sqrt():
    sqrt0 = safe_float_input("Number? ")
    anssqrt=math.sqrt(float(sqrt0))
    print(int(anssqrt)) if int(anssqrt) == anssqrt else print(anssqrt)

def fac():
    fac0 = safe_float_input("Number? ")
    #Do not look at this
    fac1=float(fac0)
    fac1=int(fac1)
    if float(fac0)>float(fac1):
        print("Føkk deg, feil input")
        return fac()
    else: ansfac=math.factorial(int(fac0))
    print(ansfac)

#Defines the morecalc function, which asks for more 
#calculation after succsessful calculation
def morecalc():
    more=input("More calculation (y/n)? ")
    more=more.lower()
    if "y" in more or "yes" in more:
        return calculate()
    elif "n" in more or "no" in more:
        print("Exit")
        exit
    else:
        print("Fuck you, yes or no?")
        return morecalc()

#Wordlists
addlist=["add","addition","plus","sum","+",]
sublist=["minus","subtraction","subtract","difference","-"]
mullist=["multiply","multiplication","mult","multi","times","*"]
divlist=["Divide","division","fraction","div","/",":"]
sqrtlist=["square root","sqrt","sqrrot",]
faclist=["factorial","!"]
exilist=["exit","esc","sisu"]

#The calculate function is a mess
def calculate():
    type=input("What type of calculation? ")
    type=type.lower()
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
    else: morecalc()
        

#Hmmm yes, calculate
calculate()