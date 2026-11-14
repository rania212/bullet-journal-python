# Bullet Journal — Bibliothèque Python

## Présentation du projet
Ce projet est réalisé dans le cadre de notre formation en école d'ingénieur à CY Tech.

L'objectif est de développer une bibliothèque Python permettant de gérer un **Bullet Journal**, un outil d'organisation personnelle qui permet de suivre ses tâches, ses événements et ses notes.

Contrairement à une simple To-Do List, le Bullet Journal permet également de gérer l'évolution des tâches : les terminer, les reporter à une autre date, les planifier ou les abandonner.

La bibliothèque a pour objectif d'être réutilisable dans différentes applications Python.

## Fonctionnalités du projet
Le projet est organisé en trois niveaux de développement.

**Niveau 1 — Fonctionnalités de base**

- Ajouter, terminer et supprimer des tâches.
- Afficher les tâches en cours.
- Gérer les différents états d'une tâche.
- Gérer les tâches, événements et notes.

**Niveau 2 — Organisation du Bullet Journal**

- Organiser les entrées dans des journaux quotidiens et mensuels.
- Reporter les tâches non terminées vers une autre date.
- Gérer les signifiants de priorité et d'idée.
- Afficher les symboles du Bullet Journal.

**Niveau 3 — Fonctionnalités supplémentaires**

- Planifier des tâches dans un Future Log.
- Gérer des collections personnalisées et un index.
- Sauvegarder et recharger les données au format JSON.
- Exporter les journaux au format Markdown.
- Rechercher des entrées selon différents critères.

Les niveaux 1 et 2 constituent notre objectif principal. Le niveau 3 pourra être développé en fonction de l'avancement du projet.

## Technologies et outils

- **Python** : développement de la bibliothèque.
- **Git et GitHub** : gestion des versions et travail collaboratif.
- **pytest** : réalisation des tests unitaires.
- **logging** : journalisation des actions et des erreurs.
- **GitHub Actions** : automatisation des vérifications du code.
- **Sphinx** : génération possible de la documentation.

Le développement est réalisé avec Visual Studio Code.

## Prérequis
Pour installer et utiliser le projet, il faut disposer de :

- Python 3.10 ou une version plus récente compatible.
- Git.
- Un gestionnaire d'environnement Python (`venv` ou Anaconda).
- Un terminal pour exécuter les commandes.

## Installation
**1. Cloner le dépôt GitHub**

```bash
git clone https://github.com/rania212/bullet-journal-python.git
cd bullet-journal-python
```

**2. Créer un environnement virtuel**

```bash
python -m venv .venv
```

**3. Installer les dépendances**

Sous Windows :

```bash
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Sous Linux ou macOS :

```bash
.venv/bin/python -m pip install -r requirements.txt
```

## Tests
Le projet utilise pytest pour vérifier le bon fonctionnement des différentes fonctionnalités.

Pour exécuter les tests :

```bash
python -m pytest -v
```

Les tests seront complétés au fur et à mesure du développement.

## Organisation du projet
Le code est organisé en plusieurs modules afin de séparer les responsabilités : gestion des entrées, organisation du journal, exceptions et tests.

Le projet utilise la programmation orientée objet, notamment les classes, l'héritage et les classes abstraites.

L'architecture détaillée et les exemples d'utilisation seront ajoutés lorsque les différentes parties du projet seront intégrées.

## Équipe du projet

- **BOUSFIHA Rania**
- **HALIL Kenza**
- **HIDAYA**


# Équipe du projet
BOUSFIHA Rania
HALIL Kenza
HIDAYA