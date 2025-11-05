from Crypto.Util.number import bytes_to_long, getRandomInteger, getPrime, long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random

m = getPrime(1024)
a = random.randint(2, m)
b = random.randint(2, m)
x = random.randint(2, m)

for i in range(8):
    x = (a * x + b) % m
    print('x{} = {}'.format(i, hex(x >> 850)))
x = (a * x + b) % m

flag = 'ASEAN{fake_flag}'
key = long_to_bytes(x)
ciphertext = AES.new(key[:16], AES.MODE_ECB).encrypt(pad(flag.encode(), 16))
print('ciphertext =', ciphertext.hex())

# x0 = 0x10d7d6f98670fc7a8946ead6cc341515f8cb2cc0543
# x1 = 0x3be21ba2012033d994789a535180cf636a663785f91d
# x2 = 0x22a0d74c1aa7f655b71043a0d9c099d9af39006746e9
# x3 = 0x19dca855fb0396157349e33510c9f84e45c71ba5ef3
# x4 = 0x11e6c8ccf28602aab2e4c6b9a48bb8849d06ba20949e
# x5 = 0xabe5d7f11cdd3e81b458eb6499dae80494dc5a31fb6
# x6 = 0x1c2930ad36ac56ca9c6afdf0490d10410739d2f543fc
# x7 = 0x22956b1d6379da1f628f43c0adb2922aa2df60ed17a6
# ciphertext = 766a8a92c8446ebe37ce3858e5143c6d