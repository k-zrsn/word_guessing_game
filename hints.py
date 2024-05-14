### module for word_hint function


def word_hint(word):
    """
    Docstring:
    A function that returns a hint 
    based on the word.
    """
    if word == "iribe":
        hint = "\n\nHint: Glass building"

    elif word == "eppley":
        hint = "\n\nHint: Rec center"

    elif word == "mckeldin" or word == "hornbake":
        hint = "\n\nHint: Good place to study"

    elif word == "tawes":
        hint = "\n\nHint: Writing center"

    elif word == "armory":
        hint = "\n\nHint: ROTC"

    elif word == "atlantic":
        hint = "\n\nHint: Shares name with an ocean"

    elif word == "stamp":
        hint = "\n\nHint: Terpzone"

    elif word == "shoemaker":
        hint = "\n\nHint: Shoes"

    elif word == "jimenez":
        hint = "\n\nHint: Professor of Spanish language and literature"


    return hint