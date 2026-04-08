#  Lien de la consigne : https://rmechety.notion.site/Enonc-du-TP-Jeu-Vid-o-en-Python-avec-MongoDB-182c6c9d3d2080fd958bf1d1ad7b2ca5
import random
from time import *
# Initialiser la base de données


def afficher_header(titre:str):
    print("-" * 23)
    print(titre.center(23))
    print("-"*23)

def afficher_menu():
    # Vider le terminal

    # Afficher mon en-tête
    titre = "JEU DE COMBAT"
    afficher_header(titre)
    # Afficher les choix possibles
    print("1. Démarrer une nouvelle partie")
    print("2. Voir les 3 meilleurs scores")
    print("3. Quitter")



def creer_equipe():    
    personnages = {
        "Guerrier" : {"ATK": 15, "DEF": 10, "PV": 100},
        "Mage" : {"ATK": 20, "DEF": 5, "PV": 80},
        "Archer" : {"ATK": 18, "DEF": 7, "PV": 90},
        "Voleur" : {"ATK": 22, "DEF": 8, "PV": 85},
        "Paladin" : {"ATK": 14, "DEF": 12, "PV": 110},
        "Sorcier" : {"ATK": 25, "DEF": 3, "PV": 70},
        "Chevalier" : {"ATK": 17, "DEF": 15, "PV": 120},
        "Moine" : {"ATK": 19, "DEF": 9, "PV": 95},
        "Berserker" : {"ATK": 23, "DEF": 6, "PV": 105},
        "Chasseur" : {"ATK": 16, "DEF": 11, "PV": 100}
    }
    
    # Print les personnages et en choisir 3
    print("Voici les personnages disponibles:")
    for nom, stats in personnages.items():
        print(nom,":",stats)
        sleep(0.1)
    print("Choisissez-en 3")

    # Création de l'équipe
    equipe = {}
    for i in range(3):
        print("Choisissez le membre ", i+1)
        choix = input()

        if choix not in personnages:
            while choix not in personnages:
                print("Ce personnage n'existe pas. Choississez en un autre")
                choix = input()

        # equipe[name] = stats
        equipe[choix] = personnages[choix]
        del personnages[choix]

    # Afficher tous les personnages et leurs stats
    print("Voici votre équipe !")
    for nom, stats in equipe.items():
        print(nom,":",stats)
    
    return equipe



def tour(equipe, index, life_state, ennemi):
    # chaque personne de l'équipe tape le monstre avec atk du perso - def de l'ennemi
    for membre in index:
        degats =  equipe[membre]["ATK"] - ennemi[1]["DEF"]
        if degats > 0:
            print(membre, " attaque ", ennemi[0], " de ", degats, " points ")
            ennemi[1]["PV"] -= degats
            print("Le", ennemi[0], "a", ennemi[1]["PV"], "PVs !")
            sleep(0.1)
    # L'ennemi attaque un membre random avec atk monstre - def perso
    victime = random.choice(index)
    print(ennemi[0], "attaque ", victime, "!")
    equipe[victime]["PV"] -= ennemi[1]["ATK"] - equipe[victime]["DEF"]
    sleep(0.1)

    if equipe[victime]["PV"] < 1:
        print(victime, "est vaincu !")
        life_state -= 1
        del equipe[victime]
        sleep(0.1)
        
        if len(index) == 1:
            index.pop(0)
            print("Défaite !")
            return life_state
        
        index.remove(victime)

    return life_state


def lancer_vagues(equipe):
    enemy_list = {
        "Gobelin" : {"ATK": 10, "DEF": 5, "PV": 50},
        "Orc" : {"ATK": 20, "DEF": 8, "PV": 120},
        "Dragon" : {"ATK": 30, "DEF": 20, "PV": 200},
        "Zombie" : {"ATK": 12, "DEF": 6, "PV": 70},
        "Troll" : {"ATK": 25, "DEF": 15, "PV": 200},
        "Spectre" : {"ATK": 18, "DEF": 10, "PV": 100},
        "Golem" : {"ATK": 28, "DEF": 25, "PV": 200},
        "Vampire" : {"ATK": 22, "DEF": 12, "PV": 150},
        "Loup-garou" : {"ATK": 25, "DEF": 18, "PV": 180},
        "Squelette" : {"ATK": 15, "DEF": 7, "PV": 90}
    }

    life_state = 3
    # Initialisation de l'équipe avec une liste pour répertorier les noms en index
    index_equipe = []
    for nom in equipe.keys():
        index_equipe.append(nom)

    i = 0       # initialisation du compteur de vague
    # vague avec une condition de vie de l'équipe genre 
    while life_state > 0:
        ennemi = list(random.choice(list(enemy_list.items())))[:]       # On choisit un ennemi random de la liste
        print("")
        print("-" * 75)
        print("Début de la vague ", i+1, ": ", ennemi)     # On imprime l'ennemi et ses stats sous forme de liste 
        print("-" * 75)
        print("")

        sleep(1)
        # Une vague c'est pour un ennemi, un tour c'est un round de taper l'ennemi et après c'est lui qui te tape
        # Tour
        while ennemi[1]["PV"] > 0 :
            resultats = tour(equipe, index_equipe, life_state, ennemi)
            
            life_state = resultats
            if life_state == 0:
                break
            sleep(0.2)
        # sortie du while
        i+=1    # Compteur de vagues, augmente à chaque fin de vague pour la confirmer
        if life_state > 0:
            print("Victoire !") 
            sleep(0.3)
    
    # sortie du while, life_state à 0
    return i



def terminer_combat(username, score):
    print("Félicitations,", username, "! Vous avez tenu pendant", score, "vague(s) !")
    # envoyer le score et le nom associé à la db




def main():
    # Afficher le menu
    afficher_menu()
    choice=input()
    if choice not in ('1', '2'):
        return
    #elif choice == 2:

    username=input("Entrez votre nom d'utilisateur : ")
    # Créer mon équipe
    
    equipe = creer_equipe()
    sleep(1)

    # Démarrer les vagues de combat
    print("Lancement du combat !")
    score=lancer_vagues(equipe)

    # Terminer le combat et stocker le score
    terminer_combat(username, score)



main()
