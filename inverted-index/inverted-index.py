import argparse
import os
import string

path = 'documents'

def inverted_index(path, clear_punctuation=True):
    inv_index = {}

    documentNumber = 0
    for filename in os.listdir(path):
        wordPosition = 0
        with open('{}/{}'.format(path, filename)) as file:
            for line in file:
                for word in line.split():
                    if clear_punctuation:
                        word = word.translate(word.maketrans('', '', string.punctuation))

                    if word in inv_index:
                        if documentNumber in inv_index[word]:
                            inv_index[word][documentNumber] += 1
                        else:
                            inv_index[word][documentNumber] = 1
                    else:
                        inv_index[word] = {documentNumber: 1}
                    wordPosition += 1
        documentNumber += 1
    print(inv_index)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    args = parser.parse_args()
    inverted_index(args.path,)

if __name__ == '__main__':
    main()
