def single_root_words(root_word,  *other_words):
    same_words = []
    for word in other_words:
        str1 = word.upper()
        str2 = root_word.upper()
        if ( str1 in str2) or (str2 in str1):
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)