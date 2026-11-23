from ..src import analyser


def test_filtre():
    """Garder seulement les lignes qui contiennent le mot-clé."""
    logs = ["INFO démarrage", "ERROR panne disque", "INFO arrêt"]

    resultat = analyser.filtre(logs, "ERROR")

    assert resultat == ["ERROR panne disque"]
