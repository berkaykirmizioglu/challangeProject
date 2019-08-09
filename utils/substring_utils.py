from pip._vendor.msgpack.fallback import xrange


def longest_unique_substring(text):
    n = len(text)
    current = 1
    max_len = 1
    total_chars = 256

    controlled_char = [-1] * total_chars

    controlled_char[ord(text[0])] = 0

    for i in xrange(1, n):
        previous_index = controlled_char[ord(text[i])]

        if previous_index == -1 or (i - current > previous_index):
            current += 1
        else:
            if current > max_len:
                max_len = current
            current = i - previous_index

        controlled_char[ord(text[i])] = i

    if current > max_len:
        max_len = current

    return max_len
