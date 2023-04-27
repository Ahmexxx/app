import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def main():
    st.title('Prima App')

    urlA="https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Startup.csv"#assegno ad una variabile
    urlB="https://frenzy86.s3.eu-west-2.amazonaws.com/python/data/Company.csv"
    startup=pd.read_csv(urlA)#leggo il file
    company=pd.read_csv(urlB)#leggo il file
    st.write("startup")
    st.dataframe(startup)
    st.dataframe(startup.corr())
    #grafico1
    fig=plt.figure(figsize=(10,8))
    plt.title('startupp')
    sns.heatmap(startup.corr(),annot=True,cmap="plasma")#va a creare una tabella con una palet di colori in base ai valori da un max a un min  
    st.pyplot(fig)

    st.title('company')
    st.dataframe(company)
    st.dataframe(company.corr())
    #grafico12
    fig2=plt.figure(figsize=(10,8))
    plt.title('companyyyy')
    sns.heatmap(company.corr(),annot=True , cmap="Blues")#va a creare una tabella con una palet di colori in base ai valori da un max a un min  
    st.pyplot(fig2)
#############
    st.title('ecco il tutto')
    X=startup.drop("Profit",axis=1)
    y=startup["Profit"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
    test_size = 0.2, 
    random_state = 667)
    X_train.shape, X_test.shape
    model = LinearRegression()
    model.fit(X_train, y_train)
    #model.coef_
    #model.intercept_
    y_pred = model.predict(X_test)
    res_df = pd.DataFrame(data=list(zip(y_pred, y_test)),columns=['predicted', 'real'])
    #res_df
    res_df['error'] = res_df['real'] - res_df['predicted']
    #res_df
    res_df['error'].mean()
    length = y_pred.shape[0] #  
    x = np.linspace(0,length,length)
    if st.button('regression'):
        st.balloons()
        fig=plt.figure(figsize=(10,8))
        plt.title('startupp')
        plt.plot(x, y_test, label='real y')
        plt.plot(x, y_pred, label="predicted y'")
        st.pyplot(fig)
        #model.coef_
        #model.intercept_
        rd=st.number_input('Innserire valore RD',1,1000,842)
        administration=st.number_input('Innserire valore Administration',1,1000,250)
        marketing=st.number_input('Innserire valore Marketing',1,1000,400)
        profit= model.intercept_+0.82 *rd-0.026 *administration+0.03*marketing
        #st.round(profit,1)
        st.write(f'Il valore del profitto per gli Input selezionati è:{round(profit,1)}')
        

if __name__ == "__main__":
    main()