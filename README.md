# Application IFC (Flashcards interactives)

Intelligent FlashCards est un logiciel simple de flashcards conçu pour faciliter l'apprentissage des langues étrangères en utilisant la méthode de répétition espacée, tout en observant sa progression.

## Fonctionnalités

- Créez et gérez vos propres jeux de flashcards.
- Ajoutez des cartes avec des mots à traduire dans vos propres paquets.
- Visualisez votre score pour évaluer votre niveau.

## Prérequis

- Python 3.x
- SQLite3
- Sqlite_flachcard
- Yaml
- Streamlit
- Streamlit Extra
- Matplotlib.pyplot

## Utilisation

1. L'application s'ouvrira avec une fenêtre de connexion. Si vous avez déjà un compte, saisissez vos identifiants pour vous connecter ou vous inscrire si vous êtes un nouvel utilisateur. Une fois connecté, vous serez redirigé vers la page d'accueil. 
2. Dans le menu principal, vous avez différentes options. 
3. À partir de là, vous pouvez accéder aux différentes fonctionnalités d'Intelligent FlashCards, telles que la création et la gestion des cartes dans les options : Mes Cartes /-Nouveau Paquet, le suivi de vos résultats dans -Mes Résultats, et la déconnexion par - Se déconnecter. 
- L'option "Mes Cartes" permet de consulter les paquets de flashcards. Choisissez un thème dans la liste pour commencer votre jeu de flashcards ainsi une flashcard apparaîtra, à vous de traduire le mot mentalement avant de visualiser la réponse en cliquant dessus et vous pourrez préciser si votre réponse était juste ou fausse et continuer avec d'autres cartes.
- Pour créer un paquet personnalisé, cliquez sur l'option "Nouveau Paquet" dans la fenêtre principale. Donnez un nom à votre paquet et vous pouvez ensuite ajouter des nouveaux mots et leur traduction pour chaque carte. Vous pouvez créer plusieurs mots de cette manière.
4. Vous pouvez consulter votre progression globale en cliquant sur l'option "Mes résultats" dans la fenêtre principale. Vous y trouverez des statistiques sur vos performances dans les différents paquets.

## Execution du logiciel et les fichiers

Pour utiliser l'application IFC, suivez ces étapes :
- Installez les dépendances requises en exécutant la commande `pip install -r requirements.txt`. 
- Lancez l'application en utilisant la commande `streamlit run app.py`. 
- Accédez à l'application via votre navigateur à l'adresse `http://localhost:8501`.

### Main: 
Le code de Main est la partie qui permet aux utilisateurs de :
- se connecter, s'inscrire et réinitialiser leur mot de passe. 
- mettre à jour leurs informations personnelles. 
- accéder à leur page d'accueil personnalisée. 
- demander la réinitialisation de leur mot de passe. 
- demander l'envoi de leur nom d'utilisateur par e-mail. 
- créer, modifier et supprimer des cartes d'apprentissage. 
- consulter leurs résultats d'apprentissage.
### Sqlite_flashcard : 
Ce code de la gestion de base de données SQLite crée et initialise plusieurs tables pour stocker des questions, des réponses, des utilisateurs et des résultats.
Voici une description des classes et de leurs principales méthodes :
1. `QuestionTable` : Cette classe gère la table des questions. Les principales méthodes sont :
   - `create_table()` : crée la table des questions.
   - `add_data(question, paquet)` : ajoute une carte de question à la table des questions.
   - `show_table()` : affiche toutes les lignes de la table des questions.
   - `show_question(paquet)` : affiche les cartes de question d'un paquet sélectionné.
   - `show_all_packs()` : affiche tous les paquets de questions.
   - `show_pack(iduser_fk)` : affiche les paquets enregistrés d'un utilisateur donné.
   - `user_show_questions(iduser_fk, paquet)` : affiche les questions d'un utilisateur pour un paquet sélectionné.
   - `update_data(question, idquestion)` : modifie la valeur d'une carte de question.
   - `delete_data(idquestion)` : supprime une carte de question de la table.
   - `delete_table()` : supprime la table des questions.
   - `close_sqlite()` : ferme la connexion à la base de données.
