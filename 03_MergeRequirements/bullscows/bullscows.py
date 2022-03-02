import random
from typing import List
import textdistance


def bullscows(guess: str, secret: str) -> (int, int):
    bulls = textdistance.hamming.similarity(guess, secret)
    cows = int(textdistance.overlap.similarity(guess, secret) * len(secret))
    return bulls, cows


def ask(prompt: str, valid: List[str] = None) -> str:
    guess = input(prompt)
    if not valid:
        return guess
    while guess not in valid:
        guess = input(prompt)
    return guess


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


def gameplay(ask: callable, inform: callable, words: List[str]) -> int:
    secret = random.choice(words)
    tries = 1
    guess = ask()
    while guess != secret:
        inform(*bullscows(guess, secret))
        guess = ask()
        tries += 1

    print(f"Верно! {tries} попыток!")
