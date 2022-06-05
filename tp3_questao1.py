#Questão 1- Desenvolva uma função que calcule a divisão de uma conta de consumo(conta de restaurante ou bar), em reais,
#considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.

#Laço para a execução de aplicação:
while True:

    try:

        #Valor total gasto
        total = float(input("Informe o valor do consumo: R$ "))

        #Constatação do valor total
        if total > 0:

            #Número de clientes
            consumidores = int(input("Informe o total de clientes: "))

            #Verificação do número de clientes
            if consumidores >= 1:

                #Taxa de serviço
                porcentagem = float(input("Informe o percentual do serviço, entre 0 a 100: "))

                #Verificação da taxa de serviço
                if porcentagem >=0 and porcentagem <=100:

                    #Formatação dos valores
                    totalConsumido = float(total+(total*porcentagem/100))
                    totalConsumidores = float(totalConsumido/consumidores)
                    totalConsumido = ("%0.2f" % totalConsumido).replace(".", ",")
                    totalConsumidores = ("%0.2f" % totalConsumidores).replace(".", ",")

                    #Imprimir na tela o resultado da função 
                    print(f"O valor total da conta, com a taxa de serviço, será de R$ {totalConsumido}.\n")
                    print(f"Dividindo a conta por {consumidores} pessoas, cada cliente deve pagar R$ {totalConsumidores}.")

                #Erro na porcentagem
                else:
                    print("A porcentagem deve ser entre '0' e '100'.")

            #Erro no número de clientes
            else:
                print("Valor inválido. Necessário o mínimo de 1 pessoa.")

        #Erro de consumo
        else:
            print("Você precisa ter consumido algum produto do bar!")



        print("\n-------------------------------------------------------------------------------------------------------------")
        continuidade = input("Deseja continuar calculando? \nPara continudar pressione 'Enter'. Caso deseje finalizar operação, apressione 'X'.")

        if continuidade == "x" or continuidade == "X":
            print("Finalizando a operação....")
            print("\nFinalizado! Obrigado pela preferência")
            break

    except ValueError:
        print("\n Entrada Inválida \n")
