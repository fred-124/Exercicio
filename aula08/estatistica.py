def mediana(a,b,c,d,e,f,g,h,i,j,k):
    return (a+b+c+d+e+f+g+h+i+j) / k
    
from collections import Counter

def moda(sequencia):

    contagem = Counter(sequencia)
    maior_frequencia = max(contagem.values())
    modas = [num for num, freq in contagem.items() if freq == maior_frequencia]

    if len(modas) == 1:
        return f"A moda é: {modas[0]}"
    else:
        return f"Há múltiplas modas: {modas}"

