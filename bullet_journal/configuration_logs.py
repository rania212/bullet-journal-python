"""Configuration des logs du Bullet Journal."""

#Module pour enregistrer les messages et les erreurs
import logging

#Permet de creer et manipuler des chemins de fichiers
from pathlib import Path


def configurer_logs(dossier: str = "logs") -> None:
    """Configure les fichiers de debug et d'erreurs."""

    #On cree le dossier des logs s'il n'existe pas
    chemin = Path(dossier)
    chemin.mkdir(parents=True, exist_ok=True)

    #On recupere le logger du projet
    logger = logging.getLogger("bullet_journal")

    #On autorise tous les messages a partir du niveau DEBUG
    logger.setLevel(logging.DEBUG)

    #On retire les anciennes configurations pour eviter les doublons
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()

    #n choisit le format des messages enregistres
    format_logs = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    #On cree le fichier qui contient les messages de debug
    debug_handler = logging.FileHandler(chemin / "debug.log", encoding="utf-8")

    #On enregistre les messages a partir du niveau DEBUG
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(format_logs)

    #On cree un deuxieme fichier pour les erreurs
    erreur_handler = logging.FileHandler(chemin / "erreurs.log", encoding="utf-8")

    #On enregistre uniquement les erreurs et les messages plus graves
    erreur_handler.setLevel(logging.ERROR)
    erreur_handler.setFormatter(format_logs)

    #On ajoute les deux fichiers au logger
    logger.addHandler(debug_handler)
    logger.addHandler(erreur_handler)
