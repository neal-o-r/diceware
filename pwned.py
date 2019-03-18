import requests as req
import hashlib
import argparse
import sys


def query(prefix):
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    ret = req.get(url).content

    make_split = lambda x: x.decode("utf8").split(":")
    split = [make_split(r) for r in ret.split()]

    return list(zip(*split))


def get_sha(password):

    sha1 = hashlib.sha1()
    sha1.update(bytes(password, "utf-8"))
    return sha1.hexdigest().upper()


def do_check(password):

    hshd = get_sha(password)
    q, check = hshd[:5], hshd[5:]

    poss, nums = query(q)
    if check in poss:
        i = poss.index(check)
        print(f"You've been pwned; {password} (hash {hshd}) occurs {nums[i]} times")
    else:
        print(f"You haven't been pwned with {password}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Have I been pwned?")
    parser.add_argument("password", nargs="?", default=None)
    args = vars(parser.parse_args())

    if args["password"] is None:
        password = sys.stdin.readline().rstrip()
        do_check(password)
    else:
        do_check(args["password"])
