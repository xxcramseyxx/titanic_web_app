from django.shortcuts import render
from . import fake_model
from . import ml_predict


def home(requests):
    return render(requests, 'index.html')


def result(requests):
    pclass = int(requests.GET['pclass'])
    sex = int(requests.GET['sex'])
    age = int(requests.GET['age'])
    sibsp = int(requests.GET['sibsp'])
    parch = int(requests.GET['parch'])
    fare = int(requests.GET['fare'])
    embarked = int(requests.GET['embarked'])
    title = int(requests.GET['title'])
    ##prediction = fake_model.fake_predict(user_input_age)
    prediction = ml_predict.prediction_model(
        pclass, sex, age, sibsp, parch, fare, embarked, title)
    return render(requests, 'result.html', {'prediction': prediction})
