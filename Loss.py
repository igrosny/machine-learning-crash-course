"""
Como se calcula la perdida
Algunos problemas son convexos, hasta llegar al fondo del bowl
la mayor cantidad de problema son como un maple de huevos

En este modulo aprendemos como el modelo reduce la perdida
en cada iteracion

Aprendiendo iterativamente es como jugar al caliente, calente..
donde vamos recalculado la funcion de perdida y viendo que tan caliente estamos

para regresion lineal, lo primeros valores no son tan importantes

a la funcion de perdida se le pasan dos valores
y' la prediccion del modelo para los parametros de x
y: La correcta etiqueta correspondiente a los paramentros de x

Gradient Descent
================
Para los problemas de rgresion, siempre va a ser convexo

Los problemas convezo solo tienen un minimo

gradient descent
el gradiente de la curva de perdida es igual a la derivdad

(derivada parciales)