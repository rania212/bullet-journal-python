
"""Classes pour gérer les entrées du Bullet Journal."""

from abc import ABC, abstractmethod
from datetime import date, time
from uuid import uuid4

from bullet_journal.exceptions import NomInvalide, TransitionEtatInvalide


class Entree(ABC):
    """Classe mère pour les entrées du Bullet Journal."""

    def __init__(
        self,
        nom: str,
        description: str,
        date_log: date | None = None
    ) -> None:

        if not nom.strip():
            raise NomInvalide("Le nom ne peut pas être vide.")

        self.id = str(uuid4())
        self.nom = nom
        self.description = description
        self.date_creation = date.today()

        if date_log is None:
            self.date_log = date.today()
        else:
            self.date_log = date_log

    @abstractmethod
    def symbole(self) -> str:
        """Retourne le symbole de l'entrée."""
        pass


class Tache(Entree):
    """Classe qui représente une tâche du Bullet Journal."""

    def __init__(
        self,
        nom: str,
        description: str,
        date_log: date | None = None
    ) -> None:

        super().__init__(nom, description, date_log)
        self.etat = "a_faire"

    def terminer(self) -> None:
        """Marque la tâche comme terminée."""
        if self.etat != "a_faire":
            raise TransitionEtatInvalide(
                "Cette tâche ne peut pas être terminée."
            )

        self.etat = "terminee"

    def abandonner(self) -> None:
        """Marque la tâche comme abandonnée."""
        if self.etat != "a_faire":
            raise TransitionEtatInvalide(
                "Cette tâche ne peut pas être abandonnée."
            )

        self.etat = "abandonnee"

    def migrer(self) -> None:
        """Marque la tâche comme migrée."""
        if self.etat != "a_faire":
            raise TransitionEtatInvalide(
                "Cette tâche ne peut pas être migrée."
            )

        self.etat = "migree"

    def planifier(self) -> None:
        """Marque la tâche comme planifiée."""
        if self.etat != "a_faire":
            raise TransitionEtatInvalide(
                "Cette tâche ne peut pas être planifiée."
            )

        self.etat = "planifiee"

    def symbole(self) -> str:
        """Retourne le symbole selon l'état de la tâche."""
        symboles = {
            "a_faire": "•",
            "terminee": "×",
            "migree": ">",
            "planifiee": "<",
            "abandonnee": "~"
        }

        return symboles[self.etat]

class Evenement(Entree):
    """Classe qui représente un événement du journal."""

    def __init__(
        self,
        nom: str,
        description: str,
        date_evenement: date,
        heure: time | None = None,
        date_log: date | None = None
    ) -> None:

        if date_log is None:
            date_log = date_evenement

        super().__init__(nom, description, date_log)
        self.date_evenement = date_evenement
        self.heure = heure

    def symbole(self) -> str:
        """Retourne le symbole d'un événement."""
        return "○"


class Note(Entree):
    """Classe qui représente une note du journal."""

    def symbole(self) -> str:
        """Retourne le symbole d'une note."""
        return "–"
