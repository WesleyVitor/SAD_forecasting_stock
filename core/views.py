from django.shortcuts import render, redirect
from django.views import View, generic
from core.service import forecasting_data

class ValueOfStock(View):
    def get(self, request):
        
        return render(request, 'stock.html')


class ForecastingView(View):

    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        data = request.POST['data']
        stock = request.POST['stock']
        
        forecast = forecasting_data(data, stock)
        return render(request, 'stock.html', context={'forecast': forecast, 'stock': stock, 'data': data})
    
