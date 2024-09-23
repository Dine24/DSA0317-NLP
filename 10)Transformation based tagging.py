corpus = [
    ["I", "want", "to", "book", "a", "flight"],
    ["the", "book", "is", "on", "the", "table"]
]

tagged_corpus = [[(word, "NOUN") for word in sentence] for sentence in corpus]

rules = [
    ("NOUN", "VERB", lambda word, prev: word == "book" and prev == "to"),
]

def apply_rules(tagged_sentence, rules):
    return [(word, next((new_tag for current_tag, new_tag, condition in rules if tag == current_tag and condition(word, tagged_sentence[i-1][0] if i > 0 else None)), tag)) for i, (word, tag) in enumerate(tagged_sentence)]

transformed_corpus = [apply_rules(sentence, rules) for sentence in tagged_corpus]

for sentence in transformed_corpus:
   print(sentence)
