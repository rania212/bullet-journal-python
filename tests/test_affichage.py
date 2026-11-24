"""Tests des fonctions d'affichage du Bullet Journal."""

from datetime import date

from bullet_journal.affichage import (
    afficher_entree,
    afficher_entrees,
    afficher_journal_jour,
    afficher_journal_mois,
    afficher_taches_en_cours
)
from bullet_journal.entrees import Tache, Evenement, Note
from bullet_journal.journal import Journal


def test_afficher_tache():
    """Vérifie l'affichage d'une tâche."""
    tache = Tache("Réviser", "Python")

    assert afficher_entree(tache) == "• Réviser"


def test_afficher_evenement():
    """Vérifie l'affichage d'un événement."""
    evenement = Evenement("Réunion", "Projet", date(2026, 11, 21))

    assert afficher_entree(evenement) == "○ Réunion"


def test_afficher_note():
    """Vérifie l'affichage d'une note."""
    note = Note("Idée", "Projet")

    assert afficher_entree(note) == "– Idée"


def test_afficher_signifiant():
    """Vérifie l'affichage d'une priorité."""
    tache = Tache("Réviser", "Python")
    tache.ajouter_signifiant("*")

    assert afficher_entree(tache) == "* • Réviser"


def test_afficher_entrees():
    """Vérifie l'affichage de plusieurs entrées."""
    tache = Tache("Réviser", "Python")
    note = Note("Idée", "Projet")

    resultat = afficher_entrees([tache, note])

    assert resultat == "• Réviser\n– Idée"


def test_afficher_jour():
    """Vérifie l'affichage d'une journée."""
    journal = Journal()
    jour = date(2026, 11, 21)
    tache = Tache("Réviser", "Python", date_log=jour)
    journal.ajouter(tache)

    resultat = afficher_journal_jour(journal, jour)

    assert "21/11/2026" in resultat
    assert "• Réviser" in resultat


def test_afficher_jour_vide():
    """Vérifie l'affichage d'une journée vide."""
    journal = Journal()

    resultat = afficher_journal_jour(journal, date(2026, 11, 21))

    assert "Aucune entrée" in resultat


def test_afficher_mois():
    """Vérifie l'affichage d'un mois."""
    journal = Journal()
    note = Note("Idée", "Projet", date_log=date(2026, 11, 21))
    journal.ajouter(note)

    resultat = afficher_journal_mois(journal, 2026, 11)

    assert "11/2026" in resultat
    assert "– Idée" in resultat


def test_afficher_mois_vide():
    """Vérifie l'affichage d'un mois vide."""
    journal = Journal()

    resultat = afficher_journal_mois(journal, 2026, 12)

    assert "Aucune entrée" in resultat


def test_afficher_taches_en_cours():
    """Vérifie l'affichage des tâches à faire."""
    tache1 = Tache("Réviser", "Python")
    tache2 = Tache("Travailler", "Projet")
    tache2.terminer()

    resultat = afficher_taches_en_cours([tache1, tache2])

    assert resultat == "• Réviser"


def test_afficher_taches_en_cours_vide():
    """Vérifie l'affichage sans tâche à faire."""
    note = Note("Idée", "Projet")

    resultat = afficher_taches_en_cours([note])

    assert resultat == "Aucune tâche en cours."