"""Configuration des logs du Bullet Journal."""

import logging
from pathlib import Path


def configurer_logs(dossier: str = "logs") -> None:
    """Configure les fichiers de debug et d'erreurs."""
    chemin = Path(dossier)
    chemin.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("bullet_journal")
    logger.setLevel(logging.DEBUG)

    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()

    format_logs = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    debug_handler = logging.FileHandler(
        chemin / "debug.log", encoding="utf-8"
    )
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(format_logs)

    erreur_handler = logging.FileHandler(
        chemin / "erreurs.log", encoding="utf-8"
    )
    erreur_handler.setLevel(logging.ERROR)
    erreur_handler.setFormatter(format_logs)

    logger.addHandler(debug_handler)
    logger.addHandler(erreur_handler)