from programs import vowels


def test_any_vowels():
    assert vowels.vowels('vowels') == 2
    assert vowels.vowels('constant') == 2
    assert vowels.vowels('millennium') == 4


def test_any_vowels_CAPS():
    assert vowels.vowels('VOWELS') == 2
    assert vowels.vowels('CoNsTaNT') == 2
    assert vowels.vowels('MillEnnIuM') == 4