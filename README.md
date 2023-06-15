# Application IFC (Flashcards interactives)

Intelligent FlashCards est un logiciel simple de flashcards conçu pour faciliter l'apprentissage des langues étrangères en utilisant la méthode de répétition espacée, tout en observant sa progression.

## Fonctionnalités

- Créez et gérez vos propres jeux de flashcards.
- Ajoutez des cartes avec des mots à traduire dans vos propres paquets.
- Visualisez votre score pour évaluer votre niveau.

## Prérequis

> Python 3.x
> 
> SQLite3
> 
> Sqlite_flachcard
> 
> Yaml
> 
> Streamlit
> 
> Streamlit Extra
> 
> Matplotlib.pyplot

## Utilisation

1. L'application s'ouvrira avec une fenêtre de connexion. Si vous avez déjà un compte, saisissez vos identifiants pour vous connecter ou vous inscrire si vous êtes un nouvel utilisateur. Une fois connecté, vous serez redirigé vers la page d'accueil. 
2. Dans le menu principal, vous avez différentes options. 
3. À partir de là, vous pouvez accéder aux différentes fonctionnalités d'Intelligent FlashCards, telles que la création et la gestion des cartes dans les options de "Mes Cartes" et "Nouveau Paquet", le suivi de vos résultats dans "Mes Résultats" et la déconnexion par l'onglet de "Se déconnecter". 
> L'option "Mes Cartes" permet de consulter les paquets de flashcards. Choisissez un thème dans la liste pour commencer votre jeu de flashcards ainsi une flashcard apparaîtra, à vous de traduire le mot mentalement avant de visualiser la réponse en cliquant dessus et vous pourrez préciser si votre réponse était juste ou fausse et continuer avec d'autres cartes.
- Pour créer un paquet personnalisé, cliquez sur l'option "Nouveau Paquet" dans la fenêtre principale. Donnez un nom à votre paquet et vous pouvez ensuite ajouter des nouveaux mots et leur traduction pour chaque carte. Vous pouvez créer plusieurs mots de cette manière.
4. Vous pouvez consulter votre progression globale en cliquant sur l'option "Mes résultats" dans la fenêtre principale. Vous y trouverez des statistiques sur vos performances dans les différents paquets.

## Execution du logiciel et des fichiers

Pour utiliser l'application IFC, suivez ces étapes :
- Installez les dépendances requises en exécutant la commande `pip install -r requirements.txt`. 
- Lancez l'application en utilisant la commande `streamlit run app.py`. 
- Accédez à l'application via votre navigateur à l'adresse `http://localhost:8501`.


### Main: 
Le code de Main gère l'authentification des utilisateurs de l'application, y compris la connexion, l'inscription, la réinitialisation du mot de passe et la mise à jour des détails utilisateur.
1. L'utilisateur accède à l'application et voit une interface d'authentification.
2. L'utilisateur peut saisir ses identifiants de connexion (nom d'utilisateur et mot de passe) dans le widget de connexion.
3. Si l'authentification est réussie, un message de bienvenue est affiché avec le nom de l'utilisateur.
4. Un bouton de déconnexion est également affiché pour permettre à l'utilisateur de se déconnecter.
5. En dessous du message de bienvenue, il y a un bouton "Ma page d'accueil" qui permet à l'utilisateur de passer à la page d'accueil de l'application.
6. Une section "À propos" est affichée avec une description de l'application Intelligent FlashCards et de ses fonctionnalités.
7. Si l'authentification échoue, l'utilisateur peut avoir différentes options :
   - S'il souhaite s'inscrire en tant que nouvel utilisateur, il peut cliquer sur le bouton "Register user" et suivre le processus d'inscription.
   - S'il a oublié son mot de passe, il peut cliquer sur le bouton "Forgot password" pour réinitialiser son mot de passe.
   - S'il a oublié son nom d'utilisateur, il peut cliquer sur le bouton "Forgot username" pour récupérer son nom d'utilisateur.
   - Si les informations d'identification fournies par l'utilisateur sont incorrectes, un message d'erreur est affiché.

