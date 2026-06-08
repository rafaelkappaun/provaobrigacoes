import os
import base64
import logging

logger = logging.getLogger("crypto")

SALT = b"jus_obrigacoes_salt_2024"

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    HAS_CRYPTOGRAPHY = True
except ImportError:
    logger.warning("biblioteca 'cryptography' não encontrada — chaves serão salvas em texto puro")
    HAS_CRYPTOGRAPHY = False


def _get_fernet():
    if not HAS_CRYPTOGRAPHY:
        return None
    password = os.getenv("ENCRYPTION_KEY", "").encode()
    if not password:
        logger.warning("ENCRYPTION_KEY não definida no .env — chaves de API serão salvas em texto puro!")
        return None
    try:
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=SALT, iterations=600000)
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return Fernet(key)
    except Exception as e:
        logger.error(f"Falha ao inicializar criptografia: {e}")
        return None


def encrypt_value(plaintext: str) -> str:
    if not plaintext:
        return ""
    f = _get_fernet()
    if f is None:
        return plaintext
    try:
        return f.encrypt(plaintext.encode()).decode()
    except Exception as e:
        logger.error(f"Erro ao criptografar: {e}")
        return plaintext


def decrypt_value(ciphertext: str) -> str:
    if not ciphertext:
        return ""
    f = _get_fernet()
    if f is None:
        return ciphertext
    try:
        return f.decrypt(ciphertext.encode()).decode()
    except Exception as e:
        logger.error(f"Erro ao descriptografar: {e}")
        return ciphertext
