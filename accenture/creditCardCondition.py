#let's assume you are a credit card provider and your role is to issue a credit cards, 16 digits, and the (sum of odd position + sum of even position)%10==0. Don't use array, list, tuples, etc. Credit card is not a string.
#we need to generate such numbers and check if the credit card is valid or not.

credit_card_number=1234567890123456
pos=16
even_sum=0
odd_sum=0
while(pos>=1):
    last_number=credit_card_number%10
    if(pos%2==0):
        even_sum+=last_number
    else:
        odd_sum+=last_number
    credit_card_number=credit_card_number//10
    pos=pos-1
if((even_sum+odd_sum)%10==0):
    print("Credit card is valid")
else:
    print("Credit card is invalid")