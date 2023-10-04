import time
from typing import List, Optional, Tuple

#   runtime: beats 96%
#   memory: beats 97%
class MyHashMap_wrapper:

    def __init__(self):
        self.data = dict()

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        return self.data[key]

    def remove(self, key: int) -> None:
        if key in self.data:
            self.data.pop(key)


#   runtime: beats 10%
#   memory: beats 97%
class MyHashMap_naive:

    def __init__(self):
        self.index = []
        self.values = []

    def _search(self, key: int) -> Optional[int]:
        for i, n in enumerate(self.index):
            if n == key:
                return i
        return None

    def put(self, key: int, value: int) -> None:
        index = self._search(key)
        if index is None:
            self.index.append(key)
            self.values.append(value)
        else:
            self.values[index] = value

    def get(self, key: int) -> int:
        index = self._search(key)
        if index is None:
            return -1
        else:
            return self.values[index]

    def remove(self, key: int) -> None:
        index = self._search(key)
        if index is None:
            return
        del self.index[index]
        del self.values[index]


#   runtime: beats 78%
#   memory: beats 65%
class MyHashMap_ModuloListOfLists:

    def __init__(self):
        self.length = 2069
        self.data = [ [] for _ in range(self.length) ]

    def _search(self, key: int) -> Tuple[int, Optional[int]]:
        bucket_index = key % self.length
        for i, (k,v) in enumerate(self.data[bucket_index]):
            if key == k:
                return (bucket_index, i)
        return (bucket_index, None)

    def put(self, key: int, value: int) -> None:
        (index, subindex) = self._search(key)
        if subindex is None:
            self.data[index].append( (key,value) )
        else:
            self.data[index][subindex] = (key, value)

    def get(self, key: int) -> int:
        (index, subindex) = self._search(key)
        if subindex is None:
            return -1
        return self.data[index][subindex][1]

    def remove(self, key: int) -> None:
        (index, subindex) = self._search(key)
        if subindex is None:
            return
        del self.data[index][subindex]


#   runtime: beats 22%
#   memory: beats 30%
class MyHashMap_ModuloListCollisionHandler:

    def __init__(self):
        self.length = 2069
        self.data = [ [None,None] for _ in range(self.length) ]

    def _search(self, key: int) -> Optional[int]:
        bucket_index = key % self.length
        if self.data[bucket_index][0] == key:
            return bucket_index
        for i in range(bucket_index, self.length):
            if self.data[i][0] is None:
                return None
            if self.data[i][0] == key:
                return i
        for i in range(0, bucket_index):
            if self.data[i][0] is None:
                return None
            if self.data[i][0] == key:
                return i
        return None

    def _find_next_free(self, key: int) -> Optional[int]:
        bucket_index = key % self.length
        if self.data[bucket_index][0] is None:
            return bucket_index
        for i in range(bucket_index, self.length):
            if self.data[i][0] is None:
                return i
        for i in range(0, bucket_index):
            if self.data[i][0] is None:
                return i
        return None

    def _is_full(self):
        for i in range(self.length):
            if self.data[i][0] is None:
                return False
        return True

    def _grow(self):
        old_length = self.length
        old_data = self.data
        self.length = self.length * 2 + 1
        self.data = [ [None,None] for _ in range(self.length) ]
        for (k,v) in old_data:
            self.put(k,v)

    def put(self, key: int, value: int) -> None:
        index = self._search(key)
        if not index is None:
            self.data[index] = [key,value]
            return
        index = self._find_next_free(key)
        if not index is None:
            self.data[index] = [key,value]
            return
        self._grow()
        index = self._find_next_free(key)
        if not index is None:
            self.data[index] = [key,value]
            return
        else:
            raise UnreachableError()

    def get(self, key: int) -> int:
        index = self._search(key)
        if index is None:
            return -1
        if self.data[index][1] is None:
            return -1
        return self.data[index][1]

    def remove(self, key: int) -> None:
        index = self._search(key)
        if index is None:
            return
        self.data[index][1] = None


#   runtime: beats 57%
#   memory: beats 59%
class MyHashMap_ans_Bucket:

    def __init__(self):

        class Bucket:
            def __init__(self):
                self.bucket = []
            def get(self, key):
                for (k, v) in self.bucket:
                    if k == key:
                        return v
                return -1
            def update(self, key, value):
                found = False
                for i, kv in enumerate(self.bucket):
                    if key == kv[0]:
                        self.bucket[i] = (key, value)
                        found = True
                        break
                if not found:
                    self.bucket.append((key, value))
            def remove(self, key):
                for i, kv in enumerate(self.bucket):
                    if key == kv[0]:
                        del self.bucket[i]

        self.key_space = 2069
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key, value):
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key, value)

    def get(self, key):
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key):
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)


def run_solution(c, ops, vals):
    assert len(ops) == len(vals)
    assert issubclass(c, object)
    s = c()
    result = []
    for action, loop_vals in zip(ops, vals):
        loop_result = None
        if action == "put":
            assert len(loop_vals) == 2
            s.put(loop_vals[0], loop_vals[1])
        elif action == "get":
            assert len(loop_vals) == 1
            loop_result = s.get(loop_vals[0])
        elif action == "remove":
            assert len(loop_vals) == 1
            s.remove(loop_vals[0])
        result.append(loop_result)
    return result

test_classes = [ MyHashMap_wrapper, MyHashMap_naive, MyHashMap_ModuloListOfLists, MyHashMap_ModuloListCollisionHandler, MyHashMap_ans_Bucket, ]

inputs = [ (["put","put","get","get","put","get","remove","get"],[[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]), ]
checks = [ [None,None,1,-1,None,1,None,-1] ]
assert len(inputs) == len(checks), "input/check lists length mismatch"
assert len(inputs) > 0, "No input"

for c in test_classes:
    print(c.__name__)
    start_time = time.time()
    for (ops, vals), check in zip(inputs, checks):
        print(f"ops=({ops}), vals=({vals})")
        result = run_solution(c, ops, vals)
        print(f"result=({result})")
        assert result == check, "Check comparison failed"
    print("elapsed_us=(%0.2f)" % ((time.time() - start_time) * 1_000_000))
    print()

