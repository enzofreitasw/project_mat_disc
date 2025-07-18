# decriptografar_simples.py
import json

# Carregar a chave privada simples do arquivo JSON
with open('chave_privada_simples.json', 'r') as f:
    chave_privada = json.load(f)
d = chave_privada['d']
n = chave_privada['n']

# Ler a mensagem cifrada do arquivo
with open('mensagem_cifrada.txt', 'r') as f:
    mensagem_cifrada_num = int(f.read())
print(f"Mensagem Cifrada lida do arquivo: {mensagem_cifrada_num}")

# Descriptografia usando a aritmética modular
# M = C^d % n
mensagem_decifrada_num = pow(mensagem_cifrada_num, d, n)

print(f"Cálculo: {mensagem_cifrada_num}^{d} mod {n} = {mensagem_decifrada_num}")
print(f"Mensagem Decifrada (como número): {mensagem_decifrada_num}")

print("\nSUCESSO! O número original foi recuperado.")