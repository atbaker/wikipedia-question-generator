from nltk.corpus import wordnet as wn
from textblob import TextBlob

import wikipedia

class Article:
    """Retrieves and analyzes wikipedia articles"""

    def __init__(self, title):
        self.page = wikipedia.page(title)
        self.summary = TextBlob(self.page.summary)
        self.body = TextBlob(self.page.content)

    def generate_trivia_sentences(self):
        sentences = self.summary.sentences

        # Remove the first sentence - it's never a good one
        del sentences[0]

        trivia_sentences = []
        for sentence in sentences:
            trivia = self.evaluate_sentence(sentence)
            if trivia:
                trivia_sentences.append(trivia)

        return trivia_sentences

    def get_similar_words(self, word):
        # In the absence of a better method, take the first synset
        synset = wn.synsets(word, pos='n')[0]

        # Get the hypernym for this synset (again, take the first)
        hypernym = synset.hypernyms()[0]

        # Get some hyponyms from this hypernym
        hyponyms = hypernym.hyponyms()

        # Take the name of the first lemma for the first 8 hyponyms
        similar_words = []
        for hyponym in hyponyms:
            similar_word = hyponym.lemmas()[0].name().replace('_', ' ')
            
            if similar_word != word:
                similar_words.append(similar_word)

            if len(similar_words) == 8:
                break

        return similar_words

    def evaluate_sentence(self, sentence):
        if sentence.tags[0][1] == 'RB':
            # This sentence starts with an adverb, and probably won't be a good fit
            return None

        tag_map = {word.lower(): tag for word, tag in sentence.tags}

        replace_nouns = []
        for word, tag in sentence.tags:
            # For now, only blank out non-proper nouns
            if tag == 'NN':
                # Is it in a noun phrase? If so, blank out everything in that phrase
                for phrase in sentence.noun_phrases:
                    if phrase[0] == '\'':
                        # If it starts with an apostrophe, ignore it
                        break

                    if word in phrase:
                        [replace_nouns.append(phrase_word) for phrase_word in phrase.split()]
                    else:
                        replace_nouns.append(word)
                    break
                break
        
        if len(replace_nouns) == 0:
            return None

        trivia = {
            'title': self.page.title,
            'answer': ' '.join(replace_nouns)
        }

        if len(replace_nouns) == 1:
            trivia['similar_words'] = self.get_similar_words(replace_nouns[0])
        else:
            trivia['similar_words'] = []

        for word in replace_nouns:
            sentence = sentence.replace(word, '__________')

        trivia['question'] = str(sentence)
        return trivia
