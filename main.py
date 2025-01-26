import random #This imports the random function sothat it can be used during our code, specifically for the function randomscam_meth

#This while true statement allows for a loop to occur during the beginning of the game when asing the user if they would like to play or not. Upon clicking no, the code will continue looping itself until the user says yes.
while True:
    print("You have recieved a message would you like to answer it")
    start= input("Enter:'yes' or 'no' ")
    if start == 'yes':
        print("Welcome to the game")
        break
    elif start == 'no':
        continue
    else:
        print("Please respond with ('yes' or 'no') ")
       
scam_meth = ['Call', 'Email'] #This is a list that differs the call or email function

#The randomscam_meth function uses the imported 'random' function that allows for the code to choose between a random scam method.
def randomscam_meth():
    method = random.choice(scam_meth)
    return method
scam_method = randomscam_meth()
print(f"You have randomly got a: {scam_method}")

#The score function(s) imports a variable called score so that we can use it as our score mechanism
score = 100

#This function specifically works to update the users score, taking away 10 from the initial 100 amount and returning it everytime when an incorrect answer is discovered.
def update_score(money):
    money -= 10
    return money

#This wallet function allows for the computer to store the user's current amount of money
def wallet(money):
    print(f"Your current balance is ${money}")
    
#The handle_call function is where the calling scam method is used. We make score a global variable so that it can be used throughout all of the code.
def handle_call():
    global score
    
