"""Questão 2 - Desenvolva uma função que recebe a idade de uma pessoa e informa
se essa pessoa é: um eleitor obrigatório, facultativo ou não tem direito ao voto."""

while True:
    try:
        idade = int(input("Informe sua idade, por favor: "))
        
        if idade >= 18 and idade < 70:
            print ("Tem obrigação de votar.")
        else:

             if idade == 16 or idade == 17 or idade >= 70:
                 print ("Não tem obrigação de votar.")
             else:

                 if idade <16:
                     print("Não tem direito ao voto.")

        print("\n------------------------------------------------------------")
        continuidade = input("Deseja prosseguir avaliando seu status de voto? \nEntão pressione 'Enter'. Caso queria encerrar operação, pressione 'X'.")

        if continuidade == "X" or continuidade =="x":
            print("Finalizando a operação....")
            print("\nFinalizado! Parabéns pela análise, exerça seu direito democrático.")
            break
        else:
            print("\n------------------------------------------------------------")
            continue

    except ValueError:
        print("\n Entrada Inválida \n")
            
