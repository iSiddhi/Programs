#stone paper secissioor



user_input=(input("enter the choic"))
possible_action=['stone','paper','siccor']
import random
computer_input=random.choice(possible_action)
print(computer_input)
if computer_input==user_input:
    print("it will be tie")

elif computer_input=="stone" and user_input=="paper":
    print("you will win") 

elif computer_input=="paper" and user_input=="stone": 
    print("computer will win") 

elif computer_input=="siccor" and user_input=="stone"   :  
        print("computer will win") 

elif computer_input=="stone" and user_input=="siccor" :    
    print("computer will win") 

elif computer_input=="stone " and user_input=="siccor" :    
    print("computer will win") 

elif computer_input=="siccor" and user_input=="stone" :    
    print("you will win") 


else:
    print("invalid")





