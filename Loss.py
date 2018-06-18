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

Reduciendo las perdidas: velocidad de prendizaje (learning rate)

el learning rate es el escalar por el cual se multiplica el vector gradiente
para calcular el proximo punto

Hyperparametros son la perillas que lo programadores podemos
calibrar en los algoritmos de aprendizaje automatico

the goldilocks principle (el prinicipio de ricitos de oro)
no es ni frio ni caliente

Nota! en la practica, encontrar el learning rate perfecto no es esencial
para el correcto entrenamiento de un modelo. tiene que ser
lo suficientemente bueno para que el modelo converga

Stochastic gradient descent (SGD)
===========================
En gradient descente, el batch es el numero total de ejemplos que uso
para calcular el gradiente en una sola operacion

Stochastic means randomly determined, elije un ejmplo por iteracion

mini batch SGD (entre 10 y 1000 ejmplos elegidos al azar)


