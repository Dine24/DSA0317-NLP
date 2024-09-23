import re
rules = [
    (r'\bthe\b', 'DET'),      
    (r'\ba\b', 'DET'),        
    (r'\ban\b', 'DET'),        
    (r'\b(cat|dog)\b', 'NOUN'), 
    (r'\b(sat|barked|meowed|ran)\b', 'VERB'),  
    (r'\b\w+ly\b', 'ADV'),    
    (r'\b\w+ing\b', 'VERB'),  
    (r'\b\w+ed\b', 'VERB'),   
    (r'\b\w+s\b', 'NOUN'),    
]


def rule_based_pos_tag(sentence):
    tags = []
    words = sentence.split()
    for word in words:
        tag = 'NOUN' 
        for pattern, rule_tag in rules:
            if re.fullmatch(pattern, word):
                tag = rule_tag
                break
        tags.append((word, tag))
    return tags

sentence = "the cat sat on the mat and the dog barked"
tagged_sentence = rule_based_pos_tag(sentence)
print(tagged_sentence)

