def manufacture_gifts(gifts_to_produce: list[dict[str, int]]) -> list[str]:
    # Code here
    gifts = []

    for gift in gifts_to_produce:
        gift_quantity = gift['quantity']
        if gift_quantity <= 0:
            continue

        gifts += [gift['toy'] for i in range(gift_quantity)]

    return gifts
