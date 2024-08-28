meta = 10000
vendas = {
    'João': 15000,
    'Julia': 27000,
    'Marcus': 9900,
    'Maria': 3750,
    'Ana': 10300,
    'Alon': 7870,
}

def calculo_meta(meta, vendas): #function que vai ler o dicionario vendas + a variavel meta
    bateram_meta = [] #lista criada para separar apenas os que no dicionario acima bateram a meta
    for vendedor in vendas: #para cada vendedor 'indice[0]' dentro do dicionario vendas
        if vendas[vendedor] >= meta: #se a venda foi maior ou igual a meta
            bateram_meta.append(vendedor) #append serve para adicionar informações em uma lista
    perc_meta = len(bateram_meta) / len(vendas) #calculo para encontrar o percentual de vendas, len serve para contar os indices
    return perc_meta, bateram_meta #retonar as informações de percentual e dos que bateram a meta

percentual_meta, vendedores_acima_meta = calculo_meta(meta, vendas) #unpacking 
#print(calculo_meta(meta, vendas))
print(f'O percentual dos vendedores que bateram a meta foi de: {percentual_meta:.1f}%')
print(vendedores_acima_meta)