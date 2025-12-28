def elf_battle(elf1: str, elf2: str) -> int:

    def attack_other_player(
        p1_move: str,
        p2_move: str,
        p2_hp: int
    ) -> int:
        damage = 0

        if p1_move == 'A' and p2_move != 'B':
            damage = 1

        if p1_move == 'F':
            damage = 2

        return p2_hp - damage

    def has_player_lost(player_hp: int) -> bool:
        return player_hp <= 0

    # Code here
    elf1_hp = 3
    elf2_hp = 3
    battle_output = -1

    for elf1_round, elf2_round in zip(elf1, elf2):
        # Compute new HP values after round
        elf1_hp = attack_other_player(
            p1_move=elf2_round,
            p2_move=elf1_round,
            p2_hp=elf1_hp
        )
        elf2_hp = attack_other_player(
            p1_move=elf1_round,
            p2_move=elf2_round,
            p2_hp=elf2_hp
        )

        has_elf1_lost = has_player_lost(player_hp=elf1_hp)
        has_elf2_lost = has_player_lost(player_hp=elf2_hp)
        if has_elf1_lost and has_elf2_lost:
            return 0

        if has_elf1_lost:
            return 2

        if has_elf2_lost:
            return 1

    if elf1_hp > elf2_hp:
        return 1

    if elf2_hp > elf1_hp:
        return 2

    return 0
