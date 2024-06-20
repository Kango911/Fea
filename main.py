def compress_string(s):
    if not s:
        return ""

    compressed = []
    count = 1
    previous_char = s[0]

    for char in s[1:]:
        if char == previous_char:
            count += 1
        else:
            compressed.append(f"{count}{previous_char}")
            previous_char = char
            count = 1

    compressed.append(f"{count}{previous_char}")

    return ''.join(compressed)


# Пример использования
input_string = input(f'Введите значение:\n')
compressed_string = compress_string(input_string)
print(compressed_string)
