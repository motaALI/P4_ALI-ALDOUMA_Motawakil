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

    def is_dob_valide(date_text):
        try:
            datetime.strptime(date_text, "%d/%m/%Y")
        except ValueError:
            print("This is the incorrect date string format. It should be DD/MM/YYYY")
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    def is_valide_input_string(stie: str):
        try:
            if stie.isalpha():
                return True
            else:
                print(f"{Fore.RED} + {stie} DOIT ETRE chaîne de caractères")
                return False
        except ValueError:
            print(f"{Fore.RED} + {stie} ne doit pas être vide")
            raise ValueError(f"{stie} ne doit pas être vide")

    def is_valide_input_gender(gender: str):
        try:
            if gender.upper() in ("F", "M", "O"):
                print(Fore.RED + "le genre doit être entre 'F', 'M' ou 'O")
                return True
            else:
                return False
        except ValueError:
            print(f"{gender} ne doit pas être vide")
            raise ValueError(f"{gender} ne doit pas être vide")

    def is_valide_classement(classement: int):
        try:
            if classement > 2000:
                print(f"{Fore.RED} + {classement} EST 2000 MAX")
                return False
            elif classement < 0:
                return False
            else:
                return True
        except ValueError:
            raise ValueError(f"{classement} ne doit pas être vide")
