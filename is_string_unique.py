# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# ASCII string or a Unicode string? One solution is to create an array of boolean values, where the flag
# at index i indicates whether character i in the alphabet is contained in the string. The second time you see
# this character you can immediately return false. We can also immediately return false if the string length
# exceeds the number of unique characters in the alphabet.

# import argparse
import time
import unittest
from collections import defaultdict


def without_extra_ds(sti):
    for i in range(len(sti)):
        for j in range(i+1, len(sti)):
            if sti[i] == sti[j]:
                return False
    return True

def pythonic(sti):
    return len(set(sti)) == len(sti)

def using_set(sti):
    characters_seen = set()
    for char in sti:
        if char in characters_seen:
            return False
        characters_seen.add(char)
    return True

def using_sorting(string: str) -> bool:
    sorted_string = sorted(string) #takes O(nlogn)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True

def using_dictionary(string: str) -> bool:
    character_counts = {}
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
    return True

def assuming_ASCII_128(sti):
    if len(sti) > 128:
        return False
    char_set = [False] * 128
    for char in sti:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True
    return True

def bit_vector_ASCII_128(string):
    """Uses bitwise operation instead of extra data structures."""
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False
    checker = 0
    for c in string:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True

class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        without_extra_ds,
        pythonic,
        using_set,
        using_sorting,
        using_dictionary,
        assuming_ASCII_128,
        bit_vector_ASCII_128
    ]

    def test_is_unique(self):
        num_runs = 1000
        save_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for sample_input, sample_output in self.test_cases:
                for a_function in  self.test_functions:
                    start = time.perf_counter()
                    assert a_function(sample_input) == sample_output \
                        , f"{a_function.__name__} failed for value: {sample_input}"
                    save_runtimes[a_function.__name__] += (time.perf_counter() - start) * 1000

        print(f"{num_runs} runs completed.")
        for a_function, a_runtime in save_runtimes.items():
            print(f"{a_function}: {a_runtime:.1f} ms")


if __name__ == '__main__':
    # argv = argparse.ArgumentParser()
    # argv.add_argument('string', type=str)
    # args = argv.parse_args()
    # sti = args.string
    # print(without_extra_ds(sti))
    unittest.main()
