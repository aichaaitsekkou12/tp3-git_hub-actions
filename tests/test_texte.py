

import pytest
from app.texte import nettoyer_texte
@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR   monde  ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("", ""),
    ("     ", ""),
    ("PYTHON", "python"),
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu


def test_nettoyer_texte_entree_invalide():
    with pytest.raises(TypeError):
        nettoyer_texte(123)
def test_nettoyer_texte_none():
    with pytest.raises(TypeError):
        nettoyer_texte(None)


def test_nettoyer_texte_deja_nettoye():
    texte = "bonjour monde"
    resultat = nettoyer_texte(nettoyer_texte(texte))
    assert resultat == texte
