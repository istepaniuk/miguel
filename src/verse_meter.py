# -*- coding: utf8 -*-
import re


class VerseMeter(object):
    def __init__(self, syllabificator):
        self._syllabificator = syllabificator

    def measure(self, s):
        return len(self.split(s))

    def split(self, s):
        words = re.split(r" |,|\*|\n", s)
        syllabes = []
        for word in words:
            if not word:
                continue
            new_syllabes = self._syllabificator.separate(word)
            syllabe_left = syllabes[-1] if syllabes else None
            syllabe_right = new_syllabes[0] if new_syllabes else None
            if self._should_join(syllabe_left, syllabe_right):
                syllabes[-1] = syllabe_left + syllabe_right
                del new_syllabes[0]
            syllabes = syllabes + new_syllabes
        return syllabes

    def _should_join(self, left, right):
        if not left and right:
            return False
        vowels = u"aeiouáéíóú"
        if right.startswith("h"):
            right = right[1:]
        return (left[-1] in vowels or left == 'y') \
            and (right[0] in vowels or right == 'y')