#These while true loop(s) make it so that the user must input a decision between the options 1 or 2. 
#If the user does not input a variable that is 1 or 2, it will keep asking until a correct variable is inputted by the user. The score will then continously update depending on whether or not the user got the question right or wrong.
#The break statements at the bottom of the if and elif statements make it so that the code won't loop even after a correct answer is inputted.
    while True:
        print("Hello? Is this Ms,Mohammed? This is Mark from your bank’s fraud department. "
              "We’ve detected some unusual activity on your account. Don’t worry, we’ve already taken action "
              "to secure your account, but we need to verify a few details to complete the process. It’s important, "
              "and it'll only take a minute. Can I ask you some questions?")
        print("1. 'I don’t share sensitive information like that over the phone. I’m going to call my bank directly using the number from their website.'\n"
              "2. 'The last four digits are 1234.'")
        
        ans = input("Choose option 1 or 2: ")

        if ans == '2':
            print("You have lost money")
            score = update_score(score)
            wallet(score)
            break
        elif ans == '1':
            print("You have taken a correct step in avoiding a potential scam")
            break
        
    while True:
        print("Alright, that’s the first step… Now, to ensure we’ve locked your account correctly, "
              "I’ll need your full bank account number. This is critical for preventing any further unauthorized access. "
              "Could you provide your account number so I can make sure everything is properly secured?")
        print("1. 'I’m not comfortable sharing my account number over the phone. I’ll contact my bank’s official customer service to verify everything.'\n"
              "2. 'My account number is 987654321.'")
        
        ans = input("Choose option 1 or 2: ")

        if ans == '2':
            print("You have lost money")
            score = update_score(score)
            wallet(score)
            break
        elif ans == '1':
            print("You have taken a correct step in avoiding a potential scam")
            break
            
    while True:
        print("'Good, good… Now we’re almost done. There’s just one more thing. We’ve noticed a transaction at your local grocery store that doesn’t seem to match your usual spending habits. Let’s confirm the details so we can prevent anything else from happening.'")
        print("1. 'I can’t give you that detail over the phone. I’ll call my bank’s customer service to confirm this.'\n2. 'It was $50.00.'")
        
        ans = input("Choose option 1 or 2: ")

        if ans == '2':
            print("You have lost money")
            score = update_score(score)
            wallet(score)
            break
        elif ans == '1':
            print("You have taken a correct step in avoiding a potential scam")
            break
            
    while True:
        print("'Alright, now we’re securing your account. Just one more confirmation… I’ll need to know what device you used to log into your account last time. This helps us pinpoint if anyone has been trying to access it fraudulently.'")
        print("1. 'I won’t share that information over the phone. I’m going to contact my bank’s official number directly.'\n2. 'I used my laptop.'")
        
        ans = input("Choose option 1 or 2: ")

        if ans == '2':
            print("You have lost money")
            score = update_score(score)
            wallet(score)
            break
        elif ans == '1':
            print("You have taken a correct step in avoiding a potential scam")
            break
    
    while True:
        print("'Please provide the verification code I’m sending you. It’ll be a six-digit number.'")
        print("1. 'I understand the process, but I’ll need to verify the request myself through the official app or website.'\n2. 'Sure, my code is 123456.'")
        
        ans = input("Choose option 1 or 2: ")

        if ans == '2':
            print("You have lost money")
            score = update_score(score)
            wallet(score)
            break
        elif ans == '1':
            print("You have taken a correct step in avoiding a potential scam")
            break
            
    while True:
        print("'Almost there… Just a couple more things. We need to confirm your address for the final verification. This is the last step in securing your account. Can you confirm your home address so we can lock everything down?'")
        print("1. 'I haven’t updated my address recently, so I’ll need to check it with my bank first.\n2. 'My address is 123 Main St.'")
        
        ans = input("Choose option 1 or 2: ")

        if ans == '2':
            print("You have lost money")
            score = update_score(score)
            wallet(score)
            break
        elif ans == '1':
            print("You have taken a correct step in avoiding a potential scam")
            break
            
    while True:
        print("'You’re doing great, almost done… To make sure your account is 100% secure, I just need to verify the name of your first pet. This is a final security question to complete the process.'")
        print("1. 'I believe I updated those security questions recently. Let me double-check with my bank.\n2. 'My first pet’s name was Fluffy.'")
        
        ans = input("Choose option 1 or 2: ")

        if ans == '2':
            print("You have lost money")
            score = update_score(score)
            wallet(score)
            break
        elif ans == '1':
            print("You have taken a correct step in avoiding a potential scam")
            break
            
    while True:
        print("'We’re nearly there… I need to confirm your online banking login. We need to check if anyone else has tried to access your account. Can you log in for me now? Do you have your online banking credentials ready to log in? We need to do this quickly to ensure your account is safe.'")
        print("1. 'I’ll log in through my bank’s official site, but I’ll need to use a secure connection.'\n2. 'Yes, I have my login details. Let me log in.'")
        
        ans = input("Choose option 1 or 2: ")

        if ans == '2':
            print("You have lost money")
            score = update_score(score)
            wallet(score)
            break
        elif ans == '1':
            print("You have taken a correct step in avoiding a potential scam")
            break
            
    while True:
        print("'This is getting urgent… We’ve detected a large deposit recently, and we need to confirm that it was authorized. Please tell me the amount of your most recent deposit to make sure it’s legitimate. How much was the last deposit you made into your account? I just need to verify it.'")
        print("1. 'I don’t have the details on hand right now, but I’ll check my deposit history online to verify'\n2. 'I deposited $1,000 last week.'")
        
        ans = input("Choose option 1 or 2: ")

        if ans == '2':
            print("You have lost money")
            score = update_score(score)
            wallet(score)
            break
        elif ans == '1':
            print("You have taken a correct step in avoiding a potential scam")
            break
            
    while True:
        print("'Everything looks great… Now finally, to ensure your funds are safe from further unauthorized activity, I need you to approve a temporary transfer to a safe account. This will protect your money while we finalize everything. Do you agree to transfer your funds to a safe account? This is a security measure to protect you.'")
        print("1. 'I’ll need to verify this transfer request through my bank’s official service. I don’t feel comfortable making this decision over the phone. Goodbye!'\n2. 'Yes, I agree. Please transfer the funds. Thank you, Bye!'")
        
        ans = input("Choose option 1 or 2: ")

        if ans == '2':
            print("You have lost money")
            score = update_score(score)
            wallet(score)
            print(f"\nYou have a total of ${score} left in your bank")
            if score > 40:
                print("Excellent Job, You avoided getting scammed!\nThank You For Playing")
            else:
                print("Unfortunely, You have been scammed!\nThank You For Playing")
            print("Now that you have succesfully played the game, would you like to learn more about Scamming")
            last=input("Enter yes or no: ")
            if last == 'yes':
                print("\nThe most common scam globally is digital advance fee fraud, where perpetrators request upfront payments for fake goods, services, or rewards. These scams are often mass-marketed via email, mail, or calls. Scammers primarily target elderly individuals, particularly those aged 35-44, as they are more vulnerable and less informed about scams compared to younger generations.")
                print("\nHong Kong, Brazil, and Malaysia are most commonly involved in scams, while Kenya, Brazil, and South Africa experience the highest financial losses. Singapore and Switzerland have the highest average amounts lost, with $4,031 and $3,767 respectively. Globally, over $10 billion is lost annually to scams, with $4.6 billion of that coming from investment scams.")
                print("\nIndia, Nigeria, and China are major sources of scams. India is known for cybercrimes like tech support and digital marketing scams. Nigeria primarily uses advance fee fraud and China runs sophisticated state-sponsored hacking operations to steal sensitive information from foreign entities.")
                print("\nHow to Avoid a Scame:\n1.Be cautious of people who contact you, make sure you do not trust random people who you do not know.\n2.If responding, make sure to use contact information you find on your own. Look up the official number or email to confirm if the message is real.\n3.Do not click on links and attachments that don't seem trustworthy, and if you do not know the sender.\n4.Pay attention to how people ask you to send them money. Scammers often ask for gift cards, cryptocurrency, or wire transfers.\n5.Consider that if something is too good to be true, it isn't true. Take a moment to think before choosing deals or prizes that sound too perfect.")
                break
            else:
                print("Well thats to bad, have a nice day!")
                break
        elif ans == '1':
            print("You have taken the last correct step to avoid a potential scam")
            print(f"\nYou have a total of ${score} left in your bank")
