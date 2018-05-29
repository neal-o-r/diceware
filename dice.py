import secrets


def password(n_words):

        with open('diceware.txt', 'r') as f:
                contents = f.read().split('\n')[:-1]

        words = [i.split('\t')[1] for i in contents]
        password = []
        for i in range(n_words):
                w = secrets.choice(words)
                password.append(str.capitalize(w))

        return " ".join(password)

if __name__ == '__main__':
        for i in range(5):
                print(password(5))
