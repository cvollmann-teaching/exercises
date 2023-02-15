def rot13(message):
    assert type(message) == type("")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotmessage = ""
    for character in message:
        characterposition = alphabet.find(character)
        if characterposition >= 0:
            shiftedposition = (characterposition + 13) % 26
            character = alphabet[shiftedposition]
        rotmessage += character
    return rotmessage

def test_rot13():
    assert rot13('TEXT') == 'GRKG'
    assert rot13('GRKG') == 'TEXT'
    assert rot13(' 1j!fhdG') == ' 1j!fhdT'
