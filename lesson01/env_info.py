import sys
from importlib.metadata import version

print(sys.version)
print(version("httpx"))
print(version("rich"))
print(sys.executable)

if sys.prefix != sys.base_prefix:
    print("окружение активно")
else:
    print("окружение НЕ активно")