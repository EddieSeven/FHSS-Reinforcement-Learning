# Libraries used to create a key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
# Library used to load key
from cryptography.hazmat.primitives import serialization
# Support libraries
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

# Creating private key (2048 is default in docs)
private_key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 2048,
    backend = default_backend()
)


# Loading an existing key saved on disk (no key on file, so commented out)
# with open("path/to/key.pem", "rb") as key_file:
#     private_key = serialization.load_pem_private_key(
#         key_file.read(),
#         password = None,
#         backend = default_backend()
# )

# Public Key
public_key = private_key.public_key()

# Encryption to ciphertext (requires a public key)
# The message1 variable holds the initial message (in bits) before encryption
message1 = b"Test Message"
ciphertext = public_key.encrypt(
    message1,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA1()),
        algorithm = hashes.SHA1(),
        label = None
    )
)

# Test print the encrypted ciphertest
print("\nEncrypted! Ciphertext is:\n{}".format(ciphertext))

# Signing, padding, and salt
signature = private_key.sign(
    message1,
    padding.PSS(
        mgf = padding.MGF1(hashes.SHA256()),
        salt_length = padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Private key signature verification (raises exception if signature not a match)
public_key.verify(
    signature,
    message1,
    padding.PSS(
        mgf = padding.MGF1(hashes.SHA256()),
        salt_length = padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)


# Decryption
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf = padding.MGF1(algorithm = hashes.SHA1()),
        algorithm = hashes.SHA1(),
        label = None
    )
)
# Decrypted message is back in plaintext
plaintext == message1

# Test print the decrypted plaintext message
print("\nDecrypted! It worked! Decrypted Message:\n{}".format(plaintext))

## Usage Steps:
## Generate a Private Key
## Use Private key to generate Public key
## (Optional) Digitially sign encryption
## (Optional) If signed, verify key signature (to check if Private key matches)
## Encrypt message using Public key
## Owner of Private key can decrypt any messages encrypted by corresponsding Public Key
