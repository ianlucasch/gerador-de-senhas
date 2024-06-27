import random
import string

size = int(input('Digite o tamanho de senha que você deseja: '))

chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+,.;:/?<>[]{}~^'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))