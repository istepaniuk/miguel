# -*- coding: utf-8 -*-

from syllabificator import Syllabificator
from expects import * #noqa


with description("Syllabificator"):
    with before.each:
        self.syllabificator = Syllabificator()

    with it("an empty string has no syllabes"):
        result = self.syllabificator.separate("")

        expect(result).to(be_empty)

    with it("a word with one syllabe returns that part"):
        result = self.syllabificator.separate("si")

        expect(result).to(equal(["si"]))

    with it("can separate words with many syllabes"):
        result = self.syllabificator.separate(u"estación")

        expect(result).to(equal(["es", "ta", u"ción"]))

    with it("can separate words with hiatus"):
        result = self.syllabificator.separate(u"melodía")

        expect(result).to(equal(["me", "lo", u"dí", "a"]))

    with it("correctly separates dipthongs when needed"):
        tests = {
            u"amarte": [u"a", u"mar", u"te"],
            u"partirte": [u"par", u"tir", u"te"],
            u"quererte": [u"que", u"rer", u"te"],
            u"cruel": [u"cruel"],
            u"amor": [u"a", u"mor"],
            u"yo": [u"yo"],
            u"igual": [u"i", u"gual"],
            u"soy": [u"soy"],
            u"odio": [u"o", u"dio"],
            u"odiar": [u"o", u"diar"],
            u"odioso": [u"o", u"dio", u"so"],
            u"odiado": [u"o", u"dia", u"do"],
            u"muy": [u"muy"],
            u"baile": [u"bai", u"le"],
            u"cuidado": [u"cui", u"da", u"do"],
            u"vahído": [u"va", u"hí", u"do"],
            u"guayaba": [u"gua", u"ya", u"ba"],
            u"estudiéis": [u"es", u"tu", u"diéis"],
            u"fluorescente": [u"fluo", u"res", u"cen", u"te"],
            u"frío": [u"frí", u"o"],
            u"patriótico": [u"pa", u"trió", u"ti", u"co"],
        }

        for example in tests.keys():
            result = self.syllabificator.separate(example)
            expect(result).to(equal(tests[example]))
