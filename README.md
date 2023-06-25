# house_price_predictor_AWS
The dataset includes information about the house like price	bedrooms	bathrooms	sqft_living	sqft_lot	floors	waterfront	view	condition	sqft_above	sqft_basement	yr_built	yr_renovated.  In this assignment, I worked on a house price prediction project using the "House Prices: Advanced Regression Techniques" dataset from Kaggle. My main focus was on data cleaning and preprocessing tasks, including handling missing values, outliers, and categorical features. The goal was to train a regression model to predict house prices and optimize its performance.

Task 1: Data Understanding 
I began by exploring the dataset and understanding its structure, including the meaning and type of each feature. using Explortarry data analysis methods.

Task 2: Data Cleaning
I addressed the following data cleaning tasks:
1. Handling missing values: I identified features with missing values and decided on an appropriate strategy to handle them, such as imputation or removal.
2. Dealing with outliers: I identified outliers in numerical features and decided on an appropriate approach, such as removing outliers or transforming the data.
3. Handling categorical features: I converted categorical variables into numerical representations using techniques like one-hot encoding or bining.
4. removed duplicates and invalid data.


Task 3: Feature Engineering
I performed feature engineering to enhance the predictive power of the dataset. This involved creating new features, transforming existing features, or selecting relevant features. i used binning to convert built years into categories.

Task 4: Data Preprocessing
I prepared the cleaned dataset for model training. This included scaling numerical features, encoding categorical variables, and splitting the data into training and testing sets.

Task 5: Model Training and Evaluation
I chose an appropriate regression model, such as linear regression, random forest, or gradient boosting, and trained it on the preprocessed dataset. I evaluated the model's performance using suitable metrics root mean squared error (RMSE). The choice between MSE and RMSE depends on the specific context and preference. MSE is often preferred when the errors need to be further analyzed or compared in their original scale. On the other hand, RMSE is preferred when a more easily interpretable metric is desired, as it is in the same unit as the target variable.

Task 6: Model Optimization
I fine-tuned the hyperparameters of the chosen model to improve its performance. Grid search CV were used to find the best parameter values. Then I stored that trained model and scaller into a pickle files. 

Task 7: Model Deployment (Assignment-8)
Once I had a satisfactory model, I deployed it using AWS EC2 service to make predictions on new, unseen data. I used the trained model to predict house prices for new instances and assess its real-world applicability.


I am pleased to have completed this assignment. I have learned a lot throughout the process and am confident in the solutions I have implemented.

