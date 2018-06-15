"""
x : metros cuadrados de la casa
y : precio de la casa
y = wx + b
w = m 

Loss: la distancia entre el punto y la linea
(y - y')2

Entrenamiento y funcion de Loss
entrenar lo unico que significa es poder determinar los mejores 
valores para los weights y el bias de ejemplos etiquetados

Empirical risk minimization: construir un modelo a base de ejemplos
minimizando la perdida

Loss es basicamente una penalidad por una mala predicion

l2 loss: sqaured loss
MSE: Mean square error: es el promedi de todos los l2. Sumo las
diferencias cuadradas y lo divido por la cantidad de ejemplos

