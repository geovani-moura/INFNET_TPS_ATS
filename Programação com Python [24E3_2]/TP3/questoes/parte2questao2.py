print(
    """
    Parte 2 | Questão 2: 
    Implemente uma função que receba uma string representando uma data no formato "dd/mm/aaaa" e 
    retorne a data em um formato textual, por exemplo, "25/12/2024" -> "Vinte e cinco de dezembro 
    de dois mil e vinte e quatro".
    """
)
print()

unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
especiais = ["onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

def numero_por_extenso(numero):
    if 0 <= numero <= 9:
        return unidades[numero]
    elif 10 <= numero <= 19:
        return especiais[numero - 11]
    elif 20 <= numero <= 99:
        d = numero // 10
        u = numero % 10
        if u == 0:
            return dezenas[d]
        else:
            return f"{dezenas[d]} e {unidades[u]}"
    elif 100 <= numero <= 999:
        c = numero // 100
        r = numero % 100
        if r == 0:
            if c == 1:
                return "cem"
            else:
                return f"{unidades[c]} centos"
        else:
            return f"{unidades[c]} centos e {numero_por_extenso(r)}"
    elif 1000 <= numero <= 9999:
        m = numero // 1000
        r = numero % 1000
        if r == 0:
            if m == 1:
                return "mil"
            else:
                return f"{unidades[m]} mil"
        else:
            return f"{unidades[m]} mil e {numero_por_extenso(r)}"
    else:
        raise ValueError("Número fora do intervalo suportado.")

def dia_por_extenso(dia):
    return numero_por_extenso(dia)

def mes_por_extenso(mes_num):
    return meses[mes_num - 1]

def ano_por_extenso(ano):
    return numero_por_extenso(ano)

def data_por_extenso(data):
    dia, mes_num, ano = map(int, data.split('/'))
    dia_extenso = dia_por_extenso(dia)
    mes_extenso = mes_por_extenso(mes_num)
    ano_extenso = ano_por_extenso(ano)
    return f"{dia_extenso.capitalize()} de {mes_extenso} de {ano_extenso}"

# Exemplo de uso
data = input("Digite a data no formato dd/mm/aaaa: ")
resultado = data_por_extenso(data)
print(f"Data por extenso: {resultado}")
