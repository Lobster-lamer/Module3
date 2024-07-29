def single_root_words(root_word: str,
                      *other_words,
                      root_in_words: bool = True) -> list:
    same_words = []
    root_word = root_word.lower()
    if root_in_words:
        for word in other_words:
            if root_word in word.lower():
                same_words.append(word)
    else:
        for word in other_words:
            if word.lower() in root_word:
                same_words.append(word)

    return same_words


if __name__ == "__main__":
    print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
    print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel',
                            root_in_words=False))
