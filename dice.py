import secrets


def password(n_words):

        with open('diceware.txt', 'r') as f:
                contents = f.read().split('\n')[:-1]

        words = [i.split('\t')[1] for i in contents]

        password = ''
        for i in range(n_words):
                random_index = secrets.choice(range(len(words)+1))
                password += str.capitalize(words[random_index])

        return password
