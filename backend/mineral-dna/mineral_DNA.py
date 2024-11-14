import argparse

from abc import ABC, abstractmethod
from itertools import chain
from typing import List

# Original letter dictionary
letter_dict = {
    1: ['A', 'J', 'S'],
    2: ['B', 'K', 'T'],
    3: ['C', 'L', 'U'],
    4: ['D', 'M', 'V'],
    5: ['E', 'N', 'W'],
    6: ['F', 'O', 'X'],
    7: ['G', 'P', 'Y'],
    8: ['H', 'Q', 'Z'],
    9: ['I', 'R']
}

# Inverted dictionary
letter_to_number = {}

# Fill the inverted dictionary
for number, letters in letter_dict.items():
    for letter in letters:
        letter_to_number[letter] = number

vowels = ['A', 'E', 'I', 'O', 'U', 'Y']

class PositionRule(ABC):
    @classmethod
    @abstractmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        pass

    @classmethod
    def get_name_en(cls) -> str:
        return cls.name_en

class Origin(PositionRule):
    name_fr = "origine"
    name_en = "origin"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        all_names = list(chain.from_iterable([names, sirnames]))
        return sum([letter_to_number[name[0]] for name in all_names])


class Elevation(PositionRule):
    name_fr = ""
    name_en = "elevation"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        all_names = list(chain.from_iterable([names, sirnames]))
        return sum([letter_to_number[name[-1]] for name in all_names])


class Present(PositionRule):
    name_fr = ""
    name_en = "present"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        return sum(dob)


class DailyLifeDecision(PositionRule):
    name_fr = ""
    name_en = "daily_life_decision"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        return results_so_far[0] + results_so_far[1] + results_so_far[2]


class Identity(PositionRule):
    name_fr = ""
    name_en = "identity"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        all_names = list(chain.from_iterable([names, sirnames]))
        return sum(sum([letter_to_number[l] for l in x if l in vowels]) for x in all_names)


class Interaction(PositionRule):
    name_fr = ""
    name_en = "interaction"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        all_names = list(chain.from_iterable([names, sirnames]))
        return sum(sum([letter_to_number[l] for l in x if l not in vowels]) for x in all_names)


class Communication(PositionRule):
    name_fr = ""
    name_en = "communication"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        return results_so_far[4] + results_so_far[5]


class ImmediateDecision(PositionRule):
    name_fr = ""
    name_en = "immediate_decision"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        return results_so_far[4] + results_so_far[5] + results_so_far[6]


def first_vowel_value_in_name(name: str) -> int:
    for letter in name:
        if letter in vowels:
            return letter_to_number[letter]
    return 0

class Soul(PositionRule):
    name_fr = ""
    name_en = "soul"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        all_names = list(chain.from_iterable([names, sirnames]))
        return sum([first_vowel_value_in_name(name) for name in all_names])


class Truth(PositionRule):
    name_fr = ""
    name_en = "truth"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        all_names = list(chain.from_iterable([names, sirnames]))
        return sum([sum([letter_to_number[l] for l in name]) for name in all_names])


class Guidance(PositionRule):
    name_fr = ""
    name_en = "guidance"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        return results_so_far[3] + results_so_far[7]


class RepeatDecisions(PositionRule):
    name_fr = ""
    name_en = "repeat_decisions"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        return results_so_far[8] + results_so_far[9] + results_so_far[10]


class Experimentation(PositionRule):
    name_fr = ""
    name_en = "experimentation"

    @classmethod
    def run_rule(cls, names, sirnames, dob, results_so_far: List[int]) -> int:
        return results_so_far[3] + results_so_far[7] + results_so_far[11]


def reduce_value(x: int, threshold=33) -> int:
    while x > threshold:
        digits = [int(digit) for digit in str(x)]
        x = sum(digits)
    return x

def remove_accents(input_str: str) -> str:
    accents_mapping = {
        'á': 'a', 'à': 'a', 'ä': 'a', 'â': 'a', 'ã': 'a', 'å': 'a',
        'é': 'e', 'è': 'e', 'ë': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i', 'ï': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'ö': 'o', 'ô': 'o', 'õ': 'o',
        'ú': 'u', 'ù': 'u', 'ü': 'u', 'û': 'u',
        'ç': 'c', 'ñ': 'n',
        'Á': 'A', 'À': 'A', 'Ä': 'A', 'Â': 'A', 'Ã': 'A', 'Å': 'A',
        'É': 'E', 'È': 'E', 'Ë': 'E', 'Ê': 'E',
        'Í': 'I', 'Ì': 'I', 'Ï': 'I', 'Î': 'I',
        'Ó': 'O', 'Ò': 'O', 'Ö': 'O', 'Ô': 'O', 'Õ': 'O',
        'Ú': 'U', 'Ù': 'U', 'Ü': 'U', 'Û': 'U',
        'Ç': 'C', 'Ñ': 'N'
    }
    
    # Replace accented characters using the mapping
    for accented_char, non_accented_char in accents_mapping.items():
        input_str = input_str.replace(accented_char, non_accented_char)
    return input_str

positions: List[PositionRule] = [
        Origin,
        Elevation,
        Present,
        DailyLifeDecision,
        Identity,
        Interaction,
        Communication,
        ImmediateDecision,
        Soul,
        Truth,
        Guidance,
        RepeatDecisions,
        Experimentation,
    ]

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
    names = [remove_accents(x) for x in names]
    surnames = [remove_accents(x) for x in surnames]
    surnames = list(chain.from_iterable([x.split("-") for x in surnames]))
    surnames = list(chain.from_iterable([x.split(" ") for x in surnames]))
    names = [x.upper() for x in names]
    surnames = [x.upper() for x in surnames]
    dob = [int(x) for x in dob.split("/")]

    result_values = []
    results = []

    for position in positions:
        value = position.run_rule(names, surnames, dob, result_values)
        reduced = reduce_value(value)
        name = position.get_name_en()
        stone_name = stone_names[reduced - 1]
        result_values.append(reduced)
        results.append([name, stone_name])

    return results