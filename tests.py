from unittest import TestCase

import kipsum


class KripsumTestCase(TestCase):
    def setUp(self):
        self.kipsum = kipsum.Kipsum()

    def test_sentence(self):
        for i in range(1, 100):
            sentence = self.kipsum.sentence(i)
            split = sentence.split(' ')
            assert i == len(split), 'nb_words mismatched. {} != {}'.format(i, len(split))

    def test_sentences(self):
        for i in range(1, 100):
            sentences = self.kipsum.sentences(i)
            assert i == len(sentences), 'nb mismatched. {} != {}'.format(i, len(sentences))

            for sep in ['\n', '$', '@', '|']:
                sep_sentence = self.kipsum.sentences(i, sep)
                split = sep_sentence.split(sep)
                assert i == len(split), 'nb mismatched. {} != {}'.format(i, len(split))
