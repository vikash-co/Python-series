import random
word_list = ['python', 'banana', 'hangman', 'challenge', 'easy', 'keyboard']
word = random.choice(word_list)

guessed_word = ['_'] * len(word)
guessed_letters = []
lives = 6


while lives >0 and '_' in guessed_word:
    guess = input("Enter a letter: ").lower()
    guessed_letters.append(guess)

    if guess in word:
        print("Good Guess")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        lives -= 1
        print(f"❌ Wrong guess. Lives left: {lives}")  

if '_' not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)                  