"""Fonctions d'affichage du Bullet Journal."""

from datetime import date

from bullet_journal.entrees import Entree, Tache
from bullet_journal.journal import Journal


def afficher_entree(entree: Entree) -> str:
    """Retourne le symbole, les signifiants et le nom d'une entrée."""
    symboles = " ".join(entree.signifiants)

    if symboles:
        return symboles + " " + entree.symbole() + " " + entree.nom

    return entree.symbole() + " " + entree.nom


def afficher_entrees(entrees: list[Entree]) -> str:
    """Retourne l'affichage de plusieurs entrées."""
    lignes = []

    for entree in entrees:
        lignes.append(afficher_entree(entree))

    return "\n".join(lignes)


def afficher_journal_jour(journal: Journal, jour: date) -> str:
    """Retourne les entrées d'une journée."""
    entrees = journal.afficher_jour(jour)
    titre = "Journal du " + jour.strftime("%d/%m/%Y")

    if not entrees:
        return titre + "\nAucune entrée pour cette journée."

    return titre + "\n" + afficher_entrees(entrees)


def afficher_journal_mois(
    journal: Journal, annee: int, mois: int
) -> str:
    """Retourne les entrées d'un mois."""
    entrees = journal.afficher_mois(annee, mois)
    titre = "Journal du mois " + str(mois) + "/" + str(annee)

    if not entrees:
        return titre + "\nAucune entrée pour ce mois."

    return titre + "\n" + afficher_entrees(entrees)


def afficher_taches_en_cours(entrees: list[Entree]) -> str:
    """Retourne uniquement les tâches qui restent à faire."""
    taches = []

    for entree in entrees:
        if isinstance(entree, Tache) and entree.etat == "a_faire":
            taches.append(entree)

    if not taches:
        return "Aucune tâche en cours."

    return afficher_entrees(taches)
