import random
import string

code_size = 5

def generate_key(size=code_size, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def generate_unique_key(obj, size=code_size):
    new_key = generate_key(size=size)
    Klass = obj.__class__
    if Klass.objects.filter(key=new_key).exists():
        return generate_unique_key(obj, size=size)
    return new_key