from Crypto.Cipher import AES

def aes_128_ecb_encrypt(hex_string, key):
    # Convertir la chaîne hexadécimale en bytes
    plaintext = bytes.fromhex(hex_string)

    # Convertir la clé en bytes
    key = bytes.fromhex(key)

    # Initialiser le chiffreur en mode ECB
    cipher = AES.new(key, AES.MODE_ECB)

    # Chiffrer le texte en clair
    ciphertext = cipher.encrypt(plaintext)

    # Convertir le texte chiffré en chaîne hexadécimale
    return ciphertext.hex()

# Exemple d'utilisation
hex_string = "6bc1bee22e409f96e93d7e117393172a"
key = "2b7e151628aed2a6abf7158809cf4f3c"
ciphertext = aes_128_ecb_encrypt(hex_string, key)
print(ciphertext)  # Affiche le texte chiffré en chaîne hexadécimale