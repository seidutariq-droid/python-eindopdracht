monster_health = 150
player_damage = 25
attack_count = 0

while monster_health > 0:
    attack_count += 1
    monster_health -= player_damage
    print(f"De monster heeft nog {monster_health} HP over.")
print(f"Hij heeft het monster {attack_count} aangevallen.")


monsters_health = [100, 125, 150]
attack_count = 0

for health in monsters_health:
    print(f"Ik zie een monster met {health} health")
    while health > 0:
        health -= player_damage
        attack_count += 1
        if health == 0:
            print(f"Je hebt het monster verslagen en je hebt hem {attack_count} keer aangevallen.")
            attack_count = 0
        else:
            print(f"Je hebt hem aangevallen hij heeft nog {health} health over.")