#This if and else statement is used to determine if the user has gotten scammed or has avoided being scammed. It uses a greater than symbol to provide the answer.
            if score > 40:
                print("Excellent Job, You avoided getting scammed!\nThank You For Playing")
            else:
                print("Unfortunely, You have been scammed!\nThank You For Playing")
#Simple if and else statement to see if the user want to learn more about scamming. 
            print("Now that you have succesfully played the game, would you like to learn more about Scamming")
            last=input("Enter yes or no: ")
            if last == 'yes':
                print("\nThe most common scam globally is digital advance fee fraud, where perpetrators request upfront payments for fake goods, services, or rewards. These scams are often mass-marketed via email, mail, or calls. Scammers primarily target elderly individuals, particularly those aged 35-44, as they are more vulnerable and less informed about scams compared to younger generations.")
                print("\nHong Kong, Brazil, and Malaysia are most commonly involved in scams, while Kenya, Brazil, and South Africa experience the highest financial losses. Singapore and Switzerland have the highest average amounts lost, with $4,031 and $3,767 respectively. Globally, over $10 billion is lost annually to scams, with $4.6 billion of that coming from investment scams.")
                print("\nIndia, Nigeria, and China are major sources of scams. India is known for cybercrimes like tech support and digital marketing scams. Nigeria primarily uses advance fee fraud and China runs sophisticated state-sponsored hacking operations to steal sensitive information from foreign entities.")
                print("\nHow to Avoid a Scam:\n1.Be cautious of people who contact you, make sure you do not trust random people who you do not know.\n2.If responding, make sure to use contact information you find on your own. Look up the official number or email to confirm if the message is real.\n3.Do not click on links and attachments that don't seem trustworthy, and if you do not know the sender.\n4.Pay attention to how people ask you to send them money. Scammers often ask for gift cards, cryptocurrency, or wire transfers.\n5.Consider that if something is too good to be true, it isn't true. Take a moment to think before choosing deals or prizes that sound too perfect.")
                break
#The handle_email function is where the email scam method is played. We make score a global variable so that it can be used throughout all of the code.  
def handle_email():
    global score
#The list named 'correct' is used to determine the correct answers to the qustion, the code will ask the user. It includes both lowercase and uppercase for the first letter to allow the user the ability to type if lower and upper case 
    correct = ['link','Link','grammer','Grammer','sensitive infromation','Sensitive infromation','fake','Fake','language','Language','format','Format','suspicious','Suspicious','poor','Poor','pressure','Pressure','urgent','Urgent','urgency','Urgency''forceful','Forceful','bad','Bad','email address','Email address','punctuation','Punctuation']
#This print statement is used to print out the scam email so that the user can see it.
    print("""\nSubject: Urgent: Your Account has been Suspended for Security Reasons \nFrom: "Royal Canadian Bank" <security@RoyalCanadianBank.com> \nTo: Ms,Mohammed <Salma.Mohammed@tdsb.on.ca>
    \nDear Ms,Mohammed, \nWe regret to inform you that there has been a suspicious activity detected in your account. As a security measure, we have temporarily suspended your access to ensure the safety of your funds. To regain access to your account, please follow the instructions below:
    \nImmediate Action Required:
    \n1. Click on the link below to verify your identity and reactivate your account:
    www.savebankc.com
   \n2. Log in using your account credentials to confirm your details.
   \nPlease complete this verification within 24 hours to avoid permanent suspension.
   \nFor your security, we recommend you do not share your account details with anyone. If you require assistance, contact us immediately using the link above.
   \nThank you for your prompt attention to this matter.
   \nSincerely,  
   \nRoyal Bank of Canada
   \nFraud Prevention Team  
   \nwww.RoyalCanadianBank.com\n""")
#The attempts variable is used to determine the maximum amount of attempts the user can have to the question.
    attempts = 10
    print("In this email there are 10 hidden fraudulent details that allow people to get scammed. Name the correct details one by one! You have 10 attempts! You need at least 5 corrects answers to avoid getting scammed!")
