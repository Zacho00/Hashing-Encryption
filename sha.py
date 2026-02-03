import hashlib
hash = hashlib.sha256()
hash.update(b'Hello World!')
print(hash.digest())