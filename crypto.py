import operator

cyphertext = "GUKYDQUZGHKSIKZVDLJKDSDAJSBIOJKAJJUOSBZGIZUCULBDOUKIZAYVGDKZHSSXDASJJDZHLUNLUZZDIOODAOXUZGIZZGDANGXDEEIIKHKIHJXDEEIUSUCUOZBDOUBUILKHKMILZDDKGDLZIZHEUZDKYUOJIEDONBDAZGHKHKZGUUOJJDZHIENDHONJDZHIESUICHONODVJDZNDDJRBUGUKZUYYUJJDVOIOJCIOHKGUJJDZZGULUVIKIRSHOJHONMSIKGDMSHNGZXDEEIIOJZGUNAUKZKISSRSHOQUJJDZVGUOZGUBDYUOUJZGUHLUBUKRHSRDVIKODVGULUZDRUKUUOJDZDOUGAOJLUJIOJMDLZBMDALMSIRRULNIKZUJGDRRHZKKIZRIXQKYUUXGSUKKJDZDSJDJDYLDAJMDDZLUEDCUJGHKMUUZMLDEZGUZIRSUIOJKZIEYUJ"

testkey = {
#   new: orig
    'U': 'A', 
    'Y': 'B', 
    'V': 'C',
    'O': 'D',
    'M': 'E',
    'J': 'F',
    'H': 'G',
    'I': 'H',
    'A': 'I',
    'D': 'J',
    'S': 'K',
    'R': 'L',
    'F': 'M',
    'G': 'N',
    'N': 'O',
    'X': 'P',
    'K': 'Q',
    'B': 'R',
    'L': 'S',
    'Q': 'T',
    'E': 'U',
    'W': 'V',
    'V': 'W',
    'C': 'X',
    'P': 'Y',
    'T': 'Z' }

frequencies = { 
    'A': 0.082,
    'B': 0.015,
    'C': 0.028,
    'D': 0.043,
    'E': 0.127,
    'F': 0.022,
    'G': 0.020,
    'H': 0.061,
    'I': 0.070,
    'J': 0.002,
    'K': 0.008,
    'L': 0.040,
    'M': 0.024,
    'N': 0.067,
    'O': 0.075,
    'P': 0.019,
    'Q': 0.001,
    'R': 0.060,
    'S': 0.063,
    'T': 0.091,
    'U': 0.028,
    'V': 0.010,
    'W': 0.024,
    'X': 0.002,
    'Y': 0.020,
    'Z': 0.001 }

def getCaesarCypher(key):
    decyphered = []
    for character in cyphertext:
        decyphered.append(shiftLetter(character, key))
    return "".join(decyphered)

def shiftLetter(letter, key):
    shifted = ord(letter) + key
    if shifted > ord("Z"):
        diff = shifted - ord("Z")
        shifted = ord("A") + diff
    return chr(shifted)

def getLetterOccurrences():
    occurrences = {}
    for character in cyphertext:
        if character in occurrences:
            occurrences[character] += 1
        else:
            occurrences[character] = 1
    for key in frequencies:
        if key not in occurrences:
            occurrences[key] = 0
    return occurrences

def replaceLetter(original, new, text):
    newtext = []
    for i in range(len(cyphertext)):
        if cyphertext[i] == text[i] and text[i] == original:
            newtext.append(new)
        else:
            newtext.append(text[i])
    return "".join(newtext)

def getMapping():
    occurrences = getLetterOccurrences()
    sortedfreq = sorted(frequencies.items(), key=operator.itemgetter(1))
    sortedoccur = sorted(occurrences.items(), key=operator.itemgetter(1))
    mapping = {}
    for i in range(len(frequencies)):
        mapping[sortedfreq[i][0]] = sortedoccur[i][0]
    print sortedfreq[::-1]
    print sortedoccur[::-1]
    print mapping
    return mapping

def getMonoalphabeticCypher():
    mapping = getMapping()
    text = cyphertext
    for key, value in testkey.iteritems():
        text = replaceLetter(value, key, text)
    return text

def findSubstring(substr):
    return cyphertext.count(substr)

def main():
    print "Original text: " + '\n' + cyphertext
    print findSubstring("XDEEI")
    print getMonoalphabeticCypher()
#    for i in range(3, 26):
#        print '\n'
#        print getCaesarCypher(i)

if __name__ == "__main__":
    main()
