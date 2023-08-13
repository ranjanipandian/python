#hangman game

#first perseon guess a word and the ----- are shown to the second person and he need to  guess it with a limit no of guesses and for every wrong attempt there is loose of life

#expected output:
#Let's Play Hangman!!

#You Have only 6 lives so try to guess the word within 6 attempts! Good luck !!


import random
import word_file
lives=6
chosen_word= random.choice(word_file.words)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
  display+='_'
print(display)
game_over=False
while not game_over:
    guess_letter=input("Guess a letter:").lower()
    for position in range(len(chosen_word)):
         letter = chosen_word[position]
         if letter==guess_letter:
           display[position]=guess_letter
    print(display)
    if guess_letter not in chosen_word:
        lives -=1
        if lives==0:
            game_over= True
            print("You lose !!")
    if '_' not in display:
        game_over=True
        print("You win !!!")
  
