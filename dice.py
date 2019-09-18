import secrets
import requests
import argparse
import sys


def get_words():

    link = "https://raw.githubusercontent.com/neal-o-r/diceware/master/diceware.txt"
    contents = requests.get(link).text.split("\n")[:-1]

    words = [i.split("\t")[1] for i in contents]
    return words


def password(words, n_words):

    password = [secrets.choice(words).capitalize() for _ in range(n_words)]
    return " ".join(password)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate passwords")
    parser.add_argument("n_passwords", type=int)
    parser.add_argument(
        "-w", "--n_words", type=int, help="how many words per password?", default=5
    )
    args = vars(parser.parse_args())

    words = get_words()

    for i in range(args["n_passwords"]):
        sys.stdout.write(password(words, args["n_words"]) + "\n")
