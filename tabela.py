import pandas as pd

tabela = pd.read_csv("alunos.csv")
media = []
situacao = []
for i in tabela.index:
    media.append((tabela['nota_1'][i]+tabela['nota_2'][i])/2)
    if(media[i] >= 7 and tabela['faltas'][i]<=5):
        situacao.append("APROVADO")
    else:
        situacao.append("REPROVADO")
    
tabela_2 = tabela.assign(media = media, situacao = situacao)
tabela_2.to_csv("situacao.csv")

print(f"SITUACAO DOS ALUNOS:\n{tabela_2}")

maiorfalta = tabela_2["faltas"].max()
mediaDaTurma = tabela_2["media"].median()
maiormedia = tabela_2["media"].max()

print(f"\nmaior quantidade de faltas: {maiorfalta}")
print(f"media da turma: {mediaDaTurma}")
print(f"maior media da turma: {maiormedia}")