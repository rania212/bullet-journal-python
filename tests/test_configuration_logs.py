"""Tests de la configuration des logs."""

import logging

from bullet_journal.configuration_logs import configurer_logs


def test_configuration_logs(tmp_path):
    """Vérifie la création et le contenu des fichiers de logs."""
    configurer_logs(str(tmp_path))

    logger = logging.getLogger("bullet_journal")
    logger.debug("Message de test")
    logger.error("Erreur de test")

    for handler in logger.handlers:
        handler.flush()

    debug = tmp_path / "debug.log"
    erreurs = tmp_path / "erreurs.log"

    assert debug.exists()
    assert erreurs.exists()
    assert "Message de test" in debug.read_text(encoding="utf-8")
    assert "Erreur de test" in erreurs.read_text(encoding="utf-8")

    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()