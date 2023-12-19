from django.shortcuts import render, redirect
from django.views import View, generic
from core.service import forecasting_data
import base64
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import datetime
    

class ValueOfStock(View):
    pass


class ForecastingView(View):

    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        data = request.POST['data']
        stock = request.POST['stock']
        
        (datas, forecasts, df_original) = forecasting_data(data, stock)
        df_original_values = df_original.loc[lambda x: (x.index > data) & (x.index < str((datetime.datetime.strptime(data, '%Y-%m-%d') + datetime.timedelta(days=30)).date()))]['Adj Close'].values
        
        lista = []
        l=0
        for i, r in forecasts.iterrows():
            lista.append([str(r['ds'].date()), r['trend'],list(df_original_values)[l]])
            l+=1
            if l == len(df_original_values):
                break
             
        return render(request, 'stock.html', context={'forecasts': lista, 'stock': stock, 'datas': datas})
    
