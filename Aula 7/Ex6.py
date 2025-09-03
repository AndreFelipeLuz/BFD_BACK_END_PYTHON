arquivos = ('documento.pdf', 'foto.jpg', 'relatorio.pdf', 'planilha.xlsx')
quantidade_pdf = arquivos.count('documento.pdf') + arquivos.count('relatorio.pdf')
print(f"O número de arquivos .pdf na tupla é: {quantidade_pdf}")