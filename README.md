# Dash-Application

Cette application Dash est un projet démonstratif conçu pour explorer les fonctionnalités clés de le framework Dash. Elle permet de visualiser des graphiques interactifs, d'afficher des tables, et de tester des interactions dynamiques avec des callbacks.

L'application contient plusieurs fonctionnalités interactives permettant aux utilisateurs de :

1. **Saisir et afficher un texte** :
   - L'utilisateur peut entrer un texte via un champ de saisie, et ce texte est affiché dynamiquement après soumission.

2. **Visualiser des graphiques interactifs** :
   - Trois types de graphiques sont générés en fonction de la sélection d'une option dans un menu déroulant :
     - Graphique en barres.
     - Graphique en lignes.
     - Graphique circulaire.

3. **Sélectionner des options via un menu déroulant** :
   - Les utilisateurs peuvent choisir une option dans un dropdown et voir un graphique mis à jour en temps réel.

4. **Visualiser les callbacks et les performances** :
   - L'application Dash permet d'explorer un outil intégré de visualisation des callbacks, où l'on peut inspecter les interactions entre les composants (inputs/outputs), mesurer les temps d'exécution, et identifier les 
     erreurs éventuelles.
   - Cette fonctionnalité est accessible via les boutons en bas de la page, comme "Callbacks", "Errors", et "Server".

### 📁 Structure du projet

Le projet est organisé comme suit :

 ├── app.py # Point d'entrée principal 
 
 ├── layout.py # Définit le layout (structure visuelle) 
 
 ├── callbacks.py # Gestion des interactions (callbacks) 
 
 ├── requirements.txt # Liste des dépendances 
 
 ├── assets/ # Contient les fichiers CSS (styles personnalisés) │ └── style.css # Exemple de fichier CSS 
 
 └── README.md # Documentation du projet

### 🛠️ Technologies utilisées

- **Python** : Langage principal.
- **Dash** : Framework pour la création d'applications web interactives.
- **Plotly** : Génération de graphiques interactifs.
- **Pandas** : Manipulation et traitement des données.

### 🚀 Installation

1. Clonez ce dépôt GitHub :
   
```bash
git clone https://github.com/Housseem946/Dash-Application.git
```
2. Installez les dépendances :

 ```bash
pip install -r requirements.txt
 ```
3. Lancez l'application :

 ```bash
python app.py
 ```
4. Ouvrez un navigateur et accédez à http://127.0.0.1:8050.

### 🎨 Fonctionnalités interactives

#### Graphiques interactifs :

Les graphiques changent dynamiquement en fonction des choix des utilisateurs.
Les types de graphiques incluent des barres, des lignes, et des diagrammes circulaires.

#### Composants Dash :

Utilisation de composants standards comme dcc.Graph, dcc.Input, et dcc.Dropdown.

#### Design personnalisé :

Un fichier CSS pour styliser l'application (personnalisation simple).

### 📷 Aperçu de l'application

![image](https://github.com/user-attachments/assets/fae1b106-1a56-4873-88ed-a0c571a55765)

![image](https://github.com/user-attachments/assets/656c8dbb-e927-4236-beb1-6032e7507bba)

![image](https://github.com/user-attachments/assets/95e521a8-38b4-4def-a184-c2471dcb696f)

![image](https://github.com/user-attachments/assets/d70b62bb-cfd2-4250-9747-36a592d6fc23)

### 🛡️ Contribuer

Je vous invite à contribuer à ce projet pour l'améliorer et y ajouter de nouvelles fonctionnalités. Si vous avez des idées ou des suggestions, n'hésitez pas à soumettre vos propositions. 

### Bonjour 

Pour en savoir plus sur Dash et ses possibilités, la documentation officielle est une excellente ressource : [Documentation Dash](https://dash.plotly.com/).
