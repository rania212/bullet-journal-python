"""Fonctions d'affichage du Bullet Journal."""

# On importe date pour manipuler les dates
from datetime import date

# On utilise les classes 
from bullet_journal.entrees import Entree, Tache
from bullet_journal.journal import Journal


def afficher_entree(entree: Entree) -> str:
    """Retourne le symbole, les signifiants et le nom d'une entrée."""

    # On recupere les signifiants de l'entree
    symboles = " ".join(entree.signifiants)

    # Si l'entree possede des signifiants, on les affiche
    if symboles:
        return symboles + " " + entree.symbole() + " " + entree.nom

    # Sinon, on affiche seulement le symbole et le nom
    return entree.symbole() + " " + entree.nom


def afficher_entrees(entrees: list[Entree]) -> str:
    """Retourne l'affichage de plusieurs entrées."""

    # Liste vide pour stocker les lignes a afficher
    lignes = []

    # On parcourt les entrees une par une
    for entree in entrees:
        lignes.append(afficher_entree(entree))

    # On rassemble les lignes en allant a la ligne entre chacune
    return "\n".join(lignes)


def afficher_journal_jour(journal: Journal, jour: date) -> str:
    """Retourne les entrées d'une journée."""

    # On recupere les entrees du jour 
    entrees = journal.afficher_jour(jour)

    # On prepare le titre avec la date au format: jour/mois/annee
    titre = "Journal du " + jour.strftime("%d/%m/%Y")

    # Si aucune entree n'existe pour ce jour
    if not entrees:
        return titre + "\nAucune entrée pour cette journée."

    # Sinon on affiche le titre et toutes les entrees
    return titre + "\n" + afficher_entrees(entrees)


def afficher_journal_mois(journal: Journal, annee: int, mois: int) -> str:
    """Retourne les entrées d'un mois."""

    # On recupere les entrees du mois
    entrees = journal.afficher_mois(annee, mois)

    # On prepare le titre du mois
    titre = "Journal du mois " + str(mois) + "/" + str(annee)

    # Si le mois ne contient aucune entree
    if not entrees:
        return titre + "\nAucune entrée pour ce mois."

    # Sinon, on affiche les entrees du mois
    return titre + "\n" + afficher_entrees(entrees)


def afficher_taches_en_cours(entrees: list[Entree]) -> str:
    """Retourne uniquement les tâches qui restent à faire."""

    # On cree une liste vide pour les taches a faire
    taches = []

    # On parcourt toutes les entrees
    for entree in entrees:

        # On verifie que c'est une tache et qu'elle est a faire
        if isinstance(entree, Tache) and entree.etat == "a_faire":
            taches.append(entree)

    # Si aucune tache n'est a faire
    if not taches:
        return "Aucune tâche en cours."

    # Sinon, on affiche les taches trouvees
    return afficher_entrees(taches)
