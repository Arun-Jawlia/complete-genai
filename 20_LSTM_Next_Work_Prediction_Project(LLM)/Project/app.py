# pylint: disable = all
import streamlit as st
import pickle
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# load the trained model

def load_resources():

    model = load_model('./models/next_word_model.h5')

    with open("./models/tokenizer.pkl", 'rb')as file:
        tokenizer = pickle.load(file)

    return model, tokenizer

model, tokenizer = load_resources()


reverse_index = {idx: word for word, idx in tokenizer.word_index.items() }

max_len = 44

st.title('Next Work Prediction with Deep Learning')

def generate_text(seed_text, num_words = 10): # suggest 10 words
    text = seed_text

    for _ in range(num_words):
        seq = tokenizer.texts_to_sequences([text])[0]
        padded = pad_sequences([seq], maxlen = max_len, padding='pre')
        preds = model.predict(padded, verbose = 0)
        pos = np.argmax(preds)
        next_word = reverse_index.get(pos, ' ')
        text += ' ' + next_word
        
    return text

seed = st.text_input("Enter a Starting Text: ", 'Hello')

num_words = st.slider("Number of words to generate: ", 1, 20, 10)

if st.button("Generate"):
    result = generate_text(seed, num_words)
    st.write(result)