8. Ensuite, le code gère la possibilité pour l'utilisateur de modifier son mot de passe. Si l'authentification est réussie, un widget de modification du mot de passe est affiché. 
L'utilisateur peut saisir un nouveau mot de passe et le modifier. Une fois le mot de passe modifié avec succès, un message de succès est affiché.
#### Dépendances
Ce code utilise les bibliothèques suivantes :
- streamlit : utilisée pour créer l'application et afficher l'interface utilisateur.
- streamlit_authenticator : utilisée pour gérer l'authentification des utilisateurs.
- yaml : utilisée pour lire et écrire des fichiers de configuration YAML.
- streamlit_extras.switch_page_button : utilisée pour gérer la navigation entre les pages de l'application.

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
2. `AnswerTable` : Cette classe représente la table answer_table dans la base de données SQLite. Elle offre des fonctionnalités similaires à la classe QuestionTable pour interagir avec la table des réponses.
   - `__init__`: Initialise une connexion à la base de données SQLite et crée un curseur pour exécuter les requêtes SQL.
   - `create_table`: Crée la table `answer_table` dans la base de données.
   - `add_data`: Ajoute une carte de réponse à la table.
   - `show_table`: Affiche le contenu complet de la table des réponses.
   - `show_answer`: Affiche les cartes de réponse d'un paquet spécifique.
   - `show_answer_by_question`: Récupère la réponse correspondant à une question donnée à partir de la table des réponses.
   - `update_data`: Met à jour les données d'une réponse existante.
   - `delete_data`: Supprime une réponse de la table.
   - `delete_table()` : Supprime toute la table des réponses. 
   - `execute_query(query)` : Exécute une requête SQL en l'appliquant à la base de données. 
   - `close_sqlite()` : Ferme la connexion à la base de données SQLite.
3. `UserTable` : Cette classe fournit des fonctionnalités similaires pour interagir avec la table des utilisateurs.
   - `__init__()` : Initialise une connexion à la base de données SQLite et crée un curseur pour exécuter des requêtes SQL.
   - `create_table()` : Crée la table "user_table" dans la base de données.
   - `add_data(name)` : Ajoute un utilisateur à la table des utilisateurs.
   - `show_table()` : Affiche le contenu complet de la table des utilisateurs.
   - `show_data(i)` : Affiche les informations d'un utilisateur spécifique dans la base de données.
   - `show_iduser(name)` : Récupère l'ID d'un utilisateur spécifique.
   - `update_data(name, iduser)` : Modifie le nom d'un utilisateur.
   - `delete_data(iduser)` : Supprime un utilisateur de la table des utilisateurs.
   - `delete_table()` : Supprime toute la table des utilisateurs.
   - `execute_query(query)` : Exécute une requête SQL en l'appliquant à la base de données.
   - `close_sqlite()` : Ferme la connexion à la base de données SQLite.
4. `AnswerUserTable` : Cette classe est utilisée pour gérer la relation entre les réponses et les utilisateurs.
   - `__init__()` : Initialise une connexion à la base de données SQLite et crée un curseur pour exécuter des requêtes SQL.
   - `create_table()` : Crée la table "answer_user_table" dans la base de données.
   - `add_data(idanswer_fk, iduser_fk, score)` : Ajoute un résultat à la table des réponses-utilisateurs.
   - `show_table()` : Affiche le contenu complet de la table des réponses-utilisateurs.
   - `show_data(idanswer_user)` : Affiche les informations d'une ligne spécifique de la table des réponses-utilisateurs.
   - `show_result(name, idanswer_fk)` : Affiche le résultat d'un utilisateur spécifique pour une réponse sélectionnée.
   - `update_data(score, idanswer_user)` : Modifie le résultat d'un utilisateur pour une réponse donnée.
   - `delete_data(idanswer_user)` : Supprime un résultat de la table des réponses-utilisateurs.
   - `delete_table()` : Supprime toute la table des réponses-utilisateurs.
   - `execute_query(query)` : Exécute une requête SQL en l'appliquant à la base de données.
- `close_sqlite()` : Ferme la connexion à la base de données SQLite.
5. `QuestionUserTable` : Cette classe est utilisée une table de base de données pour associer des questions à des utilisateurs.
   - `__init__()`: Initialise une connexion à la base de données SQLite et crée un curseur pour exécuter des requêtes SQL.
   - `create_table()`: Crée la table "question_user_table" dans la base de données.
   - `add_data(idquestion_fk, iduser_fk)`: Ajoute une carte de question à un utilisateur.
   - `show_table()`: Affiche le contenu complet de la table "question_user_table".
   - `show_data(idquestion_user)`: Affiche les informations d'un élément spécifique dans la table "question_user_table".
   - `delete_data(idquestion_user)`: Supprime un lien de la table "question_user_table".
   - `delete_table()`: Supprime la table "question_user_table" de la base de données.
   - `execute_query(query)`: Exécute une requête SQL en l'appliquant à la base de données.
   - `close_sqlite()`: Ferme la connexion à la base de données SQLite.

Chaque classe contient des méthodes pour créer la table correspondante, ajouter des données, afficher les données, mettre à jour les données, supprimer les données, etc.

