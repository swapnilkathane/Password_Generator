import random
import string
N=10
passwd = ''.join(random.choice(string.ascii_letters+string.digits) for i in range(N))
print(passwd)

