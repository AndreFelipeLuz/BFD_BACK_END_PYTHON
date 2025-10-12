class ECommerce:
    def __init__(self):
        self.produtos = ["Notebook", "Mouse", "Teclado"]
        self.carrinho = {}
        self.pedidos = []
        self.usuarios = {"cliente1": "senha1", "admin": "admin_senha"}
        self.relatorios = []

    def navegar_produtos(self):
        print("Cliente navega pelos produtos disponíveis.")
        return self.produtos

    def adicionar_ao_carrinho(self, usuario, produto):
        if usuario not in self.carrinho:
            self.carrinho[usuario] = []
        self.carrinho[usuario].append(produto)
        print(f"Produto '{produto}' adicionado ao carrinho de {usuario}.")

    def finalizar_compra(self, usuario, metodo_pagamento):
        print("\n--- INÍCIO FINALIZAR COMPRA ---")
        if not self.autenticar_usuario(usuario):
            print("ERRO: Autenticação falhou. A compra não pode ser finalizada.")
            return False

        if not self.processar_pagamento(usuario, metodo_pagamento):
            print("ERRO: Pagamento falhou. A compra não pode ser concluída.")
            return False

        nota_fiscal = self.gerar_nota_fiscal(usuario, self.carrinho.get(usuario, []))

        self.enviar_produto(nota_fiscal)

        self.pedidos.append({"usuario": usuario, "itens": self.carrinho.pop(usuario, []), "status": "Enviado"})
        print(f"Compra do usuário {usuario} finalizada com sucesso.")
        print("--- FIM FINALIZAR COMPRA ---\n")
        return True

    def autenticar_usuario(self, usuario):
        if usuario in self.usuarios:
            print("Usuário autenticado.")
            return True
        print("Falha na autenticação.")
        return False

    def gerar_nota_fiscal(self, usuario, itens):
        nota = f"NF-2025/123456 - Destinatário: {usuario} - Itens: {', '.join(itens)}"
        print(f"Nota Fiscal Gerada: {nota}")
        return nota

    def acompanhar_pedido(self, usuario):
        pedidos_cliente = [p for p in self.pedidos if p['usuario'] == usuario]
        if pedidos_cliente:
            print(f"Pedidos de {usuario}: {pedidos_cliente}")
        else:
            print(f"{usuario} não possui pedidos para acompanhar.")

    def processar_pagamento(self, usuario, metodo):
        print(f"Interagindo com o Sistema de Pagamento para processar pagamento de {usuario} via {metodo}...")
        
        if metodo.lower() == "falha":
            self.notificar_falha_de_pagamento(usuario)
            return False
        
        print("Pagamento processado com sucesso.")
        return True

    def notificar_falha_de_pagamento(self, usuario):
        print(f"AVISO: Falha de pagamento detectada para o usuário {usuario}.")
        print("Notificação enviada ao Cliente.")

    def enviar_produto(self, nota_fiscal):
        print(f"Interagindo com a Transportadora para Enviar Produto (NF: {nota_fiscal[:15]}...)")
        print("Produto pronto para envio.")


class Administrador:
    def __init__(self, sistema_ecommerce):
        self.sistema = sistema_ecommerce

    def gerenciar_produtos(self, acao, nome=None):
        if acao == "adicionar":
            self.sistema.produtos.append(nome)
            print(f"Admin: Produto '{nome}' adicionado.")
        elif acao == "listar":
            print(f"Admin: Produtos atuais: {self.sistema.produtos}")

    def gerenciar_usuarios(self, acao, usuario=None):
        if acao == "listar":
            print(f"Admin: Usuários: {list(self.sistema.usuarios.keys())}")

    def gerenciar_pedidos(self):
        print(f"Admin: Lista de Pedidos (pendentes/enviados): {self.sistema.pedidos}")

    def gerar_relatorios(self, tipo):
        relatorio = f"Relatório de {tipo} gerado em 11/10/2025: X vendas, Y receita."
        self.sistema.relatorios.append(relatorio)
        print(f"Admin: {relatorio}")
        return relatorio

ecommerce = ECommerce()
admin = Administrador(ecommerce)

print("--- AÇÕES DO CLIENTE ---")
ecommerce.navegar_produtos()
ecommerce.adicionar_ao_carrinho("cliente1", "Notebook")
ecommerce.adicionar_ao_carrinho("cliente1", "Mouse")
ecommerce.finalizar_compra("cliente1", "Cartão")
ecommerce.acompanhar_pedido("cliente1")

print("\n--- TESTE DE FALHA DE PAGAMENTO ---")
ecommerce.adicionar_ao_carrinho("cliente_falha", "Webcam")
ecommerce.finalizar_compra("cliente_falha", "Falha")

print("\n--- AÇÕES DO ADMINISTRADOR ---")
admin.gerenciar_produtos("adicionar", "Impressora")
admin.gerenciar_produtos("listar")
admin.gerenciar_pedidos()
admin.gerenciar_usuarios("listar")
admin.gerar_relatorios("Vendas")