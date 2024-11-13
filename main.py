from sumar import operacion_suma
from division import operacion_division
from multiplicacion import operacion_multiplicacion
from resta import operacion_resta

resultado_suma = operacion_suma(2,3)
print(f"el resultado de la suma es: ", resultado_suma)


resultado_division = operacion_division(8,3)
print(f"el resultado de la divisione es:", resultado_division)

resultado_multiplicaion = operacion_multiplicacion(9,8)
print("el resultado de la multiplicacion es: ", resultado_multiplicaion)

resultado_resta = operacion_resta(9,8)
print("el resultado de la resta es: ", resultado_resta)