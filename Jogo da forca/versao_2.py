# Versão 2: Suporte a palavra aleatória e tentativas
import random

def main():
    words = ["python", "hangman", "programacao"]
    secret = random.choice(words)
    attempts = 6
    guess = input("Digite um palpite (uma letra): ").lower()
    if guess in secret:
        print("Acertou!")
    else:
        attempts -= 1
        print(f"Errou! Restam {attempts} tentativas.")
    print(f"A palavra era: {secret}")

if __name__ == "__main__":
    main()
