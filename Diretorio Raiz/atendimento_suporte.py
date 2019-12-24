class AtendimentoSuporte():

    def run_atendimento():
    #variavel de inicialização
        inicio_atendimento = 0
                    
        while (inicio_atendimento == 0):    
        
        
            try:
                #tipo de atendimento
                duvida_geral = int(1)
                erro_sistema = int(2)
                nfe_cfe_sat = int(3)
                atendente = int(4)
                retornar = int(5)

                opcoes_suporte = int(input("""
                Digite 1 para Atendimento de Duvida em Geral
                Digite 2 para Atendimento sobre Erros no Sistema
                Digite 3 para Atendimento referente a (NFe, MDFe, CTe, CFe, SAT)
                Digite 4 para Falar com o Atendente
                Digite 5 para Retornar ao menu principal
                """))
                
                if(opcoes_suporte == retornar):
                    print('Retonando ao menu inicial')
                    break
                

            except ValueError as erro_Valor:
                print('Erro de Tipo ', type(erro_Valor), '\Por favor digite uma opção valida')
    run_atendimento()

AtendimentoSuporte()

