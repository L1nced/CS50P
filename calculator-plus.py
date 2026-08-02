choice = int(input("Qual operador você planeja utilizar? soma {1}; subtração {2}; multiplicação {3}; divisão {4}: "))
if choice == 1:
    soma1 = float(input("Primeiro valor da soma: "))
    soma2 = float(input("Segundo valor da soma: "))
    soma3 = soma1 + soma2
    print("Valor da soma:", soma3)
elif choice == 2:
    sub1 = float(input("Valor total para a subtração: "))
    sub2 = float(input("Valor a ser subtraído: "))
    sub3 = sub1 - sub2
    print("Valor da subtração:", sub3)
elif choice == 3:
    mult1 = float(input("Primeiro valor da multiplicação: "))
    mult2 = float(input("Segundo valor da multiplicação: "))
    mult3 = mult1 * mult2
    print("Valor da multiplicação:", mult3)
elif choice == 4:
    div1 = float(input("Dividendo (valor total que vai ser dividido): "))
    div2 = float(input("Divisor (número que vai dividir): "))
    try:
        div3 = div1 / div2
        print("O resultado da divisão é:", div3)
    except ZeroDivisionError:
        print("Não é possível dividir por zero")