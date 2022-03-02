import urllib.request
from bullscows import ask, gameplay, inform
import argparse


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('glossary', type=str)
    arg_parser.add_argument('length', type=int, nargs='?', default=5)
    args = arg_parser.parse_args()

    words_any_length = [word.decode('utf-8').strip() for word in urllib.request.urlopen(args.glossary)]
    word_len = args.length

    words = list(
        filter(
            lambda x: len(x) == word_len,
            words_any_length
        )
    )

    short_ask = lambda: ask("Введите слово: ", words)
    short_inform = lambda b, c: inform("Быки: {}, Коровы: {}", b, c)

    gameplay(short_ask, short_inform, words)
