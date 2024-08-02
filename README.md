# Nome do projeto: calcular-hash-de-arquivo

## Calcula o código hash de um arquivo com base em uma função **_hash_**.

- Este programa usa uma biblioteca Pyhton chamada **_hashlib_**. Ela tem todas as hashes disponiveis no momento.

### O que é uma **_função hash_**?

<p>
    Uma função de hash criptográfico, é conhecida como hash - é um algoritmo matemático que transforma qualquer bloco de dados em uma série de caracteres de comprimento fixo.
</p>

Clique para saber mais ==> [função hash](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_hash).

<p>

    - A função escolher_metodos exibe os métodos de hash disponíveis e solicita ao usuário que digite os métodos desejados.

    - O usuário digita os métodos separados por vírgula, e o programa verifica se cada método é válido.

    - Se todos os métodos são válidos, o programa solicita o caminho do arquivo e calcula as hashes usando os métodos escolhidos.

    - O programa retorna as informações no terminal do cliente.

</p>

### Git Clone

[Clone calcular-hash-de-arquivo](https://github.com/cabraldasilvac/calcular-hash-de-arquivo.git)

### Como usar:

- Instalar o python

  `brew install python`

- Rodar o código escrito em
  `python3 <nome-programa> `.

- Escolha o Hash que deseja usar. Pode ser escolhido mais de um. Eles devem ser separados por uma ','.
  Exemplo: MD5, SHA-1, SHA-256

- Informe o caminho e nome do arquivo.

===> Use este código para fazer os seus testes. Observe o código hash gerado e faça alteração no arquivo. Gere outra hash para obeservar a mudança no código gerado.

Prints:
![img01](images/img01.png)

![img02](images/img02.png)

![img03](images/img03.png)
