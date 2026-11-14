
"""Classes des entrées du Bullet Journal."""

from abc import ABC, abstractmethod
from datetime import date, time
from uuid import uuid4
import logging

from bullet_journal.exceptions import (
    NomInvalide,
    DateInvalide,
    TransitionEtatInvalide
)


logger = logging.getLogger(__name__)


class Entree(ABC):
    """Classe mère commune aux tâches, événements et notes."""

    def __init__(
        self,
        nom: str,
        description: str,
        date_log: date | None = None
    ) -> None:
        """Initialise les informations communes d'une entrée."""

        if not isinstance(nom, str) or not nom.strip():
            raise NomInvalide("Le nom ne peut pas être vide.")

        if date_log is None:
            date_log = date.today()

        if not isinstance(date_log, date):
            raise DateInvalide("La date du journal est invalide.")

        self.id = str(uuid4())
        self.nom = nom.strip()
        self.description = description
        self.date_creation = date.today()
        self.date_log = date_log
        self.signifiants: list[str] = []

    def ajouter_signifiant(self, signifiant: str) -> None:
        """Ajoute un signifiant de priorité ou d'idée."""

        if signifiant not in ("*", "!"):
            raise ValueError("Signifiant invalide.")

        if signifiant not in self.signifiants:
            self.signifiants.append(signifiant)

    @abstractmethod
    def symbole(self) -> str:
        """Retourne le symbole correspondant à l'entrée."""
        pass


class Tache(Entree):
    """Représente une tâche du Bullet Journal."""

    def __init__(
        self,
        nom: str,
        description: str,
        date_log: date | None = None
    ) -> None:
        """Crée une tâche avec l'état à faire."""

        super().__init__(nom, description, date_log)
        self._etat = "a_faire"

    @property
    def etat(self) -> str:
        """Retourne l'état actuel de la tâche."""
        return self._etat

    def _changer_etat(self, nouvel_etat: str) -> None:
        """Change l'état si la tâche est encore à faire."""

        if self._etat != "a_faire":
            logger.error(
                "Changement d'état interdit pour la tâche %s",
                self.id
            )
            raise TransitionEtatInvalide(
                "Impossible de modifier cette tâche."
            )

        self._etat = nouvel_etat
        logger.info(
            "Tâche %s : nouvel état %s",
            self.id,
            nouvel_etat
        )

    def terminer(self) -> None:
        """Marque la tâche comme terminée."""
        self._changer_etat("terminee")

    def abandonner(self) -> None:
        """Marque la tâche comme abandonnée."""
        self._changer_etat("abandonnee")

    def migrer(self) -> None:
        """Marque la tâche comme migrée."""
        self._changer_etat("migree")

    def planifier(self) -> None:
        """Marque la tâche comme planifiée."""
        self._changer_etat("planifiee")

    def symbole(self) -> str:
        """Retourne le symbole selon l'état de la tâche."""

        symboles = {
            "a_faire": "•",
            "terminee": "×",
            "migree": ">",
            "planifiee": "<",
            "abandonnee": "~"
        }

        return symboles[self._etat]


class Evenement(Entree):
    """Représente un événement du Bullet Journal."""

    def __init__(
        self,
        nom: str,
        description: str,
        date_evenement: date,
        heure: time | None = None,
        date_log: date | None = None
    ) -> None:
        """Crée un événement avec une date et une heure facultative."""

        if not isinstance(date_evenement, date):
            raise DateInvalide("La date de l'événement est invalide.")

        if heure is not None and not isinstance(heure, time):
            raise DateInvalide("L'heure de l'événement est invalide.")

        if date_log is None:
            date_log = date_evenement

        super().__init__(nom, description, date_log)
        self.date_evenement = date_evenement
        self.heure = heure

    def symbole(self) -> str:
        """Retourne le symbole d'un événement."""
        return "○"


class Note(Entree):
    """Représente une note du Bullet Journal."""

    def symbole(self) -> str:
        """Retourne le symbole d'une note."""
        return "–"
