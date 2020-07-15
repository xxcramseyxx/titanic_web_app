def fake_predict(user_age):
    if user_age > 10:
        prediction = "Survived (over ten)"
    else:
        prediction = "Super Survived (under ten)"
    return prediction
