def string_soup(ingredient: str) -> str:
    words = list(ingredient)
    words.sort()

    return "".join(words)

print(string_soup("hello"))