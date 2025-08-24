senha = "Python123"

senha_nao_vazia = len(senha) > 0
tem_mais_de_8_caracteres = len(senha) > 8
senha_e_exatamente_igual = senha == "Python123"
senha_e_diferente_de_123456 = senha != "123456"

senha_valida = (senha_nao_vazia and 
                tem_mais_de_8_caracteres and 
                senha_e_exatamente_igual and 
                senha_e_diferente_de_123456)

print(f"A senha é válida? {senha_valida}")