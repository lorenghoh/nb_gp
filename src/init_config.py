import json

from pathlib import Path
from rich import print


def init_config():
    # Resolve file path for the project directory
    prj_d = Path(__file__).absolute().parents[1]

    print(f"Initializing {prj_d}/config.json...\n")

    config = {
        "case": "/Howard16TB/data/loh/CGILS_S6"
    }

    with open(prj_d / "config.json", "w") as json_file:
        json.dump(config, json_file, indent=4)

    print(config)


if __name__ == "__main__":
    init_config()