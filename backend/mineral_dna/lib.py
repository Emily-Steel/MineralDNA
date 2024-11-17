from abc import ABC, abstractmethod
from itertools import chain
from typing import List
from enum import Enum, auto

# Original letter dictionary
letter_dict = {
    1: ["A", "J", "S"],
    2: ["B", "K", "T"],
    3: ["C", "L", "U"],
    4: ["D", "M", "V"],
    5: ["E", "N", "W"],
    6: ["F", "O", "X"],
    7: ["G", "P", "Y"],
    8: ["H", "Q", "Z"],
    9: ["I", "R"],
}

# Inverted dictionary
letter_to_number = {}

# Fill the inverted dictionary
for number, letters in letter_dict.items():
    for letter in letters:
        letter_to_number[letter] = number

vowels = ["A", "E", "I", "O", "U", "Y"]


def origin(names, surnames, dob, results_so_far: List[int]) -> int:
    all_names = list(chain.from_iterable([names, surnames]))
    return sum([letter_to_number[name[0]] for name in all_names])


def elevation(names, surnames, dob, results_so_far: List[int]) -> int:
    all_names = list(chain.from_iterable([names, surnames]))
    return sum([letter_to_number[name[-1]] for name in all_names])


def present(names, surnames, dob, results_so_far: List[int]) -> int:
    return sum(dob)


def daily_life_decision(names, surnames, dob, results_so_far: List[int]) -> int:
    return results_so_far[0] + results_so_far[1] + results_so_far[2]


def identity(names, surnames, dob, results_so_far: List[int]) -> int:
    all_names = list(chain.from_iterable([names, surnames]))
    return sum(sum([letter_to_number[l] for l in x if l in vowels]) for x in all_names)


def interaction(names, surnames, dob, results_so_far: List[int]) -> int:
    all_names = list(chain.from_iterable([names, surnames]))
    return sum(
        sum([letter_to_number[l] for l in x if l not in vowels]) for x in all_names
    )


def communication(names, surnames, dob, results_so_far: List[int]) -> int:
    return results_so_far[4] + results_so_far[5]


def immediate_decision(names, surnames, dob, results_so_far: List[int]) -> int:
    return results_so_far[4] + results_so_far[5] + results_so_far[6]


def _first_vowel_value_in_name(name: str) -> int:
    for letter in name:
        if letter in vowels:
            return letter_to_number[letter]
    return 0


def soul(names, surnames, dob, results_so_far: List[int]) -> int:
    all_names = list(chain.from_iterable([names, surnames]))
    return sum([_first_vowel_value_in_name(name) for name in all_names])


def truth(names, surnames, dob, results_so_far: List[int]) -> int:
    all_names = list(chain.from_iterable([names, surnames]))
    return sum([sum([letter_to_number[l] for l in name]) for name in all_names])


def guidance(names, surnames, dob, results_so_far: List[int]) -> int:
    return results_so_far[3] + results_so_far[7]


def repeat_decisions(names, surnames, dob, results_so_far: List[int]) -> int:
    return results_so_far[8] + results_so_far[9] + results_so_far[10]


def experimentation(names, surnames, dob, results_so_far: List[int]) -> int:
    return results_so_far[3] + results_so_far[7] + results_so_far[11]


# Array of position functions
positions: List[callable] = [
    origin,
    elevation,
    present,
    daily_life_decision,
    identity,
    interaction,
    communication,
    immediate_decision,
    soul,
    truth,
    guidance,
    repeat_decisions,
    experimentation,
]


def reduce_value(x: int, threshold=33) -> int:
    while x > threshold:
        digits = [int(digit) for digit in str(x)]
        x = sum(digits)
    return x


