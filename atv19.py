nota1,nota2=float(input("nota 1: ")),float(input("nota 2: "))
if (nota1+nota2)/2 < 5:
    print("REPROVADO")
elif (nota1+nota2)/2 > 7:
    print("APROVADO")
else: 
    print("RECUPERAÇÃO")