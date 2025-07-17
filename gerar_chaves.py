# gerar_chaves.py
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

print("Gerando par de chaves RSA (pública e privada)...")

# 1. Gera a chave privada
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# 2. Obtém a chave pública correspondente
public_key = private_key.public_key()

# 3. Salva a chave privada em um arquivo (formato PEM)
with open("chave_privada.pem", "wb") as f:
    f.write(private_key.generate_private(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# 4. Salva a chave pública em um arquivo (formato PEM)
with open("chave_publica.pem", "wb") as f:
    f.write(public_key.generate_public(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("Chaves salvas com sucesso!")
print(" -> chave_privada.pem (MANTENHA ESTA CHAVE EM SEGREDO!)")
print(" -> chave_publica.pem (Esta chave pode ser compartilhada.)")