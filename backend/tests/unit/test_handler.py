import json
import pytest
from typing import List, Dict
from mineral_dna import app
from mineral_dna.lib import Stones

@pytest.mark.parametrize("names, surnames, dob, expected", [
    ("Julie Valerie", "Happillon", "29/09/1982", [
        Stones.HEMATITE,
        Stones.MALACHITE,
        Stones.IMPERIAL_JASPER,
        Stones.LABRADORITE,
        Stones.OBSIDIAN,
        Stones.OBSIDIAN,
        Stones.GREEN_OPAL,
        Stones.LABRADORITE,
        Stones.EMERALD,
        Stones.CITRINE,
        Stones.RHODONITE,
        Stones.QUARTZ,
        Stones.AMETHYST,
    ]),
    ("Claire", "Cattin", "30/07/1972", [
        Stones.GARNET,
        Stones.RHODONITE,
        Stones.CARNELIAN,
        Stones.GREEN_FLUORITE,
        Stones.SEPTARIA,
        Stones.GREEN_FLUORITE,
        Stones.CITRINE,
        Stones.AMETHYST,
        Stones.RED_JASPER,
        Stones.CITRINE,
        Stones.EMERALD,
        Stones.AMETHYST,
        Stones.RHODONITE,
    ]),
    ("Michelle Marie Josee Ghislaine", "Duvivier", "02/09/1968", [
        Stones.LAPIS_LAZULI,
        Stones.SODALITE,
        Stones.PYRITE,
        Stones.PETRIFIED_WOOD,
        Stones.ROSE_QUARTZ,
        Stones.AQUAMARINE,
        Stones.RHODONITE,
        Stones.LAPIS_LAZULI,
        Stones.BLUE_APATITE,
        Stones.RHODONITE,
        Stones.LABRADORITE,
        Stones.CITRINE,
        Stones.PETRIFIED_WOOD,
    ]),
    ("Nathalie Marie-Francoise", "Auzemery", "24/01/1963", [
        Stones.RHODONITE,
        Stones.ARAGONITE,
        Stones.PYRITE,
        Stones.OBSIDIAN,
        Stones.RHODONITE,
        Stones.HEMATITE,
        Stones.AZURITE,
        Stones.RHODONITE,
        Stones.BLUE_CALCITE,
        Stones.AMETHYST,
        Stones.BLACK_MOONSTONE,
        Stones.OBSIDIAN,
        Stones.PYRITE,
    ]),
    ("Sonia", "Schulz", "13/09/1984", [
        Stones.RED_JASPER,
        Stones.AQUAMARINE,
        Stones.OBSIDIAN,
        Stones.TOPAZ,
        Stones.TOPAZ,
        Stones.SODALITE,
        Stones.PETRIFIED_WOOD,
        Stones.GARNET,
        Stones.AQUAMARINE,
        Stones.PETRIFIED_WOOD,
        Stones.SEPTARIA,
        Stones.RHODONITE,
        Stones.OBSIDIAN,
    ]),
])
def test_lambda_handler(names: str, surnames: str, dob: str, expected: List[Stones]):
    event = {
        "body": json.dumps(
            {
                "userID": "test",
                "names": names,
                "surnames": surnames,
                "dob": dob,
            }
        ),
        "httpMethod": "POST"
    }
    context = {}

    response = app.lambda_handler(event, context)
    actual = json.loads(response["body"])["stones"]
    for _, k in enumerate(actual):
        actual[k] = Stones(actual[k])
    expected = dict(zip([str(x + 1) for x in range(13)], expected))

    assert response["statusCode"] == 200
    assert actual == expected
