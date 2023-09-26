import random
         

name = input("What is your name? \n")
print(f"\nGood luck! {name.capitalize()},\nLet's get started!\n")
    
try_again = True
    
while try_again == True:         
    if try_again == True:
        list_of_words = ['rainbow', 'computer', 'science', 'programming',
                    'python', 'mathematics', 'player', 'condition',
                    'reverse', 'water', 'board', 'smile', 'whimsical',
                    'side', 'throat', 'hurry', 'measly', 'harbor',
                    'zealous', 'merciful', 'profit', 'worthless', 'observant']

        word = random.choice(list_of_words)

        guesses = ''
        turns = len(word) + 1
        
        print(f"Guess the characters\nYou have {turns} chances.\n")

        while turns > 0:
            failed = 0
               
            for char in word:
                if char in guesses:
                    print(f"{char}\n", end=" ")
                else:
                    print("_")
                    failed += 1
                    
            guess = input("\nGuess a character: ")
                
            guesses += guess
                
            if failed == 0:
                print(f"YOU WIN\nTHE WORD IS [{word.upper()}]\n")
               
                break
            elif guess not in word:
                turns -= 1
                print(f"Wrong\nYou have more {turns} more guesses.")
                    
                if turns == 0:
                    print(f"You lost, the word is [{word.upper()}]")
    
    again = int(input("You want to try again? Type 1 for YES and 2 for NO: "))
                            
    if again == 1:
        try_again = True
    if again == 2:
        try_again = False                
                        
print("Thanks for playing!")
      
