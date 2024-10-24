import random

def jogar_adivinhacao():
    numero_adivinhar = random.randint(1, 100)
    tentativas = 0

    print('Seja bem-vindo ao jogo da adivinhação!!')
    print('Tente adivinhar o número que estou pensando entre 1 e 100.')
    palpite = int(input('Digite seu palpite: '))

    while True:
        
        tentativas += 1

        if palpite < numero_adivinhar:
            print('Tente um número maior.')
        elif palpite > numero_adivinhar:
            print('Tente um número menor.')
        else:
            print(f'Boaaaaa, você acertou o número {numero_adivinhar} em {tentativas} tentativas')
            break

        palpite = int(input('Digite um novo palpite: '))
        
def main():
    while True:
        jogar_adivinhacao()
        jogar_novamente = input('Deseja jogar o jogo novamente? (s/n): ').lower()

        if jogar_novamente != 's':
            print('Obrigado por jogar :)')
            break
main()