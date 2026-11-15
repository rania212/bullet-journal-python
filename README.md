# Bullet Journal - Bibliothèque Python

## Présentation du projet
Ce projet est réalisé dans le cadre de notre formation en école d'ingénieur à CY Tech.

L'objectif est de développer une bibliothèque Python permettant de gérer un **Bullet Journal**, un outil d'organisation personnelle qui permet de suivre ses tâches, ses événements et ses notes.

Contrairement à une simple To-Do List, le Bullet Journal permet également de gérer l'évolution des tâches : les terminer, les reporter à une autre date, les planifier ou les abandonner.

La bibliothèque a pour objectif d'être réutilisable dans différentes applications Python,
sans dépendre d'une interface graphique.

## Fonctionnalités du projet
Le projet est organisé en trois niveaux de développement.

**Niveau 1 — Fonctionnalités de base**

- Ajouter, terminer et supprimer des tâches.
- Afficher les tâches en cours.
- Gérer les différents états d'une tâche.
- Gérer les tâches, événements et notes.

**Niveau 2 — Organisation du Bullet Journal**

- Organiser les entrées dans des journaux quotidiens et mensuels.
- Migrer une entrée existante vers une autre date sans la recréer.
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

Les tests couvrent les entrées, la gestion du journal, les filtres par date,
la migration et les erreurs d'utilisation.

## Organisation du projet
Le code est organisé en plusieurs modules afin de séparer les responsabilités :

- `bullet_journal/entrees.py` : classes `Entree`, `Tache`, `Evenement` et `Note`.
- `bullet_journal/exceptions.py` : exceptions personnalisées liées aux entrées.
- `bullet_journal/journal.py` : classes `Journal`, `DailyLog` et `MonthlyLog`.
- `tests/` : tests unitaires pytest.

Le projet utilise la programmation orientée objet, notamment les classes,
l'héritage et les classes abstraites.

## Utilisation du journal

Les entrées sont créées avec une date de journal, puis ajoutées à un objet
`Journal`. Les méthodes d'affichage retournent des listes d'objets, afin de
laisser une éventuelle interface choisir la façon de les présenter.

```python
from datetime import date

from bullet_journal.entrees import Note, Tache
from bullet_journal.journal import DailyLog, Journal, MonthlyLog

journal = Journal()

tache = Tache(
    "Réviser Python",
    "Revoir les classes",
    date_log=date(2026, 11, 15),
)
note = Note(
    "Idée",
    "Ajouter une recherche",
    date_log=date(2026, 11, 20),
)

journal.ajouter(tache)
journal.ajouter(note)

entree = journal.retrouver(tache.id)
entrees_du_jour = journal.afficher_jour(date(2026, 11, 15))
entrees_du_mois = journal.afficher_mois(2026, 11)

daily_log = DailyLog(journal, date(2026, 11, 15))
monthly_log = MonthlyLog(journal, 2026, 11)

# La même entrée est déplacée, sans être recréée.
journal.migrer(tache.id, date(2026, 11, 16))
```

Les opérations `retrouver`, `supprimer` et `migrer` lèvent une `KeyError`
lorsque l'identifiant demandé n'existe pas. Les dates et mois invalides
lèvent une `TypeError` ou une `ValueError`.

## Équipe du projet

- **BOUSFIHA Rania**
- **HALIL Kenza**
- **HIDAYA**
