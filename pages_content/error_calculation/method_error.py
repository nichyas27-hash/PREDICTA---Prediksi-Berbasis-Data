import numpy as np

def mae(df):
    e = df['Aktual'] - df['Forecast']
    return np.mean(np.abs(e))

def mape(df):
    e = df['Aktual'] - df['Forecast']
    e_relatif = e/df['Aktual']
    return np.mean(np.abs(e_relatif)*100)

def mse(df):
    e = df['Aktual'] - df['Forecast']
    return np.mean(e**2)

def rmse(df):
    e = mse(df)
    return np.mean(np.sqrt(e))