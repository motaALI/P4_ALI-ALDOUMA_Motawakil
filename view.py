from colorama import Fore
class Display:
    def render_menu(menu):
        for (index, choice) in menu.items():
            print(index, "-", choice)

    def get_user_input(menu):
        response = input("Veuillez choisir une action : ")
        if response in menu:
            return response
        else:
            error = Display.ShowError()
            print(f"{error} {Fore.LIGHTBLUE_EX} {menu}")

    def endView():
        confirm = input("Voulez vous vraiment quitter l'application ? oui[O], non[N] ")
        if confirm in ['o', 'n']:
            if confirm == 'o' or confirm == 'O':
                print("Au revoir !")
            else:
                #TODO Make it work
                print("!!!!!")
            
    def ShowError():
        print(f"{Fore.RED} Une erreur s'est produite, veuillez sélectionner une action dans cette liste\n")
