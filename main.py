from typing import Any


class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Name: {self.name}"

    def __getattribute__(self, __name: str) -> Any:
        print(f"They want to get {__name}")
        return 'Hello'


ddh = Dog("DDH")
print(ddh.name)
