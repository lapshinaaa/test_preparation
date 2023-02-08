from collections import Counter


def longest_k_substr(s, k) -> int:
    length_string = len(s)
    max_length = -1

    for char in range(length_string):
        for next_char in range(char + 1, length_string + 1):
            characters = list(s[char:next_char])
            counter_of_elements = Counter(characters)  # counting the occurrence of each character (letter)

            counter_of_less = 0  # to check if we have any values that occur fewer than k times
            for value in counter_of_elements.values():   # checking if all the values >= k
                if value < k:
                    counter_of_less += 1

            current_length = len(characters)
            if current_length > max_length and counter_of_less == 0:
                max_length = current_length

    return max_length


length, k = map(int, input().split())
s = str(input())

# Function Call
print(longest_k_substr(s, k))
