# Log Analyzer

## Présentation

Log Analyzer est un projet simple destiné à aider les débutants à lire, analyser et mieux comprendre des fichiers de logs.

Un fichier log contient souvent des informations sur le fonctionnement d’un programme : erreurs, avertissements, dates et événements. Ce projet permet de traiter ces informations afin d’en extraire les éléments importants.

## Fonctionnalités

- Lecture d’un fichier de logs
- Recherche d’informations dans les logs
- Identification des erreurs et des avertissements
- Affichage des résultats dans le terminal
- Organisation des données afin de faciliter leur lecture

## Installation

### Prérequis

- Python 3 installé
- Un terminal
- Git, si vous souhaitez télécharger le projet avec Git

Vérifiez Python avec la commande suivante :

```bash
python3 --version
```

Téléchargez ensuite le projet :

```bash
git clone <url-du-depot>
cd Log_Analyzer
```

Puis installez les dépendances, si un fichier `requirements.txt` existe :

```bash
python3 -m pip install -r requirements.txt
```

## Utilisation

Placez votre fichier de logs dans le dossier du projet, puis lancez le programme depuis le terminal :

```bash
python3 main.py chemin/vers/votre-fichier.log
```

Exemple :

```bash
python3 main.py logs/application.log
```

Les résultats seront affichés dans le terminal. Certains noms de fichiers ou options peuvent varier selon la version du programme.

## Tests

Pour vérifier que le projet fonctionne correctement, lancez les tests disponibles :

```bash
python3 -m unittest discover
```

Si vous utilisez `pytest`, vous pouvez également lancer :

```bash
python3 -m pytest
```

## Limites

- Le format des fichiers de logs peut changer selon les applications.
- L’analyse peut être moins précise avec des logs mal structurés.
- Les fichiers très volumineux peuvent nécessiter plus de mémoire.
- Les fonctionnalités disponibles peuvent dépendre des fichiers présents dans le projet.

## Suite

Les prochaines améliorations possibles sont :

- Ajouter une interface graphique ou une interface web
- Exporter les résultats au format CSV ou JSON
- Filtrer les logs par date, niveau ou mot-clé
- Générer automatiquement des statistiques
- Ajouter la prise en charge de nouveaux formats de logs
- Écrire davantage de tests
# Log-Analyzer
