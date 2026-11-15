"""Tests de la gestion du journal."""

from datetime import date

import pytest

from bullet_journal.entrees import Note, Tache
from bullet_journal.journal import DailyLog, Journal, MonthlyLog


def test_ajouter_et_retrouver_une_entree():
    """Une entrée ajoutée peut être retrouvée par son identifiant."""
    journal = Journal()
    note = Note("Idée", "Ajouter une fonctionnalité", date_log=date(2026, 11, 15))

    journal.ajouter(note)

    assert journal.retrouver(note.id) is note


def test_supprimer_une_entree():
    """Une entrée supprimée ne figure plus dans le journal."""
    journal = Journal()
    note = Note("Idée", "Ajouter une fonctionnalité")
    journal.ajouter(note)

    entree_supprimee = journal.supprimer(note.id)

    assert entree_supprimee is note
    with pytest.raises(KeyError):
        journal.retrouver(note.id)


def test_filtrer_les_entrees_par_jour_et_par_mois():
    """Le journal filtre les entrées selon leur date de journal."""
    journal = Journal()
    entree_du_jour = Note("Aujourd'hui", "Travail", date_log=date(2026, 11, 15))
    entree_du_meme_mois = Note("Demain", "Travail", date_log=date(2026, 11, 16))
    entree_d_un_autre_mois = Note("Plus tard", "Travail", date_log=date(2026, 12, 1))

    for entree in (entree_du_jour, entree_du_meme_mois, entree_d_un_autre_mois):
        journal.ajouter(entree)

    assert journal.afficher_jour(date(2026, 11, 15)) == [entree_du_jour]
    assert journal.afficher_mois(2026, 11) == [
        entree_du_jour,
        entree_du_meme_mois,
    ]


def test_migrer_une_entree_vers_un_autre_jour():
    """La migration modifie la date de l'objet existant."""
    journal = Journal()
    tache = Tache("Réviser", "Python", date_log=date(2026, 11, 15))
    journal.ajouter(tache)

    journal.migrer(tache.id, date(2026, 11, 20))

    assert journal.retrouver(tache.id) is tache
    assert tache.date_log == date(2026, 11, 20)
    assert journal.afficher_jour(date(2026, 11, 15)) == []
    assert journal.afficher_jour(date(2026, 11, 20)) == [tache]


def test_daily_log_et_monthly_log():
    """Les vues quotidienne et mensuelle exposent les bons éléments."""
    journal = Journal()
    entree = Note("Idée", "Travail", date_log=date(2026, 11, 15))
    journal.ajouter(entree)

    daily_log = DailyLog(journal, date(2026, 11, 15))
    monthly_log = MonthlyLog(journal, 2026, 11)

    assert daily_log.entrees == [entree]
    assert monthly_log.entrees == [entree]


def test_ajouter_refuse_un_objet_qui_n_est_pas_une_entree():
    """Le journal n'accepte que des objets Entree."""
    with pytest.raises(TypeError):
        Journal().ajouter("pas une entrée")


def test_ajouter_refuse_un_doublon():
    """Une même entrée ne peut pas être ajoutée deux fois."""
    journal = Journal()
    note = Note("Idée", "Travail")
    journal.ajouter(note)

    with pytest.raises(ValueError):
        journal.ajouter(note)


def test_retrouver_une_entree_absente():
    """La recherche d'une entrée absente lève une erreur explicite."""
    with pytest.raises(KeyError):
        Journal().retrouver("id-inexistant")


def test_supprimer_une_entree_absente():
    """La suppression d'une entrée absente lève une erreur explicite."""
    with pytest.raises(KeyError):
        Journal().supprimer("id-inexistant")


def test_migrer_une_entree_absente():
    """La migration d'une entrée absente lève une erreur explicite."""
    with pytest.raises(KeyError):
        Journal().migrer("id-inexistant", date(2026, 11, 20))


def test_dates_invalides_du_journal():
    """Les filtres et la migration refusent des dates invalides."""
    journal = Journal()

    with pytest.raises(TypeError):
        journal.afficher_jour("demain")
    with pytest.raises(TypeError):
        journal.migrer("id-inexistant", "demain")


def test_mois_invalide():
    """Le filtre mensuel refuse un mois en dehors de 1 à 12."""
    journal = Journal()

    with pytest.raises(ValueError):
        journal.afficher_mois(2026, 13)
