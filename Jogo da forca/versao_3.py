# Versão 3: Loop de jogo completo e exibição do estado
import random

def main():
    words = ["python", "hangman", "programacao"]
    secret = random.choice(words)
    attempts = 6
    guessed = set()
    while attempts > 0:
        display = "".join([letter if letter in guessed else "_" for letter in secret])
        print("Palavra:", " ".join(display))
        if "_" not in display:
            print("Você venceu!")
            break
        guess = input("Digite uma letra: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Entrada inválida. Digite apenas uma letra.")
            continue
        if guess in guessed:
            print("Você já tentou essa letra.")
            continue
        guessed.add(guess)
        if guess not in secret:
            attempts -= 1
            print(f"Letra incorreta. Restam {attempts} tentativas.")
    else:
        print(f"Você perdeu! A palavra era: {secret}")

if __name__ == "__main__":
    main()
