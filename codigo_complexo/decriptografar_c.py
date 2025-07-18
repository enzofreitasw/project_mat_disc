# decriptografar.py
import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Verifica se os argumentos da linha de comando foram passados corretamente
if len(sys.argv) != 3:
    print(f"Uso: python {sys.argv[0]} <arquivo_para_decriptografar.cifrado> <arquivo_chave_privada.pem>")
    sys.exit(1)

arquivo_cifrado = sys.argv[1]
arquivo_chave_privada = sys.argv[2]
arquivo_decifrado = f"DECRIPTADO_{arquivo_cifrado.replace('.cifrado', '')}"

print(f"Decriptografando '{arquivo_cifrado}'...")

# 1. Carrega a chave privada do arquivo
with open(arquivo_chave_privada, "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

# 2. Lê o conteúdo do arquivo cifrado
with open(arquivo_cifrado, "rb") as f:
    conteudo_cifrado = f.read()

# 3. Decriptografa o conteúdo com a chave privada
conteudo_decifrado = private_key.decrypt(
    conteudo_cifrado,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 4. Salva o conteúdo original em um novo arquivo
with open(arquivo_decifrado, "wb") as f:
    f.write(conteudo_decifrado)

print(f"Arquivo decriptografado com sucesso e salvo como '{arquivo_decifrado}'")