# criptografar.py
import sys
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Verifica se os argumentos da linha de comando foram passados corretamente
if len(sys.argv) != 3:
    print(f"Uso: python {sys.argv[0]} <arquivo_para_criptografar> <arquivo_chave_publica.pem>")
    sys.exit(1)

arquivo_original = sys.argv[1]
arquivo_chave_publica = sys.argv[2]
arquivo_cifrado = f"{arquivo_original}.cifrado"

print(f"Criptografando '{arquivo_original}'...")

# 1. Carrega a chave pública do arquivo
with open(arquivo_chave_publica, "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

# 2. Lê o conteúdo do arquivo original
with open(arquivo_original, "rb") as f:
    conteudo_original = f.read()

# 3. Criptografa o conteúdo com a chave pública
conteudo_cifrado = public_key.encrypt(
    conteudo_original,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 4. Salva o conteúdo cifrado em um novo arquivo
with open(arquivo_cifrado, "wb") as f:
    f.write(conteudo_cifrado)

print(f"Arquivo criptografado com sucesso e salvo como '{arquivo_cifrado}'")