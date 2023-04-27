import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
import streamlit as st
def main():
    st.title('terza App')
    urlA="iris.data"#assegno ad una variabile
    iris=pd.read_csv(urlA,header=None)#leggo il file
    iris.columns=['sepal length','sepal width','petal length','petal width','class:']
    sns.pairplot(iris ,hue="class:")
    X=iris.drop("class:",axis=1)
    y=iris["class:"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
    test_size = 0.2, random_state = 667)
    model =LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    res_df = pd.DataFrame(data=list(zip(y_pred, y_test)),columns=['predicted', 'real'])
    model.coef_
    model.intercept_
    length = y_pred.shape[0] #  
    x = np.linspace(0,length,length)
    plt.plot(x, y_test, label='real y')
    plt.plot(x, y_pred, label="predicted y'")
    model.predict([[2,2,2,2]])[0]
    st.file_uploader('carica file')




if __name__ == "__main__":
    main()
