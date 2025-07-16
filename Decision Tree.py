from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

def decision_tree_example():
    outlook = ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast',
               'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain']
    temperature = ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
                   'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild']
    humidity = ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High']
    wind = ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong',
            'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong']
    play = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
            'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

    le_outlook = LabelEncoder()
    le_temperature = LabelEncoder()
    le_humidity = LabelEncoder()
    le_wind = LabelEncoder()
    le_play = LabelEncoder()

    outlook_encoded = le_outlook.fit_transform(outlook)
    temp_encoded = le_temperature.fit_transform(temperature)
    humidity_encoded = le_humidity.fit_transform(humidity)
    wind_encoded = le_wind.fit_transform(wind)
    play_encoded = le_play.fit_transform(play)

    features = list(zip(outlook_encoded, temp_encoded, humidity_encoded, wind_encoded))

    model = DecisionTreeClassifier(criterion='entropy')
    model.fit(features, play_encoded)

    print("Trained Decision Tree")
    sample = [[2, 2, 0, 1]]
    prediction = model.predict(sample)
    print("Prediction for sample", sample, ":", le_play.inverse_transform(prediction)[0])

    tree.plot_tree(model, feature_names=['Outlook', 'Temp', 'Humidity', 'Wind'],
                   class_names=le_play.classes_, filled=True)

if __name__ == "__main__":
    decision_tree_example()
