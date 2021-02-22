#coding: utf-8
"""
Função que analisa o arquivo e realiza os seguintes passos:
    É criado um dicionário onde temos para cada chave os valores para o caminho até o "AS",
    ou seja, no exemplo "28329 6453 38040 23969" o valor da chave é "28329 6453 38040 23969".
    E para seu valor são adicionados todos os prefixos sem repetição correspondentes.
"""
dicionario_de_as = {}

def processaLote(lote):
    global dicionario_de_as
    #Parte de analise dos dados a serem adicionados ao dicionário
    aux_prefixo, aux_as = lote.split("|")[1:3]
    if aux_as in dicionario_de_as.keys():
        dicionario_de_as[aux_as].append(aux_prefixo)
        dicionario_de_as[aux_as] = list(set(dicionario_de_as[aux_as]))
    else:
        dicionario_de_as[aux_as] = [aux_prefixo]

with open('/home/marcone/Workspace/Redes/REDES/Análises/arquivo_ips.txt','r') as ponteiro:
    while True:
        try:
            lote = ponteiro.readline()
            processaLote(lote)
        except Exception as e:
            break


resultado = {}
for chave in dicionario_de_as:
    print(chave, dicionario_de_as[chave],len(dicionario_de_as[chave]))
