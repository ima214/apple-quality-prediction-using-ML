import streamlit as st
import pickle
from PIL import Image
def main():
    st.title("APPLE QUALITY PREDICTION")
    image=Image.open("apple.jpg")
    st.image(image,width=600)
    size=st.text_input("size","type here")
    weight=st.text_input("weight","type here")
    sweetness=st.text_input("sweetness","type here")
    crunchiness=st.text_input("crunchiness","type here")
    juiciness=st.text_input("juiciness","type here")
    ripeness=st.text_input("ripeness","type here")
    acidity=st.text_input("acidity","type here")
    features=[size,weight,sweetness,crunchiness,juiciness,ripeness,acidity]
    model=pickle.load(open("model2.sav","rb"))
    scaler=pickle.load(open("sacler2.sav","rb"))
    pred=st.button("predict")
    if pred:
        prediction=model.predict(scaler.transform([features]))
        if prediction==0:
            st.write("the apple quality is bad")
        else:
            st.write("the apple quality is good")
main()