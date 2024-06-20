MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Pode tirar a CNH!")
    
elif idade < MAIOR_IDADE:
    print("Não pode tirar a CNH!")