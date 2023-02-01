import argparse
from core.large_language_models.verify_codex import verify_single_sample
from dotenv import dotenv_values

config = dotenv_values(".env")

parser = argparse.ArgumentParser(
    prog="verify", description='Run unit tests')
parser.add_argument("--id", "-i", required=True, help="The bug id")
parser.add_argument("--working_directory", "-w",
                    required=True, help="The working directory")


if __name__ == "__main__":
    args = parser.parse_args()
    # TODO:
    id_start = 0
    id_end = 0
    if args.id != None:
        id_range = args.id.split('-')
        id_start = int(id_range[0])
        id_end = int(id_range[1])

    if id_start <= id_end:
        for i in range(id_start, id_end + 1):
            print(f"Verify codex reponse with id: {i}...")
            verify_single_sample(i, args.working_directory)
