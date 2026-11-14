
"""Tests des classes du Bullet Journal."""

from datetime import date, time

import pytest

from bullet_journal.entrees import Tache, Evenement, Note
from bullet_journal.exceptions import (
    NomInvalide,
    TransitionEtatInvalide
)


def test_creation_tache():
    tache = Tache("Réviser", "Réviser Python")
    assert tache.nom == "Réviser"
    assert tache.etat == "a_faire"
    assert tache.symbole() == "•"


def test_terminer():
    tache = Tache("Réviser", "Python")
    tache.terminer()
    assert tache.etat == "terminee"
    assert tache.symbole() == "×"


def test_abandonner():
    tache = Tache("Réviser", "Python")
    tache.abandonner()
    assert tache.etat == "abandonnee"


def test_migrer():
    tache = Tache("Réviser", "Python")
    tache.migrer()
    assert tache.etat == "migree"
    assert tache.symbole() == ">"


def test_planifier():
    tache = Tache("Réviser", "Python")
    tache.planifier()
    assert tache.etat == "planifiee"
    assert tache.symbole() == "<"


def test_nom_vide():
    with pytest.raises(NomInvalide):
        Tache("", "Description")


def test_transition_invalide():
    tache = Tache("Réviser", "Python")
    tache.terminer()

    with pytest.raises(TransitionEtatInvalide):
        tache.migrer()


def test_creation_evenement():
    evenement = Evenement(
        "Réunion",
        "Projet Python",
        date(2026, 11, 16),
        time(14, 30)
    )

    assert evenement.nom == "Réunion"
    assert evenement.heure == time(14, 30)
    assert evenement.symbole() == "○"


def test_creation_note():
    note = Note("Idée", "Ajouter une fonctionnalité")
    assert note.nom == "Idée"
    assert note.symbole() == "–"


def test_identifiants_uniques():
    tache1 = Tache("Réviser", "Python")
    tache2 = Tache("Réviser", "Python")

    assert tache1.id != tache2.id
