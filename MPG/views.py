from django.shortcuts import render
import joblib
import pandas as pd
# Create your views here.
reloadModel = joblib.load('./models/RFModelforMPG.pkl')

def home(request):
    return render(request,'home.html')

def predictMPG(request):
    if request.method == 'POST':
        temp={}
        temp['cylinders'] = request.POST.get('cylinderVal')
        temp['displacement'] = request.POST.get('dispVal')
        temp['horsepower'] = request.POST.get('hrsPwrVal')
        temp['weight'] = request.POST.get('weightVal')
        temp['acceleration'] = request.POST.get('accVal')
        temp['model_year'] = request.POST.get('modelVal')
        temp['origin'] = request.POST.get('originVal')

        temp2 = temp.copy()
        temp2['model year'] = temp['model_year']
        del temp2['model_year']
    testData = pd.DataFrame({'x':temp2}).transpose()
    scoreval = reloadModel.predict(testData)[0]
    return render(request,'home.html',{'scoreval':scoreval})
