from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss
import random
import os
import time

player_list=[]
def main_menu():
    os.system('cls')
    print("==============================")
    print("= A R C A N E  L I N E A G E =")
    print("==============================")
    print("\n")
    print("Select a Mode:")
    print("\t1. Single Player")
    print("\t2. Player VS Player")
    print("\t3. Leaderboard")
    print("\t4. Exit")
    
    i=1
    while i != 0:
        choice = int(input("||"))
        if choice == 1:
            os.system('cls')
            singleplayer()
        elif choice == 2:
            os.system('cls')
            pvp()
        elif choice == 3 and len(player_list) != 0:
            os.system('cls')
            
            print("Username\t||SP Wins\t||PvP Wins\n\n")
            for elem in player_list:
                print(f"{elem.getUsername()}\t||{elem.getSPWins()}\t||{elem.getPVPWins()}")
            wait = input("Press Enter key to return to main menu")
            main_menu()
        elif choice == 3 and len(player_list) == 0:
            os.system('cls')
            print("No souls registered yet.")
            continue
        elif choice == 4:
            os.system('cls')
            print("\nThanks for Playing!")
            time.sleep(3)
            break
        else:
            print("Invalid Choice")
            continue
        
def action_menu(mode, character):
    i = 0
    while i!=1:
        print("\nChoose an option:\n")
        time.sleep(0.3)
        print("1. ATTACK")
        if mode == 1:
            print("")
            print("2. RUN")
            time.sleep(0.3)
        choice = int(input("||"))
        if choice > 2 and mode!= 1:
            print("Invalid Input!")
        elif 0<choice<3:
            return choice
        else:
            print("Invalid Input!")
            continue
        
def battle_menu(x):
    print("\nChoose an Attack:\n")
    if isinstance(x, Swordsman):
        print("1. Basic Attack")
        print("2. Slash Attack")
        choice = int(input("||"))
        i = 1
        while i != 0:
            if choice==1:
                return 1
            elif choice==2:
                return 2
            else:
                print("Invalid Input!")
                continue
    elif isinstance(x, Archer):
        print("1. Basic Attack")
        print("2. Ranged Attack")
        i = 1 
        while i != 0:
            choice = int(input("||"))
            if choice==1:
                return 1
            elif choice == 2:
                return 3
            else:
                print("Invalid Input!")
                continue
    elif isinstance(x, Magician):
        print("1. Basic Attack")
        print("2. Magic Attack")
        print("3. Heal")
        i = 1 
        while i != 0:
            choice = int(input("||"))
            if choice==1:
                return 1
            elif choice==2:
                return 4
            elif choice==3:
                return 5
            else:
                print("Invalid Input!")
                continue
    elif isinstance(x, Novice):
        print("1. Basic Attack")
        i = 1 
        while i != 0:
            choice = int(input("||"))
            if choice==1:
                return 1
            else:
                print("Invalid Input!")
                continue
        
def battle(attack, player1, player2):
    if attack == 1:
        player1.basicAttack(player2)
    elif attack == 2:
        player1.slashAttack(player2)
    elif attack == 3:
        player1.rangedAttack(player2)
    elif attack == 4:
        player1.magicAttack(player2)
    elif attack == 5:
        player1.heal()
        
def battle_status(player, enemy):
    print("==============================")
    time.sleep(0.3)
    print(f"{enemy.getUsername()}: {enemy.getHp()} / {enemy.getMaxHp()}")
    time.sleep(0.3)
    print("\t\tVS")
    time.sleep(0.3)
    print(f"{player.getUsername()}: {player.getHp()} / {player.getMaxHp()}")
    time.sleep(0.3)
    print("==============================")
    time.sleep(0.3)
    
def encounter(player, enemy, mode):
    os.system('cls')
    if mode == 1:
        print(f"{enemy.getUsername()} approaches you!\n")
        time.sleep(2)
        print("\tEncounter start!")
        time.sleep(2)
    else:
        print(f"\nThe match between {player.getUsername()} and {enemy.getUsername()} is about to begin!")
        time.sleep(3)
    i=0
    turn=0
    battle_status(player, enemy)
    while player.getHp() > 0 and enemy.getHp() > 0:
        turn = random.randint(0,1)
        if turn == 0:
            print(f"{player.getUsername()}'s turn!\n")
            action = action_menu(mode, player)
            if action == 1:
             PlayerAttack = battle_menu(player)
             os.system('cls')
             battle(PlayerAttack, player, enemy)
             time.sleep(0.3)
             print("\t\tOutcome:")
             battle_status(player, enemy)
             continue
            if action == 2:
                if random.randint(0,10) > 3:
                    os.system('cls')
                    print("Successfully ran away!")
                    player.restoreHp()
                    break
                else:
                    os.system('cls')
                    print("Failed to run away!")
                    continue
        if mode == 1:
            if turn == 1:
                print (f"{enemy.getUsername()}'s turn!\n")
                time.sleep(1)
                EnemyAttack = enemy.attackPattern[i]
                battle(EnemyAttack, enemy, player)
                i += 1
                if i == 8:
                    i = 0
            time.sleep(0.3)
            print("\t\tOutcome:")
            battle_status(player, enemy)
        if mode == 2:
            if turn == 1:
                print(f"{enemy.getUsername()}'s turn!\n")
                action = action_menu(mode, enemy)
                os.system('cls')
                if action == 1:
                    EnemyAttack = battle_menu(enemy)
                    os.system('cls')
                    battle(EnemyAttack, enemy, player)
                    time.sleep(0.3)
                    print("\t\tOutcome:")
                    os.system('cls')
                    continue
    if player.getHp() <= 0:
        player.restoreHp()
        enemy.restoreHp()
        return 0
    elif enemy.getHp() <= 0:
        player.restoreHp()
        enemy.restoreHp()
        return 1

