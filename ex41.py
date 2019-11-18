# Olivia Lee
# 11-18-19
# Learning to speak object-orientated

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://leatncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",

}
