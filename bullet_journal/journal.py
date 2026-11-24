"""Gestion des entrées quotidiennes et mensuelles du Bullet Journal."""

from datetime import date

from bullet_journal.entrees import Entree


class Journal:
    """Stocke et organise les entrées d'un Bullet Journal."""

    def __init__(self) -> None:
        """Initialise un journal vide."""
        self._entrees: dict[str, Entree] = {}

    def ajouter(self, entree: Entree) -> None:
        """Ajoute une entrée au journal."""
        if not isinstance(entree, Entree):
            raise TypeError("Le journal accepte uniquement des entrées.")
        if entree.id in self._entrees:
            raise ValueError("Cette entrée est déjà présente dans le journal.")
        self._entrees[entree.id] = entree

    def supprimer(self, entree_id: str) -> Entree:
        """Supprime et retourne une entrée identifiée par son id."""
        try:
            return self._entrees.pop(entree_id)
        except KeyError as exc:
            raise KeyError(f"Entrée introuvable : {entree_id}") from exc

    def retrouver(self, entree_id: str) -> Entree:
        """Retourne une entrée identifiée par son id."""
        try:
            return self._entrees[entree_id]
        except KeyError as exc:
            raise KeyError(f"Entrée introuvable : {entree_id}") from exc

    def afficher_jour(self, jour: date) -> list[Entree]:
        """Retourne les entrées rattachées à un jour donné."""
        if not isinstance(jour, date):
            raise TypeError("Le jour doit être une date.")
        return [
            entree for entree in self._entrees.values()
            if entree.date_log == jour
        ]

    def afficher_mois(self, annee: int, mois: int) -> list[Entree]:
        """Retourne les entrées rattachées à un mois donné."""
        if not isinstance(annee, int) or not isinstance(mois, int):
            raise TypeError("L'année et le mois doivent être des entiers.")
        if mois < 1 or mois > 12:
            raise ValueError("Le mois doit être compris entre 1 et 12.")
        return [
            entree for entree in self._entrees.values()
            if entree.date_log.year == annee and entree.date_log.month == mois
        ]

    def migrer(self, entree_id: str, nouvelle_date: date) -> Entree:
        """Déplace une entrée vers une nouvelle date sans la recréer."""
        if not isinstance(nouvelle_date, date):
            raise TypeError("La nouvelle date doit être une date.")
        entree = self.retrouver(entree_id)
        entree.date_log = nouvelle_date
        return entree


class DailyLog:
    """Vue des entrées d'un jour donné."""

    def __init__(self, journal: Journal, jour: date) -> None:
        """Crée une vue quotidienne liée à un journal."""
        if not isinstance(journal, Journal):
            raise TypeError("Le daily log nécessite un journal.")
        self.journal = journal
        self.jour = jour

    @property
    def entrees(self) -> list[Entree]:
        """Retourne les entrées du jour."""
        return self.journal.afficher_jour(self.jour)


class MonthlyLog:
    """Vue des entrées d'un mois donné."""

    def __init__(self, journal: Journal, annee: int, mois: int) -> None:
        """Crée une vue mensuelle liée à un journal."""
        if not isinstance(journal, Journal):
            raise TypeError("Le monthly log nécessite un journal.")
        self.journal = journal
        self.annee = annee
        self.mois = mois

    @property
    def entrees(self) -> list[Entree]:
        """Retourne les entrées du mois."""
        return self.journal.afficher_mois(self.annee, self.mois)