from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.analyser import 


def test_filtre():
    """Garder seulement les lignes qui contiennent le mot-clé."""
    logs = ["INFO démarrage", "ERROR panne disque", "INFO arrêt"]

    resultat = analyser.filtre("ERROR")

    assert resultat == ["ERROR panne disque"]
