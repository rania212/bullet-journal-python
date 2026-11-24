
"""Tests des classes du Bullet Journal."""

from datetime import date, time

import pytest

from bullet_journal.entrees import Tache, Evenement, Note
from bullet_journal.exceptions import (
    NomInvalide,
    DateInvalide,
    TransitionEtatInvalide
)


def test_creation_tache():
    """Vérifie la création d'une tâche."""
    tache = Tache("Réviser", "Réviser Python")

    assert tache.nom == "Réviser"
    assert tache.etat == "a_faire"
    assert tache.symbole() == "•"


def test_terminer():
    """Vérifie qu'une tâche peut être terminée."""
    tache = Tache("Réviser", "Python")
    tache.terminer()

    assert tache.etat == "terminee"
    assert tache.symbole() == "×"


def test_abandonner():
    """Vérifie qu'une tâche peut être abandonnée."""
    tache = Tache("Réviser", "Python")
    tache.abandonner()

    assert tache.etat == "abandonnee"


def test_migrer():
    """Vérifie qu'une tâche peut être marquée comme migrée."""
    tache = Tache("Réviser", "Python")
    tache.migrer()

    assert tache.etat == "migree"
    assert tache.symbole() == ">"


def test_planifier():
    """Vérifie qu'une tâche peut être planifiée."""
    tache = Tache("Réviser", "Python")
    tache.planifier()

    assert tache.etat == "planifiee"
    assert tache.symbole() == "<"


def test_nom_vide():
    """Vérifie qu'un nom vide est refusé."""
    with pytest.raises(NomInvalide):
        Tache("", "Description")


def test_transition_invalide():
    """Vérifie qu'une tâche terminée ne peut pas être migrée."""
    tache = Tache("Réviser", "Python")
    tache.terminer()

    with pytest.raises(TransitionEtatInvalide):
        tache.migrer()


def test_creation_evenement():
    """Vérifie la création d'un événement."""
    evenement = Evenement(
        "Réunion",
        "Projet Python",
        date(2026, 11, 16),
        time(14, 30)
    )

    assert evenement.nom == "Réunion"
    assert evenement.date_evenement == date(2026, 11, 16)
    assert evenement.heure == time(14, 30)
    assert evenement.symbole() == "○"


def test_creation_note():
    """Vérifie la création d'une note."""
    note = Note("Idée", "Ajouter une fonctionnalité")

    assert note.nom == "Idée"
    assert note.symbole() == "–"


def test_identifiants_uniques():
    """Vérifie que deux tâches ont des identifiants différents."""
    tache1 = Tache("Réviser", "Python")
    tache2 = Tache("Réviser", "Python")

    assert tache1.id != tache2.id


def test_nom_espaces():
    """Vérifie qu'un nom contenant seulement des espaces est refusé."""
    with pytest.raises(NomInvalide):
        Tache("   ", "Description")


def test_date_log_invalide():
    """Vérifie qu'une date de journal invalide est refusée."""
    with pytest.raises(DateInvalide):
        Tache("Réviser", "Python", date_log="demain")


def test_date_evenement_invalide():
    """Vérifie qu'une date d'événement invalide est refusée."""
    with pytest.raises(DateInvalide):
        Evenement("Réunion", "Projet", "demain")


def test_heure_invalide():
    """Vérifie qu'une heure invalide est refusée."""
    with pytest.raises(DateInvalide):
        Evenement("Réunion", "Projet", date.today(), "14h")


def test_signifiant_priorite():
    """Vérifie l'ajout d'un signifiant de priorité."""
    tache = Tache("Réviser", "Python")
    tache.ajouter_signifiant("*")

    assert "*" in tache.signifiants


def test_signifiant_invalide():
    """Vérifie qu'un signifiant inconnu est refusé."""
    tache = Tache("Réviser", "Python")

    with pytest.raises(ValueError):
        tache.ajouter_signifiant("?")


def test_signifiant_sans_doublon():
    """Vérifie qu'un signifiant ne peut pas être ajouté deux fois."""
    tache = Tache("Réviser", "Python")
    tache.ajouter_signifiant("*")
    tache.ajouter_signifiant("*")

    assert tache.signifiants.count("*") == 1


def test_terminer_tache_abandonnee():
    """Vérifie qu'une tâche abandonnée ne peut pas être terminée."""
    tache = Tache("Réviser", "Python")
    tache.abandonner()

    with pytest.raises(TransitionEtatInvalide):
        tache.terminer()


def test_migrer_tache_planifiee():
    """Vérifie qu'une tâche planifiée ne peut pas être migrée."""
    tache = Tache("Réviser", "Python")
    tache.planifier()

    with pytest.raises(TransitionEtatInvalide):
        tache.migrer()


def test_modification_directe_etat():
    """Vérifie qu'on ne peut pas modifier directement l'état."""
    tache = Tache("Réviser", "Python")

    with pytest.raises(AttributeError):
        tache.etat = "terminee"
