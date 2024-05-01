from pwn import xor
import itertools

flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

known_text = b'crypto{'
known_key = xor(flag[:len(known_text)], known_text)
print(known_key) # myXORke

known_key = b'myXORkey'
for itertools.