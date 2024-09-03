import hashlib

def calcular_hashes(arquivo, metodos):
    # Inicializa os objetos de hash para cada método
    hashes = {metodo: hashlib.new(metodo) for metodo in metodos}    
    # Abre o arquivo em modo binário e lê em blocos
    with open(arquivo, 'rb') as f:
        for bloco in iter(lambda: f.read(4096), b''):
            for hash_obj in hashes.values():
                hash_obj.update(bloco)
    # Retorna as hashes calculadas em formato hexadecimal
    return {metodo: hash_obj.hexdigest() for metodo, hash_obj in hashes.items()}

def escolher_metodos():
    metodos_disponiveis = hashlib.algorithms_available
    print("Métodos de hash disponíveis:", ', '.join(metodos_disponiveis))
    
    metodos_escolhidos = input("Digite os métodos de hash que você deseja usar, separados por ',' vírgula: ")
    metodos = [metodo.strip() for metodo in metodos_escolhidos.split(',')]
    
    for metodo in metodos:
        if metodo not in metodos_disponiveis:
            print(f"'{metodo}' não é um método de hash válido.")
            return []
    
    return metodos

# Solicita ao usuário os métodos de hash e o arquivo
metodos = escolher_metodos()
if metodos:
    arquivo = input("Digite o caminho do arquivo: ")
    
    try:
        hashes_calculadas = calcular_hashes(arquivo, metodos)
        for metodo, hash_valor in hashes_calculadas.items():
            print(f'A hash {metodo.upper()} do arquivo é: {hash_valor}')
    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado.")
else:
    print("Nenhum método de hash válido foi escolhido. Tente novamente.")
#
#
