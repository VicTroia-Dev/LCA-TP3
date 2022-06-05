"""Questão 2 - Desenvolva uma função que recebe a idade de uma pessoa e informa
se essa pessoa é: um eleitor obrigatório, facultativo ou não tem direito ao voto."""

while True:
    
        idade = int(input("Informe sua idade, por favor: "))
        
        if idade >= 18 and idade < 70:
            print ("Tem obrigação de votar.")
        else:

             if idade == 16 or idade == 17 or idade >= 70:
                 print ("Não tem obrigação de votar.")
             else:

                 if idade <16:
                     print("Não tem direito ao voto.")
            
