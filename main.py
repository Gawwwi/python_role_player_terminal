import random
import sys 

health_player = 50
health_ennemy = 50
number_potion_health = 3
next_level = False
up_round = False
relaunch_s = False
start = True
INTER_LIGNE = ("-" * 50)



def launch(start, INTER_LIGNE):

    while True:
        print(INTER_LIGNE)
        start_choice = input("Voulez vous lancer le jeu ?\nEntrer 1 pour jouer, ou 2 pour ne pas jouer : ")
        
        while start == True:

            if start_choice == "1":
                print("Vous lancez le jeu.")
                print(INTER_LIGNE)
                game(health_player, health_ennemy, number_potion_health, next_level, up_round, relaunch_s, INTER_LIGNE)

            elif start_choice == "2":
                print(INTER_LIGNE)
                print("Vous ne voulez pas lancer le jeu.")
                print(INTER_LIGNE)
                sys.exit(0)

            else:
                print("Veuillez entrer un choix valide.")
                break

def regle (INTER_LIGNE):
    print("""Voici les règles du jeu : 
-Le jeu comporte deux joueurs : vous et un ennemi.
-Vous commencez tous les deux avec 50 points de vie.
-Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie.
-L'ennemi ne dispose d'aucune potion.
-Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50.
-Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie.
-L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie.
-Lorsque vous utilisez une potion, vous passez le prochain tour.
          
Note :

À chaque tour, vous attaquez en premier. Il ne peut donc pas y avoir de match nul. Si lorsque vous attaquez, votre attaque fait descendre les points de vie de l'ennemi en dessous (ou égal à) 0, vous gagnez la partie sans que l'ennemi n'ait le temps de vous attaquer en retour.""")
    print(INTER_LIGNE)


def relaunch(relaunch_s, INTER_LIGNE):

    while True:

        relaunch_choice = input("Souhaitez vous rejouer ?\nEntrer 1 pour rejouer, ou 2 pour quitter le jeu : ")

        while relaunch_s == True:

            if relaunch_choice == "1":
                print("Vous venez de relancer la partie.")
                print(INTER_LIGNE)
                game(health_player, health_ennemy, number_potion_health, next_level, up_round, relaunch_s, INTER_LIGNE)
            
            elif relaunch_choice == "2":
                print("Vous quitter le jeu.")
                print(INTER_LIGNE)
                sys.exit()

            else:
                print("Veuillez entrer un choix valide.")
                print(INTER_LIGNE)
                break


def game(health_player, health_ennemy, number_potion_health, next_level, up_round, relaunch_s, INTER_LIGNE):

    regle(INTER_LIGNE)

    while True:

        potion_health = random.randint(15, 50)
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

                if number_potion_health < 0: #plus de potion

                    print("Vous n'avez plus de potions")
                    print(INTER_LIGNE)
                    next_level = False
                    up_round = False
                    break

                elif number_potion_health >= 0: #utilisation potion

                    health_player = health_player + potion_health
                    print(f"Vous récupérez {potion_health} points de vie ({number_potion_health} restantes)")
                    next_level = True
                    up_round = True
                    break

                else: #gestion erreur

                    print("Veuillez entrer un choix valide")
                    print(INTER_LIGNE)
                    next_level = False
                    up_round = False
                    break
                
            else: #gestion erreur

                print("Veuillez entrer un choix valide")
                print(INTER_LIGNE)
                next_level = False
                up_round = False
                break

        if next_level == True: #Passez au prochain niveau

            health_player = health_player - attack_ennemy
            print(f"L'ennemi vous a infligé {attack_ennemy} points de dégats")
            print(f"Il vous reste {health_player} points de vie.")
            print(f"Il reste {health_ennemy} points de vie a l'ennemi.")
            print(INTER_LIGNE)

        if up_round == True and next_level == True: #Quand potion utilisé

            health_player = health_player - attack_ennemy
            print("Vous passez votre tour ...")
            print(f"L'ennemi vous a infligé {attack_ennemy} points de dégats")
            print(f"Il vous reste {health_player} points de vie.")
            print(f"Il reste {health_ennemy} points de vie a l'ennemi.")
            print(INTER_LIGNE)

            up_round = False

        if health_ennemy <= 0: #WIN
            print("Vous avez gagné")
            print(INTER_LIGNE)

            relaunch_s = True
            #relaunch_choice = input("1, rejouer. 2, quitter")
            relaunch(relaunch_s, INTER_LIGNE)
        
        elif health_player <= 0: #LOOSE
            print("Tu as perdu")
            print(INTER_LIGNE)

            relaunch_s = True
           # relaunch_choice = input("1, rejouer. 2, quitter")
            relaunch(relaunch_s, INTER_LIGNE)


launch(start, INTER_LIGNE)