### Controler : 
Le fichier controller.py contient la classe Controller, qui permet l'interaction entre le frontend et le backend de l'application.
Les fonctions de cette classe utilisent les méthodes des classes QuestionTable, AnswerTable et AnswerUserTable du module sqlite_flashcard pour effectuer des opérations sur la base de données de cartes flash. 
Le contrôleur agit comme une couche intermédiaire entre l'interface utilisateur et la base de données, encapsulant la logique de gestion des cartes flash et fournissant des méthodes d'accès aux données.
#### Utilisation
1. Importation de la classe `Controller` depuis le module `controler.controler`.
2. Création d'une instance de la classe `Controller` pour interagir avec la base de données.
3. Utilisation des méthodes de la classe `Controller` pour effectuer les opérations suivantes :
   - Ajouter une question à un paquet spécifique en utilisant la méthode `add_question_c(question, paquet)`.
   - Récupérer tous les paquets disponibles en utilisant la méthode `show_all_packs_c()`.
   - Récupérer les questions d'un paquet spécifique en utilisant la méthode `show_question_c(paquet)`.
   - Ajouter une réponse à un paquet spécifique en utilisant la méthode `add_answer_c(answer, paquet)`.
   - Récupérer les réponses d'un paquet spécifique en utilisant la méthode `show_answer_c(paquet)`.
   - Ajouter les données de réponse d'un utilisateur en utilisant la méthode `answeruser_add_data_c(idanswer_fk, iduser_fk, score)`.
4. Exécution de l'application par le script principal `main.py`.
5. Utilisation de l'interface utilisateur pour interagir avec les fonctionnalités de l'application.
#### Dépendances
Ce code utilise les fonctionnalités du module sqlite_flashcard pour interagir avec la base de données des cartes flash.

### Menu :
Ce fichier définit une page de menu pour l'application IFC (Intelligent FlashCards). La page de menu affiche des boutons pour accéder aux différentes fonctionnalités de l'application. 
Lorsqu'un bouton est cliqué, la fonction `switch_page` est utilisée pour naviguer vers la page correspondante.
#### Fonctionnalités principales
- **Afficher les cartes** : Le bouton "Mes cartes" permet d'accéder à la page "Mes cartes" où l'utilisateur peut sélectionner un thème de cartes et afficher les questions et réponses associées.
- **Créer de nouvelles cartes** : Le bouton "Nouvelles cartes" permet d'accéder à la page "Nouveau paquet" où l'utilisateur peut créer de nouvelles cartes en ajoutant des questions et réponses à un thème spécifique.
- **Afficher les résultats** : Le bouton "Mes résultats" permet d'accéder à la page "Résultats" où l'utilisateur peut visualiser sa progression et ses résultats d'apprentissage.
- **Se déconnecter** : Le bouton "Se déconnecter" permet à l'utilisateur de se déconnecter de l'application.
#### Utilisation du menu
Lorsque l'utilisateur clique sur l'un des boutons du menu, il est redirigé vers la page correspondante de l'application. 
* Mes Cartes : Cliquez sur le bouton "Mes cartes" pour accéder à vos jeux de flashcards. Vous pouvez consulter, modifier et étudier les cartes de chaque jeu. Utilisez cette fonctionnalité pour revoir et renforcer vos connaissances. 
* Nouvelles cartes : Pour créer de nouvelles flashcards, cliquez sur le bouton "Nouvelles cartes". Vous pouvez saisir de nouvelles questions et réponses pour construire vos propres jeux de flashcards personnalisés. Utilisez cette fonctionnalité pour élargir votre matériel d'apprentissage. 
* Mes résultats : Suivez votre progression et consultez vos performances grâce à la fonctionnalité "Mes résultats". Elle affiche des informations sur vos performances avec différentes flashcards et aide à identifier les domaines qui nécessitent davantage d'attention. 
* Se déconnecter : Pour vous déconnecter, cliquez sur le bouton "Se déconnecter".


