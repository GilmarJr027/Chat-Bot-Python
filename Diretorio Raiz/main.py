#coding: utf-8

#chat bot Python
print('*' * 10 ,'Inicio do Chat Bot', '*' * 10)
def chat_run():
        #iniciando opções do sistema propriamente definidas
        chat_inicio_sys = int(100)
        suporte_sys = int(1)
        financeiro_sys = int(2)
        sair_sys = int(0)
            
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
                    from atendimento_suporte import AtendimentoSuporte                   
            
                elif(opcoes_sys == financeiro_sys):
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







