# -*- coding: utf-8 -*-

import pyphen
import re

class Syllabificator(object):
    exceptions = {
        u'amarte': [u'a', u'mar', u'te'],
        u'amor': [u'a', u'mor'],
        u'azul': [u'a', u'zul'],
        u'amar': [u'a', u'mar'],
        u'amarnos': [u'a', u'mar', u'nos'],
        u'alimento': [u'a', u'li', u'men', u'to'],
        u'eterna': [u'e', u'ter', u'na'],
        u'odiar': [u'o', u'diar'],
        u'odio': [u'o', u'dio'],
        u'odioso': [u'o', u'dio', u'so'],
        u'odiado': [u'o', u'dia', u'do'],
        u'sino': [u'si', u'no'],
        u'senos': [u'se', u'nos'],
        u'igual': [u'i', u'gual'],
        u'ilusión': [u'i', u'lu', u'sión'],
        u'odiándote': [u'o', u'dián', u'do', u'te'],
    }

    def __init__(self):
        self._dic = pyphen.Pyphen(lang='es')

    def separate(self, s):
        if s.lower() in self.exceptions.keys():
            return list(self.exceptions[s.lower()])
        separator = "|"
        syllabes = self._dic.inserted(s, separator)
        syllabes = syllabes.split(separator)
        syllabe_lists = [self._break_dipthong(syllabe) for syllabe in syllabes]
        syllabes = [i for syllabe in syllabe_lists for i in syllabe]
        return syllabes if s else []

    def _break_dipthong(self, s):
        strong_vowels = set(u"aeoáéíóú")
        weak_vowels = set(u"iuü")
        if len(s) <= 1:
            return [s]

        weak_vowel_count = sum(map(s.count, weak_vowels))
        strong_vowel_count = sum(map(s.count, strong_vowels))
        if weak_vowel_count:
            return [s]

        if strong_vowel_count > 1:
            return list(self._split_after_separators(s, strong_vowels))

        return [s]

    def _split_after_separators(self, s, separators):
        acc = ""
        for ch in s:
            acc = acc + ch
            if ch in separators:
                yield acc
                acc = ""
        if acc:
            yield acc


