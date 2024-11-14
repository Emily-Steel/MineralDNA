import json
import pytest
from typing import List, Dict
from mineral_dna import app
from mineral_dna.lib import Stones

@pytest.mark.parametrize("names, surnames, dob, expected", [
    ("Julie Valerie", "Happillon", "29/09/1982", {
        "origin": Stones.HEMATITE,
        "elevation": Stones.MALACHITE,
        "present": Stones.IMPERIAL_JASPER,
        "daily_life_decision": Stones.LABRADORITE,
        "identity": Stones.OBSIDIAN,
        "interaction": Stones.OBSIDIAN,
        "communication": Stones.GREEN_OPAL,
        "immediate_decision": Stones.LABRADORITE,
        "soul": Stones.EMERALD,
        "truth": Stones.CITRINE,
        "guidance": Stones.RHODONITE,
        "repeat_decisions": Stones.QUARTZ,
        "experimentation": Stones.AMETHYST,
    }),
    ("Claire", "Cattin", "30/07/1972", {
        "origin": Stones.GARNET,
        "elevation": Stones.RHODONITE,
        "present": Stones.CARNELIAN,
        "daily_life_decision": Stones.GREEN_FLUORITE,
        "identity": Stones.SEPTARIA,
        "interaction": Stones.GREEN_FLUORITE,
        "communication": Stones.CITRINE,
        "immediate_decision": Stones.AMETHYST,
        "soul": Stones.RED_JASPER,
        "truth": Stones.CITRINE,
        "guidance": Stones.EMERALD,
        "repeat_decisions": Stones.AMETHYST,
        "experimentation": Stones.RHODONITE,
    }),
    ("Michelle Marie Josee Ghislaine", "Duvivier", "02/09/1968", {
        "origin": Stones.LAPIS_LAZULI,
        "elevation": Stones.SODALITE,
        "present": Stones.PYRITE,
        "daily_life_decision": Stones.PETRIFIED_WOOD,
        "identity": Stones.ROSE_QUARTZ,
        "interaction": Stones.AQUAMARINE,
        "communication": Stones.RHODONITE,
        "immediate_decision": Stones.LAPIS_LAZULI,
        "soul": Stones.BLUE_APATITE,
        "truth": Stones.RHODONITE,
        "guidance": Stones.LABRADORITE,
        "repeat_decisions": Stones.CITRINE,
        "experimentation": Stones.PETRIFIED_WOOD,
    }),
    ("Nathalie Marie-Francoise", "Auzemery", "24/01/1963", {
        "origin": Stones.RHODONITE,
        "elevation": Stones.ARAGONITE,
        "present": Stones.PYRITE,
        "daily_life_decision": Stones.OBSIDIAN,
        "identity": Stones.RHODONITE,
        "interaction": Stones.HEMATITE,
        "communication": Stones.AZURITE,
        "immediate_decision": Stones.RHODONITE,
        "soul": Stones.BLUE_CALCITE,
        "truth": Stones.AMETHYST,
        "guidance": Stones.BLACK_MOONSTONE,
        "repeat_decisions": Stones.OBSIDIAN,
        "experimentation": Stones.PYRITE,
    }),
    ("Sonia", "Schulz", "13/09/1984", {
        "origin": Stones.RED_JASPER,
        "elevation": Stones.AQUAMARINE,
        "present": Stones.OBSIDIAN,
        "daily_life_decision": Stones.TOPAZ,
        "identity": Stones.TOPAZ,
        "interaction": Stones.SODALITE,
        "communication": Stones.PETRIFIED_WOOD,
        "immediate_decision": Stones.GARNET,
        "soul": Stones.AQUAMARINE,
        "truth": Stones.PETRIFIED_WOOD,
        "guidance": Stones.SEPTARIA,
        "repeat_decisions": Stones.RHODONITE,
        "experimentation": Stones.OBSIDIAN,
    }),
])
def test_lambda_handler(names: str, surnames: str, dob: str, expected: Dict[str, int]):
    event = {
        "body": json.dumps(
            {
                "names": names,
                "surnames": surnames,
                "dob": dob,
            }
        )
    }
    context = {}

    response = app.lambda_handler(event, context)
    actual = response["body"]["stones"]
    for _, k in enumerate(actual):
        actual[k] = Stones(actual[k])

    assert response["statusCode"] == 200
    assert actual == expected
