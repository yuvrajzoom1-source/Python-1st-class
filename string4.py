class WordReverser:

    def reverse_words(self, text: str) -> str:

        words = []
        for word in text.split(" "):
            if word:
                words.append(word)

        reversed_words = []
        for i in range(len(words) - 1, -1, -1):
            reversed_words.append(words[i])

        return " ".join(reversed_words)

reverser = WordReverser()
print(reverser.reverse_words("hello world python"))