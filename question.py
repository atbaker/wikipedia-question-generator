def is_unusual_word(word, blob):
    return blob.words.count(word) < 5

def evaluate_sentence(sentence):
    replace_nouns = []
    for counter, tag in enumerate(sentence.tags):
        if tag[1] == 'NN':
            noun = tag[0]
            
            # Is it unusual? If not, it probably won't make for good trivia
            if not is_unusual_word(noun, body):
                break
            
            # Is it in a noun phrase? If so, replace everything in that phrase
            for phrase in sentence.noun_phrases:
                if noun in phrase:
                    [replace_nouns.append(word) for word in phrase.split()]
                    break
                else:
                    replace_nouns.append(noun)
            break
    
    if len(replace_nouns) == 0:
        # This sentence sucks!
        return None

    for word in replace_nouns:
        sentence = sentence.replace(word, '__________')
    return sentence

trivia_sentences = []

for sentence in body.sentences[:50]:
    trivia_sentence = evaluate_sentence(sentence)
    if trivia_sentence is not None:
        trivia_sentences.append(str(trivia_sentence))

import pprint
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(trivia_sentences)