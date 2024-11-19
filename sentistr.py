import streamlit as st 
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

model = load_model("sentimodel.h5")

with open("tokenizer.pkl","rb") as handle:
    tokenizer = pickle.load(handle)
    
def predict_sentiment(input_text):
    max_len  = 200
    sequences = tokenizer.texts_to_sequences([input_text])
    padded_sequences = pad_sequences(sequences, maxlen=max_len, padding="post")
    
    
    predicition = model.predict(padded_sequences)
    sentiment = np.argmax(predicition)
    
    labels = {0:"Positive",  1:"Negative"}
    return labels[sentiment], predicition

st.title("SENTIMENTAL ANALYSIS")
st.write("Enter text to analyze its sentiment")

user_input = st.text_area("Input text", placeholder="Type your text here..")
if st.button("Predict"):
    if user_input.strip():
        sentiment, probabilities = predict_sentiment(user_input)
        st.write(f"**Predicted Sentiment:** {sentiment}")
        st.write(f"**Probabilities:** {probabilities}")
    else:
        st.error("Please enter some text to analyze.")