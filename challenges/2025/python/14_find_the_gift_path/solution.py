def find_gift_path(workshop: dict, gift: str | int | bool) -> list[str]:

    def traverse_workshop(
        storing_unit: dict,
        gift: str | int | bool,
        keys: list | None = None
    ) -> list:
        if keys is None:
            keys = []

        for key, value in storing_unit.items():
            if isinstance(value, dict):
                new_keys = keys.copy()
                new_keys.append(key)
                result = traverse_workshop(storing_unit=value, gift=gift, keys=new_keys)
                if result:
                    return result
            else:
                if value == gift:
                    keys.append(key)
                    return keys

        return []

    # Code here
    return traverse_workshop(storing_unit=workshop, gift=gift)
