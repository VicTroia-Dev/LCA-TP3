#Questão 1- Desenvolva uma função que calcule a divisão de uma conta de consumo(conta de restaurante ou bar), em reais,
#considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.

#Laço para a execução de aplicação:
while True:

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
        print(f"\nO valor total da conta, com a taxa de serviço, será de R$ {totalConsumido}.")
        print(f"Dividindo a conta por {consumidores} pessoas, cada cliente deve pagar R$ {totalConsumidores}.")