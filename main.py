import random
import sys 

health_player = 50
health_ennemy = 50
inter_ligne = ("-" * 50)
next_level = False
number_potion_health = 3
up_round = False

while True:

    potion_helth = random.randint(15, 20)
    attack_player = random.randint(5, 10)
    attack_ennemy = random.randint(5, 15)

    user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")


    while up_round == False:
        if user_choice == "1": #attack_player
            health_ennemy = health_ennemy - attack_player
            print(f"Vous avez infligé {attack_player} points de dégats à l'ennemi")
            next_level = True
            up_round = False
            break


        elif user_choice == "2": #potion
            number_potion_health = number_potion_health - 1

            if number_potion_health < 0:
                print("Vous n'avez plus de potions")
                next_level = False
                print(inter_ligne)
                up_round = False
                break

            if number_potion_health >= 0 :
                health_player = health_player + potion_helth
                print(f"Vous récupérez {potion_helth} points de vie ({number_potion_health} restantes)")
                next_level = True
                up_round = True
                break
            
        else: 
            print("Veuillez entrer un choix valide")
            print(inter_ligne)
            next_level = False
            up_round = False
            break

    if next_level == True :
        health_player = health_player - attack_ennemy
        print(f"L'ennemi vous a infligé {attack_ennemy} points de dégats")
        print(f"Il vous reste {health_player} points de vie.")
        print(f"Il reste {health_ennemy} points de vie a l'ennemi.")
        print(inter_ligne)
