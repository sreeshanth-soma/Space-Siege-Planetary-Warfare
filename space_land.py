import random
while True:
    choice = input(
        "What would you like to do? 1) Fight in space🚀 against the Land Army, 2) Fight on land⚔️⚔ against the Space "
        "Army, or 3) Quit: ")
    if choice == "3":
        print("Bye!")
        break
    elif choice == "1":
        my_hp = 100
        shogun_hp = random.randint(100, 150)
        spaceship_type = input(
            "Choose your spaceship: 1) The Cobra⚡️ (bursts lasers) or 2) The Inferno🗼 (continuous laser beams): ")
        print("The shogun on the land has " + str(shogun_hp) + "hp and is planning to attack you.")
        if spaceship_type == "1":
            while my_hp > 0 and shogun_hp > 0:
                print("\nYour HP:", my_hp)
                print("Shogun's HP:", shogun_hp)
                action = input("What will you do? 1) Use shield🛡️ or 2) Attack directly⚔️? ")
                if action == "1":
                    shield = random.randint(1, 2)
                    if shield == 1:
                        print("You have a diamond shield🛡️ with 150hp.")
                        my_hp += shield
                    else:
                        print("You have a titanium shield🛡️ with 100hp.")
                        my_hp += shield
                elif action == "2":
                    damage = random.randint(50, 70)
                    print("You dealt " + str(damage) + "hp damage.")
                    shogun_hp -= damage
                if shogun_hp <= 0:
                    print("Congratulations! You destroyed the shogun's spaceship🏆!")
                    break
                else:
                    print("Oh no, the shogun noticed you.")
                    shogun_move = random.randint(25, 30)
                    print("They retreated to a safe place and recovered " + str(shogun_move) + "hp.")
                    shogun_hp += shogun_move
                if my_hp <= 0:
                    print("Oh no! Your spaceship was destroyed by the shogun.🏳️🏳️")
                    break
        elif spaceship_type == "2":
            print("You've chosen The Inferno spaceship🚀.")
            enemy_encounters = 3
            enemies_defeated = 0
            while enemies_defeated < enemy_encounters and my_hp > 0:
                print("\nYour HP:", my_hp)
                print("Enemy Encounter:", enemies_defeated + 1, "/", enemy_encounters)
                enemy_hp = random.randint(80, 120)
                print("An enemy spaceship approaches with " + str(enemy_hp) + "hp.")
                while my_hp > 0 and enemy_hp > 0:
                    print("\nYour HP:", my_hp)
                    print("Enemy HP:", enemy_hp)
                    action = input("What will you do? 1) Fire laser beams⚡️, 2) Evade enemy attacks🛡️, or 3) Quit: ")
                    if action == "3":
                        print("Exiting the game. Goodbye!")
                        exit()
                    if action == "1":
                        damage = random.randint(60, 80)
                        print("You fired your Inferno's laser beams, dealing " + str(damage) + " damage!")
                        enemy_hp -= damage
                    elif action == "2":
                        evasion_chance = random.random()
                        if evasion_chance > 0.3:
                            print("You successfully evaded the enemy's attacks!")
                        else:
                            print("Your evasion failed, and you took damage!")
                            damage_taken = random.randint(20, 40)
                            my_hp -= damage_taken
                            print("You've taken " + str(damage_taken) + " damage!")
                    if enemy_hp <= 0:
                        print("You destroyed the enemy spaceship!🏆")
                        enemies_defeated += 1
                        break
                    elif my_hp <= 0:
                        print("Your spaceship has been destroyed. Game Over!🏳️🏳️")
                        break
            if enemies_defeated == enemy_encounters:
                print("Congratulations! You've defeated all enemy fleets and completed your adventure!🏆")
    elif choice == "2":
        my_hp = 100
        spaceship_hp = random.randint(100, 150)
        shogun_weapon = input("Choose your weapon 1) Lightning Polearm Spear𐃆 2) Yoru - The Black Sword🗡️")
        if shogun_weapon == "1":
            while my_hp > 0 and spaceship_hp > 0:
                a = input("1) Call Reinforces🥷🏻🥷🏻 or 2) Evolve to next level and attack🧌")
                if a == "1":
                    damage_taken = random.randint(20, 40)
                    print("You have taken " + str(damage_taken) + " damage and wait till the reinforcements come")
                    my_hp -= damage_taken
                elif a == "2":
                    damage = random.randint(30, 50)
                    print("You evolved to the next level and attacked with a powerful strike, dealing " + str(
                        damage) + " damage!")
                    spaceship_hp -= damage
                if spaceship_hp <= 0:
                    print("Congratulations! You have destroyed the enemy spaceship!🏆")
                    break
                else:
                    print("The enemy spaceship retaliates!")
                    enemy_damage = random.randint(25, 35)
                    print("You've taken " + str(enemy_damage) + " damage from the enemy's counterattack!")
                    my_hp -= enemy_damage
                if my_hp <= 0:
                    print("Your spaceship has been destroyed🏳️🏳️. Game Over!")
                    break
        else:
            while my_hp > 0 and spaceship_hp > 0:
                action = input("What would you like to do? 1) Slashing Terror 2) Black Thunder")
                if action == "1":
                    damage = random.randint(35, 55)
                    spaceship_hp -= damage
                    if spaceship_hp <= 0:
                        print("Congratulations! You have destroyed the Spaceship!🏆")
                        break
                    else:
                        print("You gave a massive damage of " + str(damage))
                    damage_taken = random.randint(20, 25)
                    if my_hp > 0:
                        my_hp -= damage_taken
                        print("Enemy gave you " + str(damage_taken) + " of damage")
                    else:
                        print("You have been destroyed by the spaceship, sorry!🏳️🏳️")
                        break
                elif action == "2":
                    thunder = random.randint(40, 50)
                    spaceship_hp -= thunder
                    if spaceship_hp <= 0:
                        print("Congratulations! You have destroyed the Spaceship!🏆")
                    else:
                        print("The thunder gave a damage of " + str(thunder))
                    print("oh no, you have been spotted and nearer to the enemy")
                    enemy_damage = random.randint(50, 55)
                    my_hp -= enemy_damage
                    if my_hp <= 0:
                        print("You have been destroyed by the spaceship, sorry!🏳️")
                    else:
                        print("You got a massive damage of " + str(enemy_damage) + " because he got nearer to you")
    else:
        print("Invalid choice. Please select 1, 2, or 3 to quit.")