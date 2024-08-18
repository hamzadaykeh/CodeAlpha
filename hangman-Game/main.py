import random
list_of_words = ["python", "java", "HTml", "javascript"]

def get_word(list_of_words):
    return random.choice(list_of_words)

def board(word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print(' '.join(display))

def my_guess(word, guessed_letters, guess):
    if guess in word and guess not in guessed_letters:
        guessed_letters.append(guess)
        return True
    elif guess not in guessed_letters:
        guessed_letters.append(guess)
        return False
    return None

def main():

    word = get_word(list_of_words)
    guessed_letters = []
    domain = 6
    result = False
    print("Welcome to HangMan_Game")

    while domain > 0 and not result:
        board(word, guessed_letters)
        guess = input("say a letter").lower()
        if len(guess) == 1 and guess.isalpha():
            Game = my_guess(word, guessed_letters, guess)
            if Game:
                print('Good guess')
            elif Game is False:
                domain-=1
                print('Wrong guess, try another letter')
            else:
                print('you already guessed this letter')
        else:
            print('please enter a valid and suitable letter !')
        if all(letter in guessed_letters for letter in word):
            result = True
    if result:
        print("Congratulation")
    else:
        print("Game over")
if __name__ == "__main__":
    main()







