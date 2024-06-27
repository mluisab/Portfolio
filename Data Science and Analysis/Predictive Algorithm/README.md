# Predictive Model - Identyfing Terrorist Organisations
This model was created as part of an academic project for the bachelor Computational Social Science as the University of Amsterdam. The project, centered around the Global Terrorism Dataset offered by START, uses machine learning to create a predictive algorithm while studying AI biases, ethical considerations and social perspectives related to the development of such tools. 

Using the historical data provided, the model developed classifies terrorist organisations and predicts potential groups responsible for attacks if given a specific input. 
Given the highly imbalanced dataset, the groups were filtered by attack count, and the top 10 groups were chosen.


# Features and Model Training
The model uses mostly categroical features describing attacks. These variables include attack type, region, weapon type, target type, number of victimis, property attacked, and inclusion criteria related to whether the attack is considered a terrorist incident.

The model is trained on a dataset of past terrorist attacks, with each attack being assigned to a specific terrorist group name. The model is a multi-class Random Forest Classifier that classifies as it focuses on 10 different terrorist groups.


# How to Use the Model
To use the model to predict a terrorist organisation respinsible for a given attack, check the following steps:

1. Define the features of the attack such as region, weapon used, target or type of attack
    e.g: input_features = ['Sub-Saharan Africa', 'Government (General)', 'Bombing/Expolosion']

2. Use the model to predict the terrorist group responsible. The model will print the top 3 groups most likely to be responsible for the given attack.


# Dependencies
This project is implemented in Python, using the following libraries and packages:
- pandas: to manipulate data
- numpy: for numerical calculations
- scikit-learn: for machine learning functions or tasks
- matplotlib: for plots and data visualizations
- seaborn: for plots and data visualization


# Resources and Credits
This project uses the Global Terrorism Database (GTD), an open-source database including information on terrorist attacks and events around the world.


# Challanges and Limitations
The main challenge and limitation of this project is the selection of terrorist groups. As of now, the model focuses only the first 10 terrorist groups based on the highest number of attacks. This limits the model's abilities to predict the perpetrators of an attack. However, training the model on all the terrorist groups recorded in the GTD dataset is challenging based on their large number and high discrepnacies in available data for each.




