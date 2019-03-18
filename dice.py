import secrets
import argparse
import sys


def password(n_words):

    with open("diceware.txt", "r") as f:
        contents = f.read().split("\n")[:-1]

    words = [i.split("\t")[1] for i in contents]
    password = []
    for i in range(n_words):
        w = secrets.choice(words)
        password.append(str.capitalize(w))

    return " ".join(password)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate passwords")
    parser.add_argument("n_passwords", type=int)
    parser.add_argument(
        "-w", "--n_words", type=int, help="how many words per password?", default=5
    )
    args = vars(parser.parse_args())

    for i in range(args["n_passwords"]):
        sys.stdout.write(password(args["n_words"]) + '\n')
