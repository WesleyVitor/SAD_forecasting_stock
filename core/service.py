import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import prophet as pt
import datetime

def model_itau(data_to_previsao):
    df_itau = yf.download('ITUB4.SA',end='2023-11-28')
    df_treino_itau = pd.DataFrame()
    df_treino_itau['ds'] = df_itau.index[3800:5751] #  2016-01-28 - 2023-11-27
    df_treino_itau['y'] = df_itau['Adj Close'][3800:5751].values

    modelo = pt.Prophet(seasonality_mode='additive',daily_seasonality=False,weekly_seasonality=True,yearly_seasonality=True,n_changepoints = 300)
    modelo.fit(df_treino_itau)
    previsao = modelo.predict(data_to_previsao)
    
    return previsao, df_itau

def model_santander(data_to_previsao):
    df_santander = yf.download('BCSA34.SA',end='2023-11-28')
    df_treino_santander = pd.DataFrame()
    df_treino_santander['ds'] = df_santander.index[:900] #  2019-11-01 - 2023-06-21
    df_treino_santander['y'] = df_santander['Adj Close'][:900].values
    modelo = pt.Prophet(seasonality_mode='additive',daily_seasonality=False,weekly_seasonality=True,yearly_seasonality=True,n_changepoints = 300)
    modelo.fit(df_treino_santander)
    previsao = modelo.predict(data_to_previsao)
    return previsao, df_santander

def model_bradesco(data_to_previsao):
    df_bradesco = yf.download('BBDC4.SA',end='2023-11-28')
    df_treino_bradesco = pd.DataFrame()
    df_treino_bradesco['ds'] = df_bradesco.index[2000:4000] #  2016-02-02 - 2023-11-27
    df_treino_bradesco['y'] = df_bradesco['Adj Close'][2000:4000].values
    modelo = pt.Prophet(seasonality_mode='additive',daily_seasonality=False,weekly_seasonality=True,yearly_seasonality=True,n_changepoints = 300)
    modelo.fit(df_treino_bradesco)
    previsao = modelo.predict(data_to_previsao)
    return previsao, df_bradesco

def forecasting_data(data, stock):
    
    serie = pd.bdate_range(start = data,
                          end = str((datetime.datetime.strptime(data, '%Y-%m-%d') + datetime.timedelta(days=30)).date()),
                          freq='C',
                          weekmask = None,
                          holidays=None)
    
    data_to_previsao = pd.DataFrame()
    data_to_previsao['ds'] = serie
    

    if stock == 'itau':
        previsao, df_original =  model_itau(data_to_previsao)
        return (data_to_previsao,previsao,df_original)
    elif stock == 'santander':
        previsao, df_original =  model_santander(data_to_previsao)
        return (data_to_previsao,previsao,df_original)
    elif stock == 'bradesco':
        previsao, df_original =  model_bradesco(data_to_previsao)
        return (data_to_previsao,previsao,df_original)