import hashlib
from typing import Any


class HashTable(object):
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.table: list[list[list[object]]] = [[] for _ in range(self.size)]

    def hash(self, key: str | int) -> int:
        if isinstance(key, str):
            encoded_key = key.encode()
        else:
            encoded_key = bytes(key)
        md5_hash = hashlib.md5(encoded_key).hexdigest()
        return int(md5_hash, base=16) % self.size

    def add(self, key: str | int, value: object) -> None:
        idx = self.hash(key)
        for data in self.table[idx]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[idx].append([key, value])

    def get(self, key: str | int) -> Any:
        idx = self.hash(key)
        for data in self.table[idx]:
            if data[0] == key:
                return data[1]

    def __repr__(self):
        str_ = ""
        for i, data in enumerate(self.table):
            str_ += str(i)
            for pair in data:
                str_ += f"->{pair}"
            str_ += "\n"
        return str_

    def __setitem__(self, key: str | int, value: Any) -> None:
        self.add(key, value)

    def __getitem__(self, key: str | int) -> Any:
        return self.get(key)


def main():
    hash_tbl = HashTable(10)
    hash_tbl["beta"] = "choc"
    hash_tbl["alpha"] = "mint"
    hash_tbl["charlie"] = "biscuit"
    hash_tbl["sns"] = "YouTube"
    hash_tbl["pc"] = "Mac"
    print(hash_tbl)


if __name__ == "__main__":
    main()
