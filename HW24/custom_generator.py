import random
import requests


def random_words(count=0):
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    words = response.content.splitlines()

    words_count = 0
    while words_count != count:
        words_count += 1
        yield random.choice(words).decode("utf-8")


my_generator = random_words(10)
for i in my_generator:
    print(i)
