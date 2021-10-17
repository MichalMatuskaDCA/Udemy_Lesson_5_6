#Step 1 
import random
import hangman_words as hw
from hangman_art import logo, stages
from replit import clear

print(logo)
lives = 6
chosen_word = random.choice(hw.word_list)
print(chosen_word)

length_word = len(chosen_word)

empty_word = []
for _ in range(length_word):
  empty_word.append("_")

end = True
while end:
  letter = input("Guess a letter : ").lower()
  clear()
  for char in range(length_word):
    if chosen_word[char] in letter:
      empty_word[char] = letter
  print(empty_word)

  if letter not in chosen_word:
    lives -= 1
    print(f"'{letter}' GUESS !!!\nYOU HAVE ALREADY {lives} LIVES")
    if lives > 0:
      print(stages[lives])
    else:
      print(stages[lives])
      print('You loose !!!')
      end = False
  else:
    print(f"'{letter}' GUESS !!!\nCONTINUE !!!")
 
  if '_' not in empty_word:
    end = False
    print("You won !!!")