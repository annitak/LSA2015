__author__ = 'annita'


if __name__=='__main__':
    source = open('pao.replies.txt', 'r')
    positive = open('positive-words.txt', 'r')
    negative = open('negative-words.txt', 'r')

    for line in source:
        for word in line:
