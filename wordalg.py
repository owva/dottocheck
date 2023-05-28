import random

def train_markov_chain(words, order=2):
    markov_chain = {}
    for word in words:
        word = ' ' * order + word
        for i in range(len(word) - order):
            seq = word[i:i+order]
            next_char = word[i+order]
            if seq not in markov_chain:
                markov_chain[seq] = []
            markov_chain[seq].append(next_char)
    return markov_chain

def generate_word(markov_chain, order=2, max_length=10):
    current_seq = random.choice(list(markov_chain.keys()))
    output = current_seq
    for _ in range(max_length):
        if current_seq not in markov_chain:
            break
        possible_chars = markov_chain[current_seq]
        next_char = random.choice(possible_chars)
        output += next_char
        current_seq = output[len(output)-order:len(output)]
    return output.strip()

# This is a simple list of words for training. In a real usage scenario, you'd want to use a much larger dataset.
words = ['apple', 'orange', 'banana', 'grape', 'pineapple', 'blueberry', 'kiwi', 'mango', 'pear', 'peach']

# Train a 2nd-order Markov Chain on these words
chain = train_markov_chain(words, 2)

# Generate some words
for _ in range(10):
    print(generate_word(chain, 2))