"""Questão 3- Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas, variando de 0 até 10.
Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor."""

while True:

    try:

        numeroParticipantes = int(input("Quantos participantes esse concurso teve? "))


        for contador in range(numeroParticipantes):

            participante = input(f"Informe nome do {contador +1}º participante: ")


            nota = float(input(f"Informe a nota do {contador + 1}º participante: "))


            if nota >= 0 and nota <= 10:
                if contador == 0 or nota > maior_nota:
                    ganhador = participante
                    maior_nota = nota


            while nota < 0 or nota > 10:
                print("\nA nota deve ser maior que '0' e menor que '10', por favor preencha corretamente. \n")
                nota = float(input(f"Informe nota do {contador +1}º participante: "))
                if nota >= 0 and nota <= 10:
                     if contador == 0 or nota > maior_nota:
                        ganhador = participante
                        maior_nota = nota

        print(f"\nO(a) vencedor(a) foi {ganhador} com nota {maior_nota}!")
        


        print("\n-------------------------------------------------------------------------------------------------------------")
        continuidade = input("Deseja continuar avaliando? \nPara continudar pressione 'Enter'. Caso deseje finalizar operação, apressione 'X'.")

        if continuidade == "x" or continuidade == "X":
            print("Finalizando a operação....")
            print("\nFinalizado! Obrigado pela participação na votação")
            break

    except ValueError:
        print("\n Entrada Inválida \n")
