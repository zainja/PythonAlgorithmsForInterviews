import pyhash
bit_vector = [0]*20

fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32

# calculate the output of FNV and Murmur hash functions for Pikachu and
# Charmander
fnv_pika = fnv('Pickachu') % 20
fnv_char = fnv('Charmander') % 20

murmur_pika = murmur('Pickachu') % 20
murmur_char = murmur('Charmander') % 20

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1
bit_vector[fnv_char] = 1
bit_vector[murmur_char] = 1