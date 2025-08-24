tem_wifi = False
tem_dados_moveis = True

pode_conectar_internet = tem_wifi or tem_dados_moveis

print(f"O celular pode se conectar a internet? {pode_conectar_internet}")