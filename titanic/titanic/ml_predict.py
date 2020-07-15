def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    randomforest = pickle.load(open('titanic_model.sav', 'rb'))
    predictions = randomforest.predict(x)

    if predictions == 0:
        predictions = 'Died'
    elif predictions == 1:
        predictions = 'Survived'
    else:
        predictions = 'Error'

    return predictions
