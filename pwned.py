import requests as req
import hashlib
import argparse


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
    i = poss.index(check)
    if i:
        print(f"You've been pwned; hash {hshd} occurs {nums[i]} times")
    else:
        print("You haven't been pwned")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Have I been pwned?")
    parser.add_argument("password")
    args = vars(parser.parse_args())

    do_check(args["password"])
