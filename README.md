
## Car-Mileage-Prediction-System
This is a website for prediction of miles per gallon of a car given it's number of cylinders,displacement,horsepower,weight,model year and origin.It is made from simple bootstrap and Django.The output has been estimated from a machine learning algorithm.The input from website form is passed to the jupyter notebook and prediction is returned.

#Jupyter Notebook
The jupyter notebook used has been defined by using the mpg dataset.The dataset is first preprocessed to remove all NULL values and then passed through various ML algorithmic models.The models used were Linear Regression , Quadratic Polynomial Regression , DecisionTreeRegressor and RandomForestRegressor. Finally RandomForestRegressor was used which gave an r2 score of around 86%(which is good for Supervised Learning Algorithm).
