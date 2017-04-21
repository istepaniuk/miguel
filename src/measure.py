from verse_meter import VerseMeter
from syllabificator import Syllabificator
import fileinput

meter = VerseMeter(Syllabificator())


for line in fileinput.input():
    line = line.decode(encoding='utf8').strip()
    if line:
        print u"-".join(meter.split(line.lower())), meter.measure(line)
