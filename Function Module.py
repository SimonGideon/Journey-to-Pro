import functools
import locale


@lru_cache(maxsize=None)  # Boundless cache.
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(15))

# reduce.
from functools import reduce
def factorial(n):
    return reduce(lambda a, b: (a**b), range(1, n+1))

# The dis module
# Disassembling modules.
import dis
import marshal
with open("<file.pyc", "rb") as code_f:
    code_f.read(8)
    code = marshal.load(code_f)
    dis.dis(code)


# The base64 MOdule.
import base64
s = "Hello world!"
b = s.encode("UTF-8")
e = base64.b64decode(b)
print(e)

# Queue Module.
from Queue import Queue
question_que + Queue()
for x in range(1, 10):
    temp_dict = ('key', x)
    question_que.put(temp_dict)
while(not question_queu.empty()):
    item = question_queue.get()
    print(str(item))