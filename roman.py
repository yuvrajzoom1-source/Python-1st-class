class RomanConverter:
    def __init__(self):

        self.romanmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def to_integer(self, romanstr):
        total = 0

        for i in range(len(romanstr)):
            currentval = self.romanmap[romanstr[i]]

            if i + 1 < len(romanstr) and currentval < self.romanmap[romanstr[i + 1]]:
                total -= currentval
            else:
                total += currentval
                
        return total 
converter = RomanConverter()

print(converter.to_integer("IX"))       
print(converter.to_integer("LVIII"))
print(converter.to_integer("MCMXCIV"))
