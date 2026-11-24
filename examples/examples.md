# Utiliser `analyser.py`

Le programme lit un fichier de journal et affiche les lignes qu’il contient.

## Entrée

Créez un fichier `journal.log` avec, par exemple, ces lignes :

```text
[INFO] Le serveur a démarré
[WARNING] La mémoire est presque pleine
[ERROR] La connexion a échoué
```

## Lancer le programme

Dans un terminal, placez-vous dans le dossier où se trouve `analyser.py`, puis lancez :

```bash
python analyser.py journal.log
```

Remplacez `journal.log` par le nom de votre fichier.

## Sortie

Le programme affiche le contenu du journal, par exemple :

```text
[INFO] Le serveur a démarré
[WARNING] La mémoire est presque pleine
[ERROR] La connexion a échoué
```
