import json
import random
from pathlib import Path

ROOT_PATH = Path(__file__).parent
SOURCE_PATH = ROOT_PATH / 'sources'
DEFAULT_SOURCE_PATH = SOURCE_PATH / 'yechan.json'


class Kipsum:
    def __init__(self, source: dict = None, words_key: str = 'words', predicates_key: str = 'predicates'):
        self.source = source
        if self.source is None:
            with open(DEFAULT_SOURCE_PATH) as f:
                self.source = json.loads(f.read())
        self.words_key = words_key
        self.predicates_key = predicates_key

        if self.words_key not in self.source:
            raise KeyError('source has no key: {}'.format(self.words_key))
        if self.predicates_key not in self.source:
            raise KeyError('source has no key: {}'.format(self.predicates_key))

        self.source_words = self.source[self.words_key]
        self.source_predicates = self.source[self.predicates_key]

    def sentence(self, nb_words: int = 6):
        if nb_words == 0:
            return ''

        results = []
        if nb_words > 1:
            words = random.choices(self.source_words, k=nb_words - 1)
            results.extend(words)

        results.append(random.choice(self.source_predicates))
        return ' '.join(results)

    def sentences(self, nb: int = 3, sep: str = None):
        result = list([self.sentence() for _ in range(nb)])
        if sep is None:
            return result
        return sep.join(result)

    def paragraph(self, nb_sentences: int = 3):
        return self.sentences(nb_sentences, sep=' ')

    def paragraphs(self, nb: int = 3, sep: str = None):
        result = list([self.paragraph() for _ in range(nb)])
        if sep is None:
            return result
        return sep.join(result)


def sentence(nb_words: int = 6, **kwargs):
    kripsum = Kipsum(**kwargs)
    return kripsum.sentence(nb_words)


def sentences(nb: int = 3, sep: str = None, **kwargs):
    kripsum = Kipsum(**kwargs)
    return kripsum.sentences(nb, sep=sep)


def paragraph(nb_sentences: int = 3, **kwargs):
    kripsum = Kipsum(**kwargs)
    return kripsum.paragraph(nb_sentences)


def paragraphs(nb: int = 3, sep: str = None, **kwargs):
    kripsum = Kipsum(**kwargs)
    return kripsum.paragraphs(nb, sep=sep)