def singleplayer():
    os.system('cls')
    print("===========================")
    print("= S I N G L E P L A Y E R =")
    print("===========================")
    
    i = 0
    while i != 1:
        print("Choose an option:")
        print("\n\n\t1. Create a New Soul")
        print("\t2. Returning Soul")
        print("\t3. Main Menu")
        choice = int(input("||"))
        if choice == 1:
            os.system('cls')
            username = str(input("\n\nEnter the soul's name: "))
            player_list.append(Novice(username))
            player = player_list[-1]
            print(f"\n\nWelcome {player.getUsername()}!")
            print("Your journey awaits.")
            break
        elif choice == 2 and len(player_list) != 0:
            i = 1
            print("Choose a save file:")
            for elem in player_list:
                print(f"{i},", elem.getUsername())
                i += 1
            load = int(input("||"))
            if 0 < load <= len(player_list):
                player = player_list[load-1]
                os.system('cls')
                print(f"\n\nWelcome back, {player.getUsername()}.")
                break
            else:
                os.system('cls')
                print("Invalid Input!")
                continue
        elif choice == 2:
            os.system('cls')
            print("No past souls yet. Create a new soul first.")
        elif choice == 3:
            main_menu()
        else:
            print("Invalid Input!")
            continue
            
    while i != 1:
            if player.getSPWins() == 2:
                j = 0
                print("You can now choose your Super Class.")
                print("Choose from 3 different options:")
                print("\n1. Swordsman")
                print("2. Archer")
                print("3. Magician")
                while j != 1:
                    class_choice = int(input("||"))
                    if class_choice == 1:
                        player = Swordsman(player.getUsername())
                        print(f"{player.getUsername()} chose to be a Swordsman.")
                        player.ClassAscension()
                        break
                    elif class_choice == 2:
                        player = Archer(player.getUsername())
                        print(f"{player.getUsername()} chose to be an Archer.")
                        player.ClassAscension()
                        break
                    elif class_choice == 3:
                        player = Magician(player.getUsername())
                        print(f"{player.getUsername()} chose to be a Magician.")
                        player.ClassAscension()
                        break
                    else:
                        print("Invalid Input!")
                        continue
            time.sleep(0.3)
            print("\nChoose an option:")
            time.sleep(0.3)
            print("1. Start the Encounter")
            time.sleep(0.3)
            print("2. Save and Quit to Main Menu")
            
            choice = int(input("||"))
            if choice == 1:
                enemy = Boss("Monster")
                os.system('cls')
                result = encounter(player, enemy, 1)
                if result == 0:
                    print("You have been succumbed to the corruption.")
                    wait = input("Press Enter to return to previous checkpoint")
                    os.system('cls')
                elif result == 1:
                    print(f"You have bested {enemy.getUsername()}.")
                    wait = input("Press Enter to continue.")
                    os.system('cls')
                    player.addSPWins()
            elif choice == 2:
                os.system('cls')
                main_menu()
            else:
                print("Invalid Input!")
                continue
def pvp():
    os.system('cls')
    print("====================")
    print("= PLAYER vs PLAYER =")
    print("====================")
    
    PlayerUsername = str(input("Soul 1's Username: "))
    print("Select a Super Class:")
    print("\n1. Swordsman")
    print("2. Archer")
    print("3. Magician")
    j = 0
    while j != 1:
        choice = int(input("||"))
        if choice == 1:
            player = Swordsman(PlayerUsername)
            break
        if choice == 2:
            player = Archer(PlayerUsername)
            break
        if choice == 3:
            player = Magician(PlayerUsername)
            break
    os.system('cls')
    EnemyUsername = str(input("Soul 2's Username: "))
    print("Select a Super Class:")
    print("\n1. Swordsman")
    print("2. Archer")
    print("3. Magician")
    j = 0
    while j != 1:
        choice = int(input("||"))
        if choice == 1:
            enemy = Swordsman(EnemyUsername)
            break
        if choice == 2:
            enemy = Archer(EnemyUsername)
            break
        if choice == 3:
            enemy = Magician(EnemyUsername)
            break
    result = encounter(player, enemy, 2)
    if result == 0:
        print(f"{enemy.getUsername()} won.")
        wait = input("Press Enter to return to main menu.")
        enemy.addPVPWins()
        os.system('cls')
        main_menu()
    elif result == 1:
        print(f"{player.getUsername()} won.")
        wait = input("Press Enter to return to main menu.")
        player.addPVPWins()
        os.system('cls')
        main_menu()

main_menu()
