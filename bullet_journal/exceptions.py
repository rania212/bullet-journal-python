
"""Exceptions utilisées dans le Bullet Journal."""


class ErreurBulletJournal(Exception):
    """Classe de base pour les erreurs du journal."""
    pass


class NomInvalide(ErreurBulletJournal):
    """Erreur lorsque le nom d'une entrée est vide."""
    pass


class TransitionEtatInvalide(ErreurBulletJournal):
    """Erreur lorsqu'un changement d'état est interdit."""
    pass
