# Application IFC (Flashcards interactives)

Intelligent FlashCards est un logiciel simple de flashcards conçu pour faciliter l'apprentissage des langues étrangères en utilisant la méthode de répétition espacée, tout en observant sa progression.

## Fonctionnalités

- Créez et gérez vos propres jeux de flashcards.
- Ajoutez des cartes avec des mots à traduire dans vos propres paquets.
- Visualisez votre score pour évaluer votre niveau.

## Prérequis

- Python 3.x
- SQLite
- Yaml
- Streamlit, Streamlit Extra
- 
## Utilisation

1. L'application s'ouvrira avec une fenêtre de connexion. Si vous avez déjà un compte, saisissez vos identifiants pour vous connecter ou vous inscrire si vous êtes un nouvel utilisateur. Une fois connecté, vous serez redirigé vers la page d'accueil. 
2. Dans le menu principal, vous avez les options de Mes Cartes, Nouveau Paquet, Mes Résultats, Se déconnecter.  
3. À partir de là, vous pouvez accéder aux différentes fonctionnalités d'Intelligent FlashCards, telles que la création et la gestion des cartes, le suivi de vos résultats, etc. 
- Vous pouvez sélectionner l'option "Mes Cartes" pour consulter les paquets de flashcards. Choisissez un paquet de votre choix pour commencer à votre jeu de flashcards.
- Pour créer un paquet personnalisé, cliquez sur l'option "Nouveau Paquet" dans la fenêtre principale. Donnez un nom à votre paquet et sélectionnez un thème dans la liste. Vous pouvez ensuite ajouter des mots et leur traduction pour chaque flashcard.
Une fois que vous avez ajouté des paquets à votre collection personnelle, vous pouvez sélectionner un paquet et 

------cliquer sur "Lancer la session de révision" pour commencer une session de révision.

7. Pendant la session de révision, une flashcard apparaîtra à l'écran avec la question. Saisissez votre réponse dans la zone de texte prévue à cet effet et appuyez sur "Enter" pour soumettre votre réponse. Vous recevrez immédiatement un feedback indiquant si votre réponse est correcte ou non.
8. Après avoir répondu à toutes les flashcards, un récapitulatif s'affichera avec votre score.
9. Vous pouvez consulter votre progression globale en cliquant sur l'option "Mon profil" dans la fenêtre principale. Vous y trouverez des statistiques sur vos performances dans les différents paquets.

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
Ce le code qui .....








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
1. Entrez le nom du nouveau paquet dans le champ de . 
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

