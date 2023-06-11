def merge_words(word1, word2):
    merged = ''
    length1 = len(word1)
    length2 = len(word2)
    max_length = max(length1, length2)

    for i in range(max_length):
        if i < length1:
            merged += word1[i]
        if i < length2:
            merged += word2[i]

    return merged


# example

word_1 = 'abcde'
word_2 = 'xyz'

result = merge_words(word_1, word_2)
print(result)   # result = 'axbyczde'
