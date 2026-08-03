import os


files = [

"bot/config.py",
"bot/main.py",
"website/app.py",
"requirements.txt"

]


print("Vérification Lumora...")


for file in files:

    if os.path.exists(file):

        print("OK :", file)

    else:

        print("MANQUANT :", file)


print("Vérification terminée.")
