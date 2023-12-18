import os
import sys
import csv
import pprint

wheres = [[],[]]
values = [[],[]]
sql = []
qtd_where = 0
table = 'clientes'

def monta_insert(values):
    sql_line = 'INSERT INTO '+table+ ' ('
    sql_temp = ''
    sql_temp2 = ''

    #Limpar arquivo de saida
    with open('Criados/insert.sql', 'w') as arquivo:
        arquivo.write('')

    for indice_valor1, valores1 in enumerate(values): 
        for valores2 in valores1:
            #Verifica se é array de identificação ou valores  
            if indice_valor1 == 0:   
                sql_temp = sql_temp + valores2.replace("'","") + ','
            else:
                for indice_valor2, valores3 in enumerate(valores2):
                    #Verifica se na identificação tem aspas
                    if values[0][indice_valor2][0] == "'":
                        sql_temp2 = sql_temp2 + "'" + valores3 + "',"
                    else: 
                        sql_temp2 = sql_temp2 + valores3 + ','

                #tira a ultima virgula
                sql_temp2 = sql_temp2[:-1]

                sql_temp = sql_line + '(' + sql_temp2 + ');'
                sql.append(sql_temp)
                with open('Criados/insert.sql', 'a') as arquivo:
                    arquivo.write(str(sql_temp)+'\n')
                sql_temp2 = ''

        #tira a ultima virgula
        sql_temp = sql_temp[:-1]

        if indice_valor1 == 0: 
            #coloca a parte do values
            sql_line = sql_line + sql_temp + ') VALUES '

        sql_temp = ''
    

def monta_update():
    print("Opção 2 selecionada.")

def monta_delete():
    print("Opção 3 selecionada.")

def operacao():
    print("Selecione a operação:")
    print("1 - Insert")
    print("2 - Update")
    print("3 - Delete")
    print("0 - Sair")

    opcao = input("O que deseja fazer? ")

    if opcao == '1':
        monta_insert()
    elif opcao == '2':
        monta_update()
    elif opcao == '3':
        monta_delete()
    elif opcao == '0':
        sys.exit(0)
    else:
        print("Opção inválida, tente novamente.")
        menu()

def arquivo():
    caminho_arquivo = input("Informe o caminho do csv: ")

    if os.path.exists(caminho_arquivo):
        causulas_where() 
    else:        
        print("O arquivo inexistente.")
        arquivo()

def causulas_where():
    qtd_where = input("Quantas cláusula where? ")

    if qtd_where.isdigit():
        operacao()
    else:
        print("Valor inválido.")
        causulas_where() 

def ler_arquivo():
    with open('teste.csv', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=';')

        for indice_linha, linha in enumerate(leitor_csv):
            array_temp_wheres = []
            array_temp_values =[]
            for indice_valor, valor in enumerate(linha):
                if indice_linha == 0: 
                    if indice_valor < qtd_where:
                        wheres[0].append(valor)
                    else:    
                        values[0].append(valor)  
                else:
                    if indice_valor < qtd_where:
                        array_temp_wheres[1].append(valor)
                    else:
                        array_temp_values.append(valor)
                
            if indice_linha < qtd_where and len(array_temp_wheres) != 0:
                wheres[1].append(array_temp_wheres) 
            elif len(array_temp_values) != 0:       
                values[1].append(array_temp_values)                
                
        monta_insert(values)

ler_arquivo()
#arquivo()
#causulas_where()
#operacao()
