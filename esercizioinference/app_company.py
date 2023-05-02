import streamlit as st
import numpy as np
import joblib

def main():
    st.title("pred company")
    load_model=joblib.load('./modello_company.pkl')
    tv=st.number_input('inserisci investimenti in tv',1,10000,500)
    radio=st.number_input('inserisci investimenti in radio',1,10000,850,)
    newspaper=st.number_input('inserisci investimenti in newspaper',1,10000,600)
    pred=load_model.predict([[tv,radio,newspaper]])
    st.write(f"il forecast delle vendite previste con questi investimenti é: euro{round(pred[0],1)}")



if __name__ == "__main__":
    main()