2. `AnswerTable` : Cette classe gère la table des réponses. 
3. `UserTable` : Cette classe gère la table des utilisateurs. 
4. `AnswerUserTable` : Cette classe gère la table des résultats des utilisateurs. 

### Controler : 
Le fichier controller.py contient la classe Controller, qui permet l'interaction entre le frontend et le backend de l'application.
Pour utiliser le contrôleur, vous devez d'abord importer le module sqlite_flashcard du package model :
```python
from model import sqlite_flashcard
```
Ensuite, vous pouvez créer une instance de la classe Controller pour accéder aux différentes fonctionnalités fournies.

### Menu :
* Mes Cartes : Cliquez sur le bouton "Mes cartes" pour accéder à vos jeux de flashcards. Vous pouvez consulter, modifier et étudier les cartes de chaque jeu. Utilisez cette fonctionnalité pour revoir et renforcer vos connaissances. 
* Nouvelles cartes : Pour créer de nouvelles flashcards, cliquez sur le bouton "Nouvelles cartes". Vous pouvez saisir de nouvelles questions et réponses pour construire vos propres jeux de flashcards personnalisés. Utilisez cette fonctionnalité pour élargir votre matériel d'apprentissage. 
* Mes résultats : Suivez votre progression et consultez vos performances grâce à la fonctionnalité "Mes résultats". Elle affiche des informations sur vos performances avec différentes flashcards et aide à identifier les domaines qui nécessitent davantage d'attention. 
* Se déconnecter : Pour vous déconnecter, cliquez sur le bouton "Se déconnecter".
### Nouveau_paquet :
1. Entrez le nom du nouveau paquet dans le champ. 
2. Cliquez sur le bouton "Créer" pour créer le nouveau paquet. 
3. Une fois le paquet créé, vous pouvez ajouter de nouvelles cartes en remplissant les champs de texte "Nouveau mot" et "Traduction" et en cliquant sur le bouton "Ajouter". 
4. Répétez l'étape précédente pour ajouter autant de cartes que nécessaire. 
5. Une fois que vous avez ajouté toutes les cartes souhaitées, cliquez sur le bouton "Valider" pour enregistrer les cartes dans le paquet. 
6. Les cartes nouvellement créées seront affichées à l'écran avec leur mot et leur traduction correspondants. 
7. Vous pouvez continuer à créer de nouveaux paquets ou revenir au menu principal en cliquant sur le bouton "Retour au menu".
### Mes_cartes :
1. Sélectionnez un thème dans le menu déroulant. 
2. Une fois que vous avez sélectionné un thème, les flashcards associées à ce thème seront affichées. 
3. Chaque flashcard se compose d'une question et d'une réponse.
4. Développez la flashcard pour afficher la question et sa réponse correspondante. 
5. Pour chaque flashcard, vous pouvez cliquer sur le bouton "Juste" si vous avez répondu correctement à la question, ou sur le bouton "Faux" si votre réponse était incorrecte. 
6. L'application vous fournira un retour en fonction de votre réponse. 
7. Vous pouvez continuer à revoir et à répondre à d'autres flashcards. 
8. Si vous souhaitez revenir au menu principal, cliquez sur le bouton "Retour au menu".
### Résultats : 
Cette partie du code utilise le framework Streamlit pour créer une interface utilisateur conviviale.
* Affichage des résultats : L'application affiche les résultats d'apprentissage des flashcards dans une interface claire. 
* Sélection des thèmes de cartes : Vous pouvez sélectionner un thème de cartes parmi ceux disponibles pour afficher les résultats correspondants. 
* Retour au menu principal : Vous avez la possibilité de retourner au menu principal en cliquant sur le bouton "Retour au menu".



***
À propos d'Intelligent FlashCards

Intelligent FlashCards est un projet développé par le groupe LOLS en 2023. Nous avons créé ce logiciel dans le but d'aider les utilisateurs à apprendre de nouvelles langues de manière amusante et efficace. Nous espérons que cette application vous aidera à atteindre vos objectifs d'apprentissage linguistique !

Olivia VERBRUGGE
Leonie NUSSBAUM
Laure MARGOT
Sinem KILIC
