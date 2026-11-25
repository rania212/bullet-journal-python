"""Tests de la configuration des logs."""

#On importe le module qui permet de gerer les logs
import logging

#On importe la fonction que l'on veut tester
from bullet_journal.configuration_logs import configurer_logs


def test_configuration_logs(tmp_path):
    """Vérifie la création et le contenu des fichiers de logs."""

    #On configure les logs dans un dossier temporaire
    configurer_logs(str(tmp_path))

    #On recupere le logger du projet
    logger = logging.getLogger("bullet_journal")

    #On envoie deux messages pour verifier les fichiers
    logger.debug("Message de test")
    logger.error("Erreur de test")

    #On s'assure que les messages sont bien ecrits
    for handler in logger.handlers:
        handler.flush()

    #On indique les chemins des deux fichiers de logs
    debug = tmp_path / "debug.log"
    erreurs = tmp_path / "erreurs.log"

    #On verifie que les deux fichiers existent
    assert debug.exists()
    assert erreurs.exists()

    #On verifie que les messages sont bien enregistres
    assert "Message de test" in debug.read_text(encoding="utf-8")
    assert "Erreur de test" in erreurs.read_text(encoding="utf-8")

    #On ferme les fichiers pour terminer proprement le test
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()
