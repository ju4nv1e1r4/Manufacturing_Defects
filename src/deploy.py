# %%
# importando bibliotecas e sources
from source import path
import pandas as pd
import numpy as np
import lightgbm


# %%
# carga do modelo
predictors = pd.read_csv(path.model)
target = pd.read_csv(path.target)
predictors = predictors.values
target = target.iloc[:, 0].values

# %%
# algoritmo
dataset = lightgbm.Dataset(predictors, label=target
                           )
params = {'num_leaves':200, 
              'objective':'binary',
              'max_depth':4,
              'learning_rate':.05,
              'max_bin':150}

lgbm = lightgbm.train(params, dataset, num_boost_round=100)

for i in range(0, 3239):
    predictors[i] = [1 if x >= 0.5 else 0 for x in predictors[i]]

# %%
# previsão
exemplo1 = np.array([[549, 12423, 90, 2.75, 80, 5, 1.5, 6, 90, 3000, 0.29, 5.5, 300, 0.72, 337.25, 0.004238, 0.90, 16.091, 0.007453, 0.90, 0.32, 324.11]])

prediction = lgbm.predict(exemplo1)

if prediction == 1:
    print('A máquina provavelmente dará defeitos.')
else:
    print('A máquina provavelmente não dará defeitos')
'''
este pequeno teste, foi feito uma redução de mais de 
50% de horas de manutenção semanais,  e o algoritmo
identificou que, com base nas entradas do 'exemplo1'
a máquina tem mais probabilidades de não dar defeitos
'''
