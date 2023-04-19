
from googletrans import Translator
translator = Translator()
translation = translator.translate("Der Himmel ist blau und ich mag Bananen", dest='en')
print(translation.text)


# Execution du code de la base de données...
def main():

    pass


if __name__ == "__main__":
    main()