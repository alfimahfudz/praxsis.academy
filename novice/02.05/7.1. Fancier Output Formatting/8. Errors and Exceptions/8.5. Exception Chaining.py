def func():
    raise ConnectionError

try:
    func()  
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
