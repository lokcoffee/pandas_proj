import pandas as pd

import hashlib
from cryptography.fernet import Fernet

hash_object = hashlib.md5(b"hello world")
"""
5eb63bbbe01eeed093cb22bb8f5acdc3
"""
print(hash_object.hexdigest())

hash_object = hashlib.sha256(b"hello world")
"""
b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
"""
print(hash_object.hexdigest())

key = Fernet.generate_key()
"""
b'V_FB5Rub8FBOPVAblIXoptJtAb6ywNu3MSoGI5zCWO8='
"""
print(key)

cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"hello world")
"""
b'gAAAAABnQxhmZdw7irkWistqp-zMn9WDeb-c2zF_qV_cLV7JNMT7WNg-tToLqdKN5TI2YK_vYB2wK8oL4lrZcsN8nyBsv__gVw=='
"""
print(cipher_text)

plain_text = cipher_suite.decrypt(cipher_text)
"""
b'hello world'
"""
print(plain_text)