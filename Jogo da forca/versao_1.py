# Versão 1: Esqueleto básico
def main():
    secret = input("Digite a palavra secreta: ").lower()
    guess = input("Digite um palpite (uma letra): ").lower()
    if guess in secret:
        print("Acertou!")
    else:
        print("Errou!")

if __name__ == "__main__":
    main()
