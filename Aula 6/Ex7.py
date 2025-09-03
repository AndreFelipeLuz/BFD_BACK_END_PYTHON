status_pedido = input("Digite o status do pedido (recebido, em_preparacao, em_entrega, entregue): ")

match status_pedido:
    case "recebido":
        print("Seu pedido foi recebido e está aguardando processamento.")
    case "em_preparacao":
        print("Seu pedido está sendo preparado pela nossa equipe.")
    case "em_entrega":
        print("Seu pedido saiu para entrega e está a caminho do seu endereço.")
    case "entregue":
        print("Seu pedido foi entregue! Aproveite sua compra.")
    case _:
        print("Status não identificado. Por favor, verifique se digitou corretamente.")