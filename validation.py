from datetime import datetime

from colorama import Fore


class Validators:
    def is_valide_date(your_date):
        format = "%d-%m-Y"

        try:
            datetime.strptime(your_date, format)
            print("This is the correct date string format.")
        except ValueError:
            print("This is the incorrect date string format. It should be DD/MM/YYYY")

    def is_valide_input_string(stie: str):
        if len(stie) == 0:
            return f"{stie} ne doit pas être vide"
        return True

    def is_valide_input_gender(gender: str):
        error_message = ""
        if gender.upper() == "F" or gender.upper() == "M" or gender.upper() == "O":
            error_message = "Veuillez entrer [F, M, O] comme genre !"
            return Fore.RED + error_message
        else:
            return False