### Nouveau_paquet :
Ce fichier permet à l'application de créer de nouvelles cartes flash.
Les utilisateurs peuvent saisir le nom d'un paquet, ajouter de nouveaux mots et leurs traductions et valider la création des cartes flash.
#### Ajout des nouvelles cartes
1. Lors du lancement de l'application, vous verrez une page intitulée "Nouveau paquet". 
2. Saisissez le nom du nouveau paquet dans le champ de saisie prévu à cet effet. 
3. Cliquez sur le bouton "Créer" pour continuer. 
4. Si le bouton est cliqué et qu'un nom de paquet est saisi, un message indiquant la création de nouvelles cartes s'affichera. 
5. L'application présentera un formulaire permettant de saisir de nouveaux mots et leurs traductions. 
6. Saisissez un nouveau mot dans le champ de saisie "Nouveau mot" et sa traduction dans le champ de saisie "Traduction". 
7. Cliquez sur le bouton "Ajouter" pour ajouter la nouvelle carte. 
8. Si les champs du mot et de la traduction ne sont pas vides, l'application affichera un message de réussite indiquant la création de la nouvelle carte. 
9. Les valeurs du mot et de la traduction seront affichées à l'utilisateur. 
10. Répétez les étapes 6 à 9 pour ajouter plus de cartes. Le formulaire continuera à être affiché jusqu'à ce que le bouton "Ajouter" ne soit pas cliqué. 
11. Une fois toutes les nouvelles cartes ajoutées, cliquez sur le bouton "Valider" pour valider la création des cartes flash. 
12. Le code traitera les nouveaux mots et traductions, en appelant la fonction submit_form() pour ajouter la question et la réponse au paquet spécifié. 
13. L'application affichera les valeurs du mot et de la traduction pour confirmer la création de chaque carte. 
14. Enfin, un message de réussite sera affiché, indiquant la création réussie des cartes flash. 
15. Si le bouton "Créer" est cliqué, mais aucun nom de paquet n'est saisi, un message d'avertissement sera affiché, demandant à l'utilisateur de saisir le nom du paquet. 
16. Le bouton "Retour au menu" peut être cliqué pour revenir à la page "MenuIFC".

### Mes_cartes :
Ce fichier principal de l'application Streamlit affiche une page intitulée "Mes cartes" avec une liste déroulante de sélection de thème et une liste de questions et réponses. 
Chaque question est affichée dans un expandeur, et des boutons sont fournis pour que l'utilisateur puisse répondre (Juste ou Faux). 
La réponse sélectionnée est capturée et traitée par l'instance du contrôleur (Controller).
#### Utilisations
1. Sélectionnez un thème de cartes parmi les options disponibles dans le menu déroulant. 
2. Une fois que vous avez sélectionné un thème, les flashcards associées à ce thème seront affichées. 
3. Chaque flashcard se compose d'une question et d'une réponse.
4. Pour chaque question affichée, deux boutons sont présents : "Juste" et "Faux". Vous pouvez cliquer sur l'un de ces boutons pour indiquer si votre réponse à la question est correcte ou incorrecte.
5. Lorsque vous cliquez sur le bouton "Juste", un message de confirmation est affiché avec une icône appropriée pour indiquer que la réponse est correcte. 
6. De même, lorsque vous cliquez sur le bouton "Faux", un message d'erreur est affiché avec une icône appropriée pour indiquer que la réponse est incorrecte. 
7. Vous pouvez continuer à parcourir les questions et à fournir ses réponses en cliquant sur les boutons correspondants. 
8. Enfin, l'utilisateur a la possibilité de revenir à la page du menu en cliquant sur le bouton "Retour au menu".
#### Dépendances
Ce code utilise les bibliothèques suivantes :
- streamlit : utilisée pour créer l'application et afficher l'interface utilisateur.
- streamlit_extras.switch_page_button : utilisée pour gérer la navigation entre les pages de l'application.
- controler.controler : fichier contenant la classe Controller utilisée pour la récupération des questions, réponses et autres fonctionnalités du contrôleur.

### Résultats :
Cette partie du code utilise le framework Streamlit pour créer une interface utilisateur conviviale. Il utilise également Matplotlib pour générer un graphique représentant la progression des résultats.
#### Fonctionnalitées Principales
**Affichage des résultats** : L'application affiche les résultats d'apprentissage des flashcards dans une interface claire. 
**Sélection des thèmes de cartes** : Vous pouvez sélectionner un thème de cartes parmi ceux disponibles pour afficher les résultats correspondants. 
**Retour au menu principal** : Vous avez la possibilité de retourner au menu principal en cliquant sur le bouton "Retour au menu".
####Affichage du graphique
Le graphique représente la progression des résultats sous forme de courbe. Les données utilisées pour le graphique sont définies dans les listes x et y. 
Le graphique est créé à l'aide de la bibliothèque Matplotlib. Les axes x et y sont étiquetés et la légende du graphique est affichée.

***
À propos d'Intelligent FlashCards

Intelligent FlashCards est un projet développé par le groupe LOLS en 2023. Nous avons créé ce logiciel dans le but d'aider les utilisateurs à apprendre de nouvelles langues de manière amusante et efficace. Nous espérons que cette application vous aidera à atteindre vos objectifs d'apprentissage linguistique !

Olivia VERBRUGGE
Leonie NUSSBAUM
Laure MARGOT
Sinem KILIC