#This while loop is used to repeat the question over and over again untill the number of attempts reaches 0, in which the loop will stop. 
#The if statement uses an any to determine if any correct answer is found in the list. It checks the answer the user inputted than checks if its in the list named 'correct'.  
    while attempts > 0:
        ans = input(f"Name the correct detail! You have {attempts} attempts remaining: ")
        if any(answer in ans for answer in correct):
            print("Good job!\n")
            attempts -= 1
        else:
            print("Unlucky.")
            score = update_score(score)
            wallet(score)
            attempts -= 1
            print("\n")
        if attempts == 0:
            print("Game over! You have completed all your attempts.\n")
#This if and else statement is used to determine if the user has gotten scammed or has avoided being scammed. It uses a greater than symbol to provide the answer.
            print(f"You have a total of ${score} left in your bank")
            if score > 40:
                print("Excellent Job, You avoided getting scammed!\nThank You For Playing")
#Simple if and else statement to see if the user want to learn more about scamming.
                print("Now that you have succesfully played the game, would you like to learn more about Scamming!")
                last=input("Enter yes or no: ")
                if last == 'yes':
                    print("\nThe most common scam globally is digital advance fee fraud, where perpetrators request upfront payments for fake goods, services, or rewards. These scams are often mass-marketed via email, mail, or calls. Scammers primarily target elderly individuals, particularly those aged 35-44, as they are more vulnerable and less informed about scams compared to younger generations.")
                    print("\nHong Kong, Brazil, and Malaysia are most commonly involved in scams, while Kenya, Brazil, and South Africa experience the highest financial losses. Singapore and Switzerland have the highest average amounts lost, with $4,031 and $3,767 respectively. Globally, over $10 billion is lost annually to scams, with $4.6 billion of that coming from investment scams.")
                    print("\nIndia, Nigeria, and China are major sources of scams. India is known for cybercrimes like tech support and digital marketing scams. Nigeria primarily uses advance fee fraud and China runs sophisticated state-sponsored hacking operations to steal sensitive information from foreign entities.")
                    print("\nHow to Avoid a Scam:\n1.Be cautious of people who contact you, make sure you do not trust random people who you do not know.\n2.If responding, make sure to use contact information you find on your own. Look up the official number or email to confirm if the message is real.\n3.Do not click on links and attachments that don't seem trustworthy, and if you do not know the sender.\n4.Pay attention to how people ask you to send them money. Scammers often ask for gift cards, cryptocurrency, or wire transfers.\n5.Consider that if something is too good to be true, it isn't true. Take a moment to think before choosing deals or prizes that sound too perfect.")
                else:
                    print("Well thats to bad, have a nice day!")
            else:
                print("Unfortunely, You have been scammed!\nThank You For Playing")
#Simple if and else statement to see if the user want to learn more about scamming.
                print("Now that you have succesfully played the game, would you like to learn more about Scamming!")
                last=input("Enter yes or no: ")
                if last == 'yes':
                    print("\nThe most common scam globally is digital advance fee fraud, where perpetrators request upfront payments for fake goods, services, or rewards. These scams are often mass-marketed via email, mail, or calls. Scammers primarily target elderly individuals, particularly those aged 35-44, as they are more vulnerable and less informed about scams compared to younger generations.")
                    print("\nHong Kong, Brazil, and Malaysia are most commonly involved in scams, while Kenya, Brazil, and South Africa experience the highest financial losses. Singapore and Switzerland have the highest average amounts lost, with $4,031 and $3,767 respectively. Globally, over $10 billion is lost annually to scams, with $4.6 billion of that coming from investment scams.")
                    print("\nIndia, Nigeria, and China are major sources of scams. India is known for cybercrimes like tech support and digital marketing scams. Nigeria primarily uses advance fee fraud and China runs sophisticated state-sponsored hacking operations to steal sensitive information from foreign entities.")
                    print("\nHow to Avoid a Scam:\n1.Be cautious of people who contact you, make sure you do not trust random people who you do not know.\n2.If responding, make sure to use contact information you find on your own. Look up the official number or email to confirm if the message is real.\n3.Do not click on links and attachments that don't seem trustworthy, and if you do not know the sender.\n4.Pay attention to how people ask you to send them money. Scammers often ask for gift cards, cryptocurrency, or wire transfers.\n5.Consider that if something is too good to be true, it isn't true. Take a moment to think before choosing deals or prizes that sound too perfect.")
                else:
                    print("Well thats to bad, have a nice day!")
#These statements check to see if the type of scam method, then calls the corresponding handle function to the user.
if scam_method == 'Call':
    handle_call()
elif scam_method == 'Email':
    handle_email()