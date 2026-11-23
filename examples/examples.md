# Exemples pour débutants

Ce document présente quelques commandes utiles pour lire et analyser un fichier de journaux (`log`).

## Exemple de fichier

Nous utilisons un fichier nommé `journal.log` contenant :

```text
2026-11-23 10:00:01 INFO  Utilisateur connecté
2026-11-23 10:01:15 ERROR Échec de connexion
2026-11-23 10:02:30 INFO  Demande reçue
2026-11-23 10:03:45 ERROR Fichier introuvable
2026-11-23 10:04:20 WARNING Mémoire faible
```

## 1. Afficher tout le contenu : `cat`

**Entrée :**

```bash
cat application.log
```

**Sortie :**

```text
2026-11-23 10:00:01 INFO  Utilisateur connecté
2026-11-23 10:01:15 ERROR Échec de connexion
2026-11-23 10:02:30 INFO  Demande reçue
2026-11-23 10:03:45 ERROR Fichier introuvable
2026-11-23 10:04:20 WARNING Mémoire faible
```

## 2. Afficher les dernières lignes : `tail`

**Entrée :**

```bash
tail -n 3 application.log
```

**Sortie :**

```text
2026-11-23 10:02:30 INFO  Demande reçue
2026-11-23 10:03:45 ERROR Fichier introuvable
2026-11-23 10:04:20 WARNING Mémoire faible
```

`-n 3` demande les trois dernières lignes.

## 3. Rechercher des erreurs : `grep`

**Entrée :**

```bash
grep "ERROR" application.log
```

**Sortie :**

```text
2026-11-23 10:01:15 ERROR Échec de connexion
2026-11-23 10:03:45 ERROR Fichier introuvable
```

`grep` affiche uniquement les lignes contenant le mot `ERROR`.

## 4. Compter les lignes : `wc`

**Entrée :**

```bash
wc -l application.log
```

**Sortie :**

```text
5 application.log
```

Le fichier contient donc cinq lignes.

## 5. Compter les mots : `wc`

**Entrée :**

```bash
wc -w application.log
```

**Sortie :**

```text
20 application.log
```

## 6. Compter les niveaux de gravité : `sort` et `uniq`

**Entrée :**

```bash
awk '{print $3}' application.log | sort | uniq -c
```

**Sortie :**

```text
      2 ERROR
      2 INFO
      1 WARNING
```

- `awk '{print $3}'` prend la troisième colonne.
- `sort` rassemble les valeurs identiques.
- `uniq -c` compte chaque valeur.

## 7. Afficher les colonnes voulues : `cut`

**Entrée :**

```bash
cut -d' ' -f1,2 application.log
```

**Sortie :**

```text
2026-11-23 10:00:01
2026-11-23 10:01:15
2026-11-23 10:02:30
2026-11-23 10:03:45
2026-11-23 10:04:20
```

Cette commande affiche la date et l'heure, présentes dans les première et deuxième colonnes.

## 8. Filtrer puis enregistrer : `grep` et redirection

**Entrée :**

```bash
grep "ERROR" application.log > erreurs.log
```

**Sortie dans le terminal :**

```text
Aucune sortie affichée
```

Le caractère `>` crée le fichier `erreurs.log` et y place les lignes trouvées.

**Contenu de `erreurs.log` :**

```text
2026-11-23 10:01:15 ERROR Échec de connexion
2026-11-23 10:03:45 ERROR Fichier introuvable
```

## 9. Lire une page à la fois : `less`

**Entrée :**

```bash
less application.log
```

**Sortie :**

Une interface permet de faire défiler le fichier avec les flèches ou la touche `Page Down`. Appuyer sur `q` quitte `less`.

## 10. Tester si une chaîne existe : `grep`

**Entrée :**

```bash
grep -q "WARNING" application.log
printf "%s\n" $?
```

**Sortie :**

```text
0
```

- `0` signifie que la chaîne a été trouvée.
- Une autre valeur signifie qu'elle est absente ou qu'une erreur s'est produite.

## 11. Trier les lignes : `sort`

**Entrée :**

```bash
sort application.log
```

**Sortie :**

```text
2026-11-23 10:00:01 INFO  Utilisateur connecté
2026-11-23 10:01:15 ERROR Échec de connexion
2026-11-23 10:02:30 INFO  Demande reçue
2026-11-23 10:03:45 ERROR Fichier introuvable
2026-11-23 10:04:20 WARNING Mémoire faible
```

Comme les lignes commencent par une date, cette commande les trie déjà dans l'ordre chronologique.

## 12. Afficher uniquement les lignes contenant une date : `grep`

**Entrée :**

```bash
grep -E "2026-11-23" application.log
```

**Sortie :**

Toutes les lignes du fichier, car chacune contient cette date.

## Récapitulatif

| Commande | Utilité | Exemple |
|---|---|---|
| `cat` | Afficher un fichier | `cat application.log` |
| `tail` | Afficher la fin | `tail -n 3 application.log` |
| `grep` | Rechercher du texte | `grep "ERROR" application.log` |
| `wc` | Compter | `wc -l application.log` |
| `sort` | Trier | `sort application.log` |
| `uniq` | Regrouper les doublons | `sort fichier.txt \| uniq -c` |
| `awk` | Sélectionner ou transformer des colonnes | `awk '{print $3}' application.log` |
| `cut` | Sélectionner des colonnes | `cut -d' ' -f1,2 application.log` |
| `less` | Lire avec navigation | `less application.log` |
