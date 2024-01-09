name=input("Enter your name: ")
amt=int(input("Enter your shopping amount: "))
discountedValue=amt
discount=0
def discounter(value,p):
    return (value-(p/100)*value)
    
if(amt>=4000):
    print("You get 4% discount !")
    discount=4
    discountedValue=discounter(amt,4)
elif(amt>=3000):
     print("You get 3% discount !")
     discount=3
     discountedValue=discounter(amt,3)
elif(amt>=2000):
     print("You get 2% discount !")
     discount=2
     discountedValue=discounter(amt,2)
elif(amt>=1000):
     print("You get 1% discount !")
     discount=1
     discountedValue=discounter(amt,1)
else:
    print("No discount applicable !")
print("Initial amount to be paid was",amt)
print("Amount to be paid after discount is: ", discountedValue)
print("===================================================================")
print("Thankyou for shopping",name,", Visit again !")
    
