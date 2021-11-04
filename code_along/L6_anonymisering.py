import hashlib as hl 
import pandas as pd

# utf_8 encoded version

secret = "gore_board@gmail.com".encode()
secret2 = "gore_board1@gmail.com".encode()
print(secret)

secret_hash = hl.sha256(secret).hexdigest()
print(f" secret hash: {secret_hash}")

secret_hash2 = hl.sha256(secret2).hexdigest()
print(f" secret hash2: {secret_hash2}")

secret_hash_same = hl.sha256("gore_board@gmail.com".encode()).hexdigest()
print(f"secret hash same: \n{secret_hash_same}")

secret_hash_same2 = hl.sha256("gore_board1@gmail.com".encode()).hexdigest()
print(f"secret hash same2: \n{secret_hash_same2}")

bank = pd.read_csv("BankChurners.csv")
bank["CLIENTNUM"] = bank["CLIENTNUM"].astype(str)

hash_series = bank["CLIENTNUM"].apply(lambda x: hl.sha256(x.encode())).hexdigest()
hash_series.head()

bank.insert(1, "Hashed clientnumbers", hash_series)
