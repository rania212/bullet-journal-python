"""Tests des fonctions d'affichage du Bullet Journal."""

#On importe date pour utiliser des dates dans les tests
from datetime import date

#On importe les fonctions d'affichage qu'on veut tester
from bullet_journal.affichage import (
    afficher_entree,
    afficher_entrees,
    afficher_journal_jour,
    afficher_journal_mois,
    afficher_taches_en_cours
)

#On importe les classes necessaires pour creer les entrees
from bullet_journal.entrees import Tache, Evenement, Note
from bullet_journal.journal import Journal


def test_afficher_tache():
    """Vérifie l'affichage d'une tâche."""

    #On cree une tache pour le test
    tache = Tache("Réviser", "Python")

    #On verifie que le symbole et le nom sont corrects
    assert afficher_entree(tache) == "• Réviser"


def test_afficher_evenement():
    """Vérifie l'affichage d'un événement."""

    #On cree un evenement avec une date precise
    evenement = Evenement("Réunion", "Projet", date(2026, 11, 21))

    #On verifie que l'evenement s'affiche avec son symbole
    assert afficher_entree(evenement) == "○ Réunion"


def test_afficher_note():
    """Vérifie l'affichage d'une note."""

    #On cree une note
    note = Note("Idée", "Projet")

    #On verifie le symbole et le nom de la note
    assert afficher_entree(note) == "– Idée"


def test_afficher_signifiant():
    """Vérifie l'affichage d'une priorité."""

    #On cree une tache avec un signifiant de priorite
    tache = Tache("Réviser", "Python")
    tache.ajouter_signifiant("*")

    #On verifie que le signifiant apparait dans l'affichage
    assert afficher_entree(tache) == "* • Réviser"


def test_afficher_entrees():
    """Vérifie l'affichage de plusieurs entrées."""

    #On cree deux entrees differentes
    tache = Tache("Réviser", "Python")
    note = Note("Idée", "Projet")

    #On utilise la fonction pour afficher les deux entrees
    resultat = afficher_entrees([tache, note])

    #On verifie que les deux entrees sont sur des lignes differentes
    assert resultat == "• Réviser\n– Idée"


def test_afficher_jour():
    """Vérifie l'affichage d'une journée."""

    #On cree un journal et une date
    journal = Journal()
    jour = date(2026, 11, 21)

    #On ajoute une tache au journal pour cette date
    tache = Tache("Réviser", "Python", date_log=jour)
    journal.ajouter(tache)

    #On recupere le texte de la journee
    resultat = afficher_journal_jour(journal, jour)

    # On verifie que la date et la tache apparaissent
    assert "21/11/2026" in resultat
    assert "• Réviser" in resultat


def test_afficher_jour_vide():
    """Vérifie l'affichage d'une journée vide."""

    #On cree un journal sans entree
    journal = Journal()

    #On essaie d'afficher une journee vide
    resultat = afficher_journal_jour(journal, date(2026, 11, 21))

    #On verifie qu'un message indique qu'il n'y a aucune entree
    assert "Aucune entrée" in resultat


def test_afficher_mois():
    """Vérifie l'affichage d'un mois."""

    #On cree un journal avec une note
    journal = Journal()
    note = Note("Idée", "Projet", date_log=date(2026, 11, 21))
    journal.ajouter(note)

    #On affiche les entrees du mois de novembre
    resultat = afficher_journal_mois(journal, 2026, 11)

    #On verifie la date et la presence de la note
    assert "11/2026" in resultat
    assert "– Idée" in resultat


def test_afficher_mois_vide():
    """Vérifie l'affichage d'un mois vide."""

    #On cree un journal vide
    journal = Journal()

    #On essaie d'afficher le mois de decembre
    resultat = afficher_journal_mois(journal, 2026, 12)

    #On verifie le message pour un mois vide
    assert "Aucune entrée" in resultat


def test_afficher_taches_en_cours():
    """Vérifie l'affichage des tâches à faire."""

    #On cree deux taches
    tache1 = Tache("Réviser", "Python")
    tache2 = Tache("Travailler", "Projet")

    #On termine la deuxieme tache
    tache2.terminer()

    #On affiche uniquement les taches qui restent a faire
    resultat = afficher_taches_en_cours([tache1, tache2])

    #On verifie que seule la premiere tache apparait
    assert resultat == "• Réviser"


def test_afficher_taches_en_cours_vide():
    """Vérifie l'affichage sans tâche à faire."""

    #On cree une note, mais aucune tache
    note = Note("Idée", "Projet")

    #On essaie d'afficher les taches en cours
    resultat = afficher_taches_en_cours([note])

    #On verifie le message lorsqu'aucune tache n'est presente
    assert resultat == "Aucune tâche en cours."
