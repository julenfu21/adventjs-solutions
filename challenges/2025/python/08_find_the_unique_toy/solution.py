from collections import defaultdict

def find_unique_toy(toy: str) -> str:
    # Code here
    character_frequencies = defaultdict(int)

    # Get frequency for each character
    for character in toy:
        character_frequencies[character.lower()] += 1

    # Get first unique character
    for character in toy:
        if character_frequencies[character.lower()] == 1:
            return character

    return ''
