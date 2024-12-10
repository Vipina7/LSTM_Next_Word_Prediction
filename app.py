## Import the libraries
import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import pad_sequences

## load the LSTM model
model = load_model('next_word_lstm.h5')

## Load the tokenizer
with open('tokenizer.pickle','rb') as file:
    tokenizer = pickle.load(file)

# Function to predict the next word
def predict_next_word(mmodel, tokeniszer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len - 1):]
    token_list = pad_sequences([token_list], padding = 'pre', maxlen=max_sequence_len-1)
    predicted = model.predict(token_list, verbose=0)
    predicted_word_index = np.argmax(predicted)
    for word, index in tokenizer.word_index.items():
        if predicted_word_index == index:
            return word
    return None

# Streamlit app
st.title('Next Word Prediction With LSTM')
st.caption('Trained on "The Hamlet" by Shakespeare')
inptu_text = st.text_input('Enter the sequence of words','To be or not to')
if st.button('Predict Next Word'):
    max_sequence_len = model.input_shape[1]+1
    next_word = predict_next_word(model, tokenizer, inptu_text, max_sequence_len)
    st.write(f'Next Word : {next_word}')