def new_player(p_pool, p_pos, p_skill, pl, pos, sk):
    p_pool[player] = []
    p_pool[player].append([pos, sk])
    p_pos[position].append(pl)
    p_skill[player] = 0
    p_skill[player] += sk
    return p_pool, p_pos, p_skill


def existing_player(p_pool, p_pos, p_skill, pl, pos, sk):
    for key, value in p_pool.items():
        if key == pl:
            res = any(pos in sublist for sublist in value)
            if res:
                for el in value:
                    if pos in el:
                        if el[1] < sk:
                            p_skill[pl] -= el[1]
                            p_skill[pl] += sk
                            el[1] = sk
            else:
                p_pool[player].append([pos, sk])
                p_pos[position].append(pl)
                p_skill[player] += sk
    return p_pool, p_pos, p_skill


def player_remover(p_pool, p_skill, p_pos, r_player):
    del p_pool[r_player]
    del p_skill[r_player]
    for key, value in p_pos.items():
        if r_player in p_pos[key]:
            p_pos[key].remove(r_player)
    return p_pool, p_pos, p_skill


player_pool = {}
player_skill = {}
player_pos = {}

while True:
    receive = input()
    if receive == "Season end":
        break

    if " -> " in receive:
        player, position, skill = receive.split(" -> ")
        skill = int(skill)

        if position not in player_pos:
            player_pos[position] = []

        if player not in player_pool:
            player_pool, player_pos, player_skill = new_player(player_pool, player_pos, player_skill, player, position,
                                                               skill)
        else:
            player_pool, player_pos, player_skill = existing_player(player_pool, player_pos, player_skill, player,
                                                                    position, skill)

    elif " vs " in receive:
        player_one, player_two = receive.split(" vs ")
        if player_one in player_pool and player_two in player_pool:
            for pos, pl in player_pos.items():
                if player_one in player_pos[pos] and player_two in player_pos[pos]:
                    if player_skill[player_one] > player_skill[player_two]:
                        player_pool, player_pos, player_skill = player_remover(player_pool, player_skill, player_pos,
                                                                               player_two)
                    elif player_skill[player_one] < player_skill[player_two]:
                        player_pool, player_pos, player_skill = player_remover(player_pool, player_skill, player_pos,
                                                                               player_one)

player_skill = dict(sorted(player_skill.items(), key=lambda x: (-x[1], x[0])))
for key, value in player_skill.items():
    print(f"{key}: {player_skill[key]} skill")
    for k, v in player_pool.items():
        if k == key:
            player_pool[k].sort(key=lambda x: (-x[1], x[0]))
            for el in player_pool[k]:
                print(f"- {el[0]} <::> {el[1]}")
