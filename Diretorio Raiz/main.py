#coding: utf-8

#chat bot Python

print('*' * 10 ,'Inicio do Chat Bot', '*' * 10)

def chat_run():

        #iniciando opções do sistema propriamente definidas
        chat_inicio_sys = 100
        suporte_sys = (1)
        financeiro_sys = 2
        sair_sys = 0
            
        while(chat_inicio_sys==100):

            try:
                
                opcoes_sys = int(input("""
                Digite 1 para suporte
                Digite 2 para ir ao financeiro
                Digite 0 para finalizar o programa
                ==>
                """))

                if (opcoes_sys == suporte_sys):
                    print('Voce escolheu a opção suporte!\nAguarde em breve iremos atender')
                    
                    #variavel de inicialização
                    inicio_atendimento = 0
                    
                    while (inicio_atendimento == 0):    
                        try:
                            #tipo de atendimento
                            duvida_geral = int(1)
                            erro_sistema = int(2)
                            nfe_cfe_sat = int(3)
                            atendente = int(4)

            
                if (opcoes_sys == financeiro_sys):
                    print('Você escolheu a opção financeiro\nAguarde em breve iremos atendelo')
                
                elif (opcoes_sys != suporte_sys) and (opcoes_sys != financeiro_sys) and (opcoes_sys != sair_sys):
                    print('Você digitou uma opção invalida\nPor favor escolha uma das opções abaixo:')
                
                #Finaliza o sistema    
                elif (opcoes_sys == sair_sys):
                    print('Obrigado por utilizar o nosso sistema')
                    chat_inicio_sys = 200
                    break
                
            except ValueError as erroValor:
                print('Erro de Tipo ', type(erroValor),'\nPor favor selecione uma opção valida!')

            
chat_run()





