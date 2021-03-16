#coding: utf-8
import os
dicionario_de_as = {}
'''
Função que analisa o arquivo e realiza os seguintes passos:
    É criado um dicionário onde temos para cada chave o valor mais a direita do "AS",
    ou seja, no exemplo "28329 6453 38040 23969" o valor da chave é "23969".
    E para seu valor são adicionados todos os prefixos sem repetição correspondentes.
'''
path = os.path.abspath(__file__)
path = os.path.dirname(path)

def processaLote(lote):
    """
    Função que processa as informações do arquivo
    """
    global dicionario_de_as
    #Pego os valores de interesse
    aux_prefixo, aux_as = lote.split("|")[1:3]
    #Realizo as verificações necessárias a fim de adicionar os valores no dicionário.
    try:
        if aux_as in dicionario_de_as.keys():
            dicionario_de_as[aux_as.split()[-1]].append(aux_prefixo)
            dicionario_de_as[aux_as.split()[-1]] = list(set(dicionario_de_as[aux_as.split()[-1]]))
        else:
            dicionario_de_as[aux_as.split()[-1]] = [aux_prefixo]
    except:
        pass
#Abertura do arquivo
with open((path, 'Análises', 'arquivo_ips.txt'),'r') as ponteiro:
    while True:
        try:
            lote = ponteiro.readline()
            processaLote(lote)
        except Exception as e:
            break

#Mostrando os resultados obtidos
resultado = {}
for chave in dicionario_de_as:
    print(chave, dicionario_de_as[chave],len(dicionario_de_as[chave]))
