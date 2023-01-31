
# Car-Mileage-Prediction-System
This is is a web application built using the Django web framework that allows users to predict the miles per gallon (MPG) of a car based on input parameters. The input parameters are collected from a website form and include the number of cylinders, displacement, horsepower, weight, model year, and origin of the car.

The input data is then passed to a Jupyter notebook where a machine learning algorithm is applied to estimate the MPG. The machine learning algorithm used to predict the MPG could be a regression model, such as linear regression or random forest regression. These models are trained on a dataset that contains historical data on car characteristics and their corresponding MPG.

The output is returned to the website and displayed to the user.

This type of web application can be useful for car manufacturers, buyers, sellers or researchers to estimate the fuel efficiency of the car before buying or selling it. This can also be useful for researchers to compare the performance of different models of cars and find out which models are more fuel-efficient.

##Data
The dataset consists of the following details:

Engine characteristics: Information about the car's engine, such as the number of cylinders, displacement, and horsepower.

Vehicle characteristics: Information about the car's physical characteristics, such as its weight, length, and width.

Fuel efficiency: Data on the car's fuel efficiency, such as its estimated miles per gallon (MPG) and emissions ratings.

Model year: The year the car model was produced

Origin: The country where the car was manufactured or assembled

Brand: The car manufacturer brand


## Jupyter Notebook
The Jupyter notebook  uses the mpg dataset to train a machine learning model for predicting the miles per gallon (MPG) of a car.

*The dataset is first preprocessed to remove any missing or null values, which is a crucial step in ensuring the quality and integrity of the data.

*The data is cleaned, passed through various machine learning algorithmic models, such as Linear Regression, Quadratic Polynomial Regression, DecisionTreeRegressor, and RandomForestRegressor. These models are chosen because they are commonly used for regression tasks, and are well suited for predicting a continuous value such as MPG.

*The models are evaluated using evaluation metrics such as Mean Squared Error, Root Mean Squared Error, R-squared score, etc. The final model chosen is the one that performs the best on the evaluation metrics.

*In this case, the final model chosen is RandomForestRegressor which gave an R-squared score of around 86%, which is considered good for a supervised learning algorithm.

## Web application Screenshot
![image](https://user-images.githubusercontent.com/78245820/214334137-9faeee52-7f4d-4491-acd0-cf57cd0f1a36.png)

## Output
![image](https://user-images.githubusercontent.com/78245820/214334338-38cc2dd6-3681-427b-9ee7-b642b40e3805.png)

