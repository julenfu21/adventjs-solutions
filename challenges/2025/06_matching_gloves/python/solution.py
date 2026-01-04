from collections import defaultdict
from typing import List, Dict

def match_gloves(gloves: List[Dict[str, str]]) -> List[str]:
    # Code here
    gloves_per_hand = defaultdict(lambda: defaultdict(int))
    matched_gloves = []

    for glove in gloves:
        hand = glove["hand"]
        color = glove["color"]
        gloves_per_hand[color][hand] += 1

        if gloves_per_hand[color]['L'] >= 1 and gloves_per_hand[color]['R'] >= 1:
            matched_gloves.append(color)
            gloves_per_hand[color]['L'] -= 1
            gloves_per_hand[color]['R'] -= 1

    return matched_gloves
