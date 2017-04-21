# -*- coding: utf-8 -*-

from syllabificator import Syllabificator
from verse_meter import VerseMeter
from expects import * #noqa


with description("Verse meter"):
    with before.each:
        self.meter = VerseMeter(Syllabificator())

    with it("can measure the metric of a verse with one word"):
        result = self.meter.measure("si")

        expect(result).to(equal(1))

    with it("can measure the metric of a verse with independent words"):
        result = self.meter.measure("si soy yo")

        expect(result).to(equal(3))

    with it("can measure the metric of a verse with joined words"):
        result = self.meter.measure("aire helado")

        expect(result).to(equal(4))

    with it("can measure the metric of neruda soneto LXVI"):
        tests = {
            u"No te quiero sino porque te quiero": 11,
            u"y de quererte a no quererte llego": 11,
            u"y de esperarte cuando no te espero": 11,
            u"pasa mi corazón del frío al fuego.": 11,

            u"Te quiero sólo porque a ti te quiero,": 11,
            u"te odio sin fin, y odiándote te ruego,": 11,
            u"y la medida de mi amor viajero": 11,
            u"es no verte y amarte como un ciego.": 11,

            u"Tal vez consumirá la luz de enero,": 11,
            u"su rayo cruel, mi corazón entero,": 11,
            u"robándome la llave del sosiego.": 11,

            u"En esta historia sólo yo me muero": 11,
            u"y moriré de amor porque te quiero,": 11,
            u"porque te quiero, amor, a sangre y fuego.": 11,
        }

        for verse, metric in tests.items():
            result = self.meter.measure(verse)
            expect(result).to(equal(metric))