def deaccentuate_characters(input_str: str) -> str:
    accents_mapping = {
        "á": "a",
        "à": "a",
        "ä": "a",
        "â": "a",
        "ã": "a",
        "å": "a",
        "é": "e",
        "è": "e",
        "ë": "e",
        "ê": "e",
        "í": "i",
        "ì": "i",
        "ï": "i",
        "î": "i",
        "ó": "o",
        "ò": "o",
        "ö": "o",
        "ô": "o",
        "õ": "o",
        "ú": "u",
        "ù": "u",
        "ü": "u",
        "û": "u",
        "ç": "c",
        "ñ": "n",
        "Á": "A",
        "À": "A",
        "Ä": "A",
        "Â": "A",
        "Ã": "A",
        "Å": "A",
        "É": "E",
        "È": "E",
        "Ë": "E",
        "Ê": "E",
        "Í": "I",
        "Ì": "I",
        "Ï": "I",
        "Î": "I",
        "Ó": "O",
        "Ò": "O",
        "Ö": "O",
        "Ô": "O",
        "Õ": "O",
        "Ú": "U",
        "Ù": "U",
        "Ü": "U",
        "Û": "U",
        "Ç": "C",
        "Ñ": "N",
    }

    # Replace accented characters using the mapping
    for accented_char, non_accented_char in accents_mapping.items():
        input_str = input_str.replace(accented_char, non_accented_char)
    return input_str


class Stones(Enum):
    ROSE_QUARTZ = auto()
    RED_JASPER = auto()
    BLUE_CALCITE = auto()
    IMPERIAL_JASPER = auto()
    EMERALD = auto()
    GARNET = auto()
    CITRINE = auto()
    OBSIDIAN = auto()
    AQUAMARINE = auto()
    RHODONITE = auto()
    CARNELIAN = auto()
    PETRIFIED_WOOD = auto()
    HEMATITE = auto()
    AMETHYST = auto()
    MALACHITE = auto()
    GREEN_OPAL = auto()
    ARAGONITE = auto()
    BLACK_MOONSTONE = auto()
    TOPAZ = auto()
    LAPIS_LAZULI = auto()
    BLACK_TOURMALINE = auto()
    QUARTZ = auto()
    AZURITE = auto()
    AMAZONITE = auto()
    SEPTARIA = auto()
    PYRITE = auto()
    GREEN_FLUORITE = auto()
    BLUE_APATITE = auto()
    SODALITE = auto()
    SMOKY_QUARTZ = auto()
    SULFUR = auto()
    LABRADORITE = auto()
    APOPHYLLITE = auto()


stone_names = [
    "Quartz rose",
    "Jaspe rouge",
    "Calcite bleue",
    "Jaspe impérial / Polychrome",
    "Emeraude",
    "Grenat almandin",
    "Citrine",
    "Obsidienne",
    "Aigue marine",
    "Rhodonite",
    "Cornaline",
    "Bois fossilisé",
    "Hématite / Fer oxydé rouge",
    "Améthyste",
    "Malachite",
    "Opale verte fossilisée",
    "Aragonite cristallisée",
    "Pierre de lune noire",
    "Topaze",
    "Lapis lazuli",
    "Tourmaline noire",
    "Cristal de roche / Quartz",
    "Azurite",
    "Amazonite",
    "Septaria / Pierre du dragon",
    "Pyrite",
    "Fluorine verte / Fluorite verte",
    "Apatite bleue",
    "Sodalite",
    "Quartz fumé",
    "Souffre",
    "Labradorite",
    "Apophyllite",
]


def calculate_mineral_DNA(names, surnames, dob):
    names = [deaccentuate_characters(x) for x in names]
    names = [x.replace("-", "") for x in names]
    surnames = [deaccentuate_characters(x) for x in surnames]
    surnames = list(chain.from_iterable([x.split("-") for x in surnames]))
    surnames = list(chain.from_iterable([x.split(" ") for x in surnames]))
    names = [x.upper() for x in names]
    surnames = [x.upper() for x in surnames]
    dob = [int(x) for x in dob.split("/")]

    result_values = []
    results = {}

    for index, position_func in enumerate(positions):
        value = position_func(names, surnames, dob, result_values)
        reduced = reduce_value(value)
        result_values.append(reduced)
        results[index + 1] = reduced

    return results
