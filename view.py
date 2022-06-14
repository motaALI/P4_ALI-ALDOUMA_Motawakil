class Display:
    def render_menu(menu):
        for (index, choice) in menu.items():
            print(index, "-", choice)

    def get_user_input(menu):
        response = input("Veuillez choisir une action : ")
        if response in menu:
            return response
        print("Error")

    def endView():
        print("Goodbye")
