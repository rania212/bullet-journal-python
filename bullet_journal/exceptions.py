
"""Exceptions personnalisées du Bullet Journal."""


class ErreurBulletJournal(Exception):
    """Classe mère des erreurs du Bullet Journal."""
    pass


class NomInvalide(ErreurBulletJournal):
    """Erreur lorsqu'une entrée possède un nom invalide."""
    pass


class DateInvalide(ErreurBulletJournal):
    """Erreur lorsqu'une date ou une heure est invalide."""
    pass


class TransitionEtatInvalide(ErreurBulletJournal):
    """Erreur lorsqu'un changement d'état est interdit."""
    pass
