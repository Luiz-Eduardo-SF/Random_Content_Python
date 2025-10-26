def leiaInt(txt):
    while True:
        try:
            inteiro = int(input(txt))
        except (TypeError, ValueError):
            print(f'\033[1;31mERRO! Por favor, digite um valor inteiro válido!\033[m')
        except (KeyboardInterrupt):
            print(f'\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return inteiro
def leiaFloat(txt):
    while True:
        try:
            real = float(input(txt))
        except (TypeError, ValueError):
            print(f'\033[1;31mERRO! Por favor, digite um valor real válido!\033[m')
        except (KeyboardInterrupt):
            print(f'\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return real