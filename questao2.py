# Solicita que o usuário digite um número a ser procurado na sequência de Fibonacci
num_procurado = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Inicia as duas primeiras posições da sequência como 0 e 1
fibonacci = [0, 1]

# Gera a sequência de Fibonacci até que o último número seja maior ou igual ao número procurado
while fibonacci[-1] < num_procurado:
    # Calcula o próximo número da sequência Fibonacci como a soma dos dois anteriores
    proximo_fibonacci = fibonacci[-1] + fibonacci[-2]

    # Adiciona o próximo número na lista da sequência Fibonacci
    fibonacci.append(proximo_fibonacci)

# Verifica se o número procurado pertence à sequência de Fibonacci
if num_procurado in fibonacci:
    print(f'O número {num_procurado} pertence à sequência de Fibonacci!')
else:
    print(f'O número {num_procurado} não pertence à sequência de Fibonacci.')
