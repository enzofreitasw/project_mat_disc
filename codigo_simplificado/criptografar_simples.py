# criptografar_simples.py
import json

# Carregar a chave pública simples do arquivo JSON
with open('chave_publica_simples.json', 'r') as f:
    chave_publica = json.load(f)
e = chave_publica['e']
n = chave_publica['n']

# Mensagem original (deve ser um número menor que 'n')
# No nosso caso, n = 187, então a mensagem deve ser um número < 187
mensagem_original_num = 51 # 'Pinga'
print(f"Mensagem Original (como número): {mensagem_original_num}")

# Criptografia usando a aritmética modular
# C = M^e % n
mensagem_cifrada_num = pow(mensagem_original_num, e, n)

print(f"Cálculo: {mensagem_original_num}^{e} mod {n} = {mensagem_cifrada_num}")
print(f"Mensagem Cifrada (como número): {mensagem_cifrada_num}")

# Salvando o número criptografado em um arquivo
with open('mensagem_cifrada.txt', 'w') as f:
    f.write(str(mensagem_cifrada_num))

print("Mensagem não cifrada salva em 'mensagem_cifrada.txt'")