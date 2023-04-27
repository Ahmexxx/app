import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
def main():
    st.title("ml app")
    generate_random = np.random.RandomState(667)
    inprand=st.slider("inserisci valore punti random",1,1000,50)
    x = 10 * generate_random.rand(inprand)
    mu=0
    sigma=st.slider("inserisci sigma",0,10,1)
    s=np.random.normal(mu,sigma,inprand)
    coe=st.slider("inserisci coeficente angolare",1,10,1)
    y =  coe * x + s
    fig =plt.figure(figsize = (10, 8))
    X=x.reshape(-1,1)

    model=LinearRegression()
    model.fit(X,y)
    y_pred=model.predict(X) #predice 

    plt.scatter(x, y)
    plt.plot(x, y_pred,'-r')
    plt.title('Simple Linear Regression')
    plt.axis([0,10,0,30]) #fissare l'asse 
    st.pyplot(fig)



if __name__ == "__main__":
    main()