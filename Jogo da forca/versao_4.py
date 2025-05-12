# Versão 4: Organização em funções
import random

def choose_word():
    words = ["python", "hangman", "programacao"]
    return random.choice(words)

def display_state(secret, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in secret])

def get_guess(guessed):
    guess = input("Digite uma letra: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Entrada inválida. Digite apenas uma letra.")
        return None
    if guess in guessed:
        print("Você já tentou essa letra.")
        return None
    return guess

def main():
    secret = choose_word()
    attempts = 6
    guessed = set()
    while attempts > 0:
        print("Palavra:", display_state(secret, guessed))
        if all(letter in guessed for letter in secret):
            print("Parabéns, você venceu!")
            break
        guess = get_guess(guessed)
        if not guess:
            continue
        guessed.add(guess)
        if guess not in secret:
            attempts -= 1
            print(f"Letra incorreta. Restam {attempts} tentativas.")
    else:
        print(f"Fim de jogo! A palavra era: {secret}")

if __name__ == "__main__":
    main()
