import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def forbred_data(filbane):

    df = pd.read_csv(filbane) 

    #her henter vi ut dato elementene vi trenger 
    df['date'] = pd.to_datetime(df['date'])
    df['dayofyear'] = df['date'].dt.dayofyear
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    #her bruker vi sinus og cosinus for å gi sesongmønstre
    df['sin_day'] = np.sin(2 * np.pi * df['dayofyear'] / 365.0)
    df['cos_day'] = np.cos(2 * np.pi * df['dayofyear'] / 365.0)

    x = df[['sin_day', 'cos_day']]
    y = df['sunshine_hours']

    return df, x, y

def tren_pred(df, x, y):
    
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score

    #deler opp data i trening og test sett
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    #trener lineær regresjonsmodell
    modell = LinearRegression()
    modell.fit(x_train, y_train)

    #lager predikasjoner
    y_pred = modell.predict(x_test)

    # printer ut mål for evaluering
    print('mes:', mean_squared_error(y_test, y_pred))
    print('R²-score:', r2_score(y_test,y_pred))

    #scatterplot som sammenligner predikert og faktisk verdi
    sns.scatterplot(x=y_test, y=y_pred)
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--')
    plt.xlabel('faktiske verdier')
    plt.ylabel('predikerte verider')
    plt.title('faktiske vs predikerte verdier')
    plt.show()

    return modell, y_pred

def gen_framtid(startdato, antall_dager=365):
    from datetime import timedelta
    
    #lager ei liste me dato fra start til oppgitte antall dager
    framtidige_datoer = [startdato + timedelta(days=i) for i in range(1, antall_dager + 1)]
    df_framtid = pd.DataFrame({'date':framtidige_datoer})

    df_framtid['dayofyear'] = df_framtid['date'].dt.dayofyear
    df_framtid['month'] = df_framtid['date'].dt.month

    df_framtid['sin_day'] = np.sin(2 * np.pi * df_framtid['dayofyear'] / 365.0)
    df_framtid['cos_day'] = np.cos(2 * np.pi * df_framtid['dayofyear'] / 365.0)

    return df_framtid


def vis_fremtid(df, modell):
    #setter start dato til siste dag i datasettet
    startdato = pd.to_datetime(df['date'].max())
    df_framtid = gen_framtid(startdato, 365)

    x_fremtid = df_framtid[['sin_day', 'cos_day']]
    y_fremtid_pred = modell.predict(x_fremtid)
    df_framtid['sunshine_predicted'] = y_fremtid_pred

    plt.figure(figsize=(12, 10))

    #linjediagram
    plt.subplot(3, 1, 1)
    sns.lineplot(x=df_framtid['date'], y=df_framtid['sunshine_predicted'])
    plt.title('predikert solskinn linjediagram')
    plt.ylabel('timer solskinn')
    plt.xlabel('dato')
    plt.xticks(rotation=45)
    
    #punktdiagram
    plt.subplot(3, 1, 2)
    sns.scatterplot(x=df_framtid['date'], y=df_framtid['sunshine_predicted'])
    plt.plot([min(df_framtid['date']), max(df_framtid['date'])], [min(df_framtid['sunshine_predicted']), max(df_framtid['sunshine_predicted'])], '*')
    plt.title('predikert solskinn punktdiagram')
    plt.ylabel('timer solskinn')
    plt.xlabel('dato')
    plt.xticks(rotation=45)

    #histogram 
    plt.subplot(3, 1, 3)
    sns.histplot(df_framtid['sunshine_predicted'], bins=30, kde=True, color='yellow')
    plt.title('predikert solskinn histogram')
    plt.xlabel('timer solskinn')
    plt.ylabel('antall dager')
    
    plt.tight_layout()
    plt.show()


'''
Matplotlib (n.d.) matplotlib.org
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

OpenAI. (n.d.). *ChatGPT (GPT-4)* [Stor språkmodell]. https://chat.openai.com/

Pandas (n.d.) pandas.pydata.org.
    https://pandas.pydata.org/docs/user_guide/index.html
    https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe

Rouhani, M. (2019). *Applied Programming — Applied Programming.* Ntnu.no. https://rouhani.folk.ntnu.no/textbooks/tdt4114/intro.html

Scikit learn (n.d.) scikit-learn.org
    https://scikit-learn.org/stable/getting_started.html
    https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics

W3Schools. (n.d.-a).  Www.w3schools.com.
    https://www.w3schools.com/python/pandas/default.asp
    https://www.w3schools.com/python/pandas/pandas_dataframes.asp
    https://www.w3schools.com/python/matplotlib_subplot.asp
    https://www.w3schools.com/python/matplotlib_intro.asp

Waskom, M. L., (2021). seaborn: statistical data visualization. Journal of Open Source Software, 6(60), 3021, https://doi.org/10.21105/joss.03021.
    '''
    