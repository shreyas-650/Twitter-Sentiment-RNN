import numpy as np
import streamlit as st
import tensorflow
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

#Loading the TensorFlow Model for Prediction

model = load_model('model.h5')

with open('tokenizer.pkl','rb') as file:
    tok = pickle.load(file)

st.title('Tweet Sentiment Analysis')
text = st.text_area('Enter The Tweet: ')
if st.button('Predict Sentiment') and text.strip():
    sequence = tok.texts_to_sequences([text])
    sequence = pad_sequences(sequence,padding='post',maxlen=100)

    prediction = model.predict(sequence)
    prediction_class = np.argmax(prediction,axis=1)[0]

    sentiment_map={0:'Negative',1:'Neutral',2:'Positive'}
    st.write('Sentiment:',sentiment_map[prediction_class])
    
