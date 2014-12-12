import wikipedia
from textblob import TextBlob

class Article:
    """Retrieves and analyzes wikipedia articles"""

    def __init__(self, title):
        self.title = title
        self.page = wikipedia.page(title)
        self.summary = TextBlob(self.page.summary)
        self.body = TextBlob(self.page.content)

    def is_unusual_word(self, word):
        return self.body.words.count(word) < 5

    def generate_trivia_sentences(self):
        trivia_sentences = []
        for sentence in self.summary.sentences:
            trivia = self.evaluate_sentence(sentence)
            if trivia:
                trivia_sentences.append(str(trivia))

        return trivia_sentences

    def evaluate_sentence(self, sentence):
        replace_nouns = []
        for counter, tag in enumerate(sentence.tags):
            if tag[1] == 'NN':
                noun = tag[0]
                
                # Is it unusual compared to other words in this article? 
                # If not, it probably won't make for good trivia
                if not self.is_unusual_word(noun):
                    break
                
                # Is it in a noun phrase? If so, blank out everything in that phrase
                for phrase in sentence.noun_phrases:
                    if noun in phrase:
                        [replace_nouns.append(word) for word in phrase.split()]
                        break
                    else:
                        replace_nouns.append(noun)
                break
        
        if len(replace_nouns) == 0:
            # No words or phrases are unusual enough in this sentence
            # to make good trivia
            return None

        for word in replace_nouns:
            sentence = sentence.replace(word, '__________')
        return sentence
