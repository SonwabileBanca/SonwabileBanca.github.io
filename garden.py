import spacy

# Load the English language model in spaCy
nlp = spacy.load("en_core_web_sm")

# Garden path sentences
garden_path_sentences = [
    "The man while hunting ducks also takes pictures",
    "The girl told the story was funny",
    "Mary gave the child a Band-Aid",
    "That Jill is never here hurts",
    "The cotton clothing is made of grows in Mississippi"
]

# Tokenize each sentence
tokenized_sentences = []

for sentence in garden_path_sentences:
    doc = nlp(sentence)
    tokens = [token.text for token in doc]
    tokenized_sentences.append(tokens)

# Print the tokenized sentences
for i, tokens in enumerate(tokenized_sentences):
    print(f"Sentence {i + 1}: {tokens}")

# Extract entities from each sentence
for i, doc in enumerate([nlp(sentence) for sentence in garden_path_sentences]):
    print(f"Entities in Sentence {i + 1}:")
    for ent in doc.ents:
        print(f"Entity Text: {ent.text}, Entity Label: {ent.label_}")

