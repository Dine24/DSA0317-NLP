import nltk
from nltk.parse.earleychart import EarleyChartParser
from nltk.grammar import CFG

# Define your grammar
grammar = CFG.fromstring("""
    S  -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the'
    N  -> 'cat' | 'dog'
    V  -> 'chased' | 'saw'
""")

# Create an EarleyChartParser with the defined grammar
parser = EarleyChartParser(grammar)

# Define your input sentence
sentence = "the cat chased the dog".split()

# Parse the sentence
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()        
