from unittest.mock import Mock
from app.moderation import decider


def test_message_spam():
    modele = Mock()
    modele.predict.return_value = "spam"

    resultat = decider(modele, "Offre miracle")

    assert resultat == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")


def test_message_normal():
    modele = Mock()
    modele.predict.return_value = "normal"

    resultat = decider(modele, "Bonjour")

    assert resultat == "autoriser"
    modele.predict.assert_called_once_with("Bonjour")