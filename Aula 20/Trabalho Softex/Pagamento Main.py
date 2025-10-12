import random
from time import sleep

class Api_Pagamento():
    def __init__(self,):
        
        # Variaveis fixas para simular o status do codigo
        self.status_aprovado = "succeeded"
        self.status_falhou = "failed"
        self.status_pendente = "pending"
        self.status_erro_conecao = "mock_error" 
        
        self.valor_falha = 15.00
    def criar_cobranca(self, valor, id_transacao):
        print(f"[API] Recebendo requisição para transação {id_transacao} no valor R${valor:.2f}")
        
        #Abaixo uma cadeia de if e elif para fazer a simulação da api
        
        if valor == self.valor_falha:
            status = self.status_falhou
            mensagem = "Pagamento rejeitado pela operadora."
        elif random.random() < 0.1:
            status = self.status_erro_conecao
            mensagem = "Erro de conexão/sistema na API."
        elif random.random() < 0.15:
            status = self.status_pendente
            mensagem = "Pagamento em análise."
        else:
            status = self.status_aprovado
            mensagem = "Pagamento aprovado com sucesso."
        
        sleep(0.5) 
        
        #Retorna o Dicionario e envia para o pagamento.
        return {
            "api_id": f"ch_{id_transacao}_{random.randint(1000, 9999)}",
            "status": status,
            "message": mensagem
        }

class Pagamento:
    #Nesse caso a api cliente significa para utilizar a simulação de pagamento.

    def __init__(self, api_client : Api_Pagamento):
        self.api = api_client
        self.transacoes = {}
        
    def processar_pagamento(self, valor, metodo_pagamento="Cartão de Crédito"):
        
        #Cria uma Transacão que interage e simula com a API.
        
        nova_transacao = Transacao(valor, metodo_pagamento)
        self.transacoes[nova_transacao.id] = nova_transacao
        
        print(f"\n--- Processando Transação {nova_transacao.id} (R${valor:.2f}) ---")
        
        api_response = self.api.criar_cobranca(valor, nova_transacao.id)
        
        # Atualiza o objeto Transacao com a resposta da API
        
        nova_transacao.status = api_response['status']
        nova_transacao.api_id = api_response['api_id']
        nova_transacao.mensagem = api_response['message']
        
        print(f"[Sistema] Transação {nova_transacao.id} Status: {nova_transacao.status}")
        
        # Verifica o status Para poder disparar se tiver falha ou erro.
        
        if nova_transacao.status in [self.api.status_falhou, self.api.status_erro_conecao, self.api.status_pendente]:
            self.enviar_alerta(nova_transacao.id,nova_transacao.valor,nova_transacao.mensagem)
        
        return nova_transacao.id

    def verificar_status(self, id_transacao):
        """
        Verifica e exibe o status de uma transação específica.
        """
        transacao = self.transacoes.get(id_transacao)
        if transacao:
            print(f"\nStatus da Transação {id_transacao}:")
            print(f"  Valor: R${transacao.valor:.2f}")
            print(f"  Status: {transacao.status.upper()}")
            print(f"  Mensagem API: {transacao.mensagem}")
            print(f"  Data/Hora: {transacao.data_criacao.strftime('%Y-%m-%d %H:%M:%S')}")
            return transacao.status
        else:
            print(f"\nErro: Transação {id_transacao} não encontrada.")
            return None
    def enviar_alerta(self, id_transacao, valor, motivo):
        alerta = (
            f"\n[!!! ALERTA DE FALHA DE PAGAMENTO !!!]\n"
            f"Transação ID: {id_transacao}\n"
            f"Valor: R${valor:.2f}\n"
            f"Motivo da Falha: {motivo}\n"
            f"Ação: Disparar email para o cliente e logar para análise da equipe."
        )
        print("-" * 50)
        print(alerta)
        print("-" * 50)


class Transacao:
    
    # Representação os dados de uma transação de pagamento em nosso sistema.
    # Contador estático para gerar IDs de transação
    _id_counter = 1
    
    def __init__(self, valor, metodo):
        from datetime import datetime
        self.id = self._id_counter
        Transacao._id_counter += 1
        self.valor = valor
        self.metodo = metodo
        self.data_criacao = datetime.now()
        self.status = "iniciado"
        self.api_id = None
        self.mensagem = None

    def __repr__(self):
        return (f"<Transacao ID={self.id}, Valor={self.valor:.2f}, "
                f"Status='{self.status}'>")


api =Api_Pagamento()
sistema = Pagamento(api)

id1 = sistema.processar_pagamento(250.75)
sistema.verificar_status(id1)
