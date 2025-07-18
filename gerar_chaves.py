# gerar_chaves_simples.py
import math
import json # Usaremos JSON para salvar nossas chaves de forma legível

print("--- Início da Geração de Chaves RSA (Versão Educacional) ---")

# Passo 1: Escolher dois números primos distintos e pequenos.
# No mundo real, eles seriam gigantescos e aleatórios.
p = 11
q = 17
print(f"1. Primos escolhidos: p = {p}, q = {q}")

# Passo 2: Calcular 'n', o módulo. 'n' fará parte tanto da chave pública quanto da privada.
n = p * q
print(f"2. Módulo calculado: n = p * q = {p} * {q} = {n}")

# Passo 3: Calcular o 'phi(n)' (Função Totiente de Euler).
# Isso representa a quantidade de números menores que 'n' que são primos relativos a 'n'.
# A fórmula para primos é simples: phi(n) = (p-1) * (q-1)
phi_n = (p - 1) * (q - 1)
print(f"3. Phi(n) calculado: phi_n = (p-1)*(q-1) = {p-1}*{q-1} = {phi_n}")
print("   (Qualquer mensagem criptografada será um número entre 0 e n)")
print("   (Phi(n) é o 'universo' matemático onde a mágica da chave privada acontece)")

# Passo 4: Escolher 'e' (o expoente público).
# 'e' deve ser maior que 1, menor que phi_n, e ser coprimo a phi_n
# (ou seja, o máximo divisor comum entre 'e' e 'phi_n' deve ser 1).
e = 7
# Verificando se 'e' é uma boa escolha
while math.gcd(e, phi_n) != 1:
    e += 1
print(f"4. Expoente público escolhido: e = {e} (verificamos que mdc(e, phi_n) = 1)")

# Passo 5: Calcular 'd' (o expoente privado).
# 'd' é o inverso multiplicativo modular de 'e' módulo phi_n.
# A equação é: (d * e) % phi_n = 1
# O Python 3.8+ torna isso fácil com a função pow(base, exp, mod)
d = pow(e, -1, phi_n)
print(f"5. Expoente privado calculado: d = {d}")
print(f"   (Verificação: ({d} * {e}) % {phi_n} = { (d*e) % phi_n }, que é 1. Correto!)")

# --- Resumo das Chaves ---
print("\n--- Chaves Geradas ---")
print(f"Chave Pública: (e={e}, n={n})")
print(f"Chave Privada: (d={d}, n={n})")

# Salvando as chaves em arquivos JSON para facilitar a leitura
chaves = {
    'publica': {'e': e, 'n': n},
    'privada': {'d': d, 'n': n}
}

with open('chave_publica_simples.json', 'w') as f:
    json.dump(chaves['publica'], f, indent=4)

with open('chave_privada_simples.json', 'w') as f:
    json.dump(chaves['privada'], f, indent=4)

print("\nChaves simples salvas em 'chave_publica_simples.json' e 'chave_privada_simples.json'")