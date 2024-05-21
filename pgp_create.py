import gnupg
import os
import random
import string

# Initialize the gnupg instance
gpg = gnupg.GPG()

# Generate a random 20-character password
password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=20))

# Define key input parameters for maximum security
input_data = gpg.gen_key_input(
    name_real='My Key',
    name_comment='Custom comment or description',
    name_email='user@example.com',
    passphrase=password,
    key_type='RSA',
    key_length=4096,
    expire_date='2y'
)

# Generate the key
key = gpg.gen_key(input_data)

# Export the public and private keys
public_key = gpg.export_keys(key.fingerprint)
private_key = gpg.export_keys(key.fingerprint, True, passphrase=password)

# Save the keys to .ASC files
with open('PGP_public.asc', 'w') as pub_file:
    pub_file.write(public_key)

with open('PGP_private.asc', 'w') as priv_file:
    priv_file.write(private_key)

# Save the password to a .txt file
with open('PGP_password.txt', 'w') as pass_file:
    pass_file.write(password)

print("PGP key pair and password have been generated and saved to files.")

