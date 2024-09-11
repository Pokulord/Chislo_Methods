# Выполнил студент группы РИ-321055 Черников С.С
#! Программа для вычисления интегралов функций следующими методами:
# 1. Аналитический метод
# 2. Метод средних прямоугольников
# 3. Формула трапеций
# 4. Формула Симпсона

####### Импорт модулей #####
from scipy.integrate import quad
import numpy as np

# Константы для выполнения расчётов
INTERVALS_COUNT = [5,10,100]
METHODS_NAMES = ["средних треугольников", "трапеций", "Симпсона"]
# Класс, содержащий методы для вычисления значения интегралов 
class Integral_value:
    def __init__(self, a , b) -> None:
        self.begin_value = a
        self.end_value = b
        self.funs_links = [self.Middle_Triangles]
        self.execute_code()

    def integrated_function(self, x):
        return x/(1+x**4)

    # Аналитический метод
    def Analytics_method(self):
        return quad(self.integrated_function, self.begin_value, self.end_value)[0]
    
    # Метод средних прямоугольников
    def Middle_Triangles(self , n):
        h = (self.end_value - self.begin_value)/ n
        s = 0
        for i in range(0, n-1):
            s = s + h * self.integrated_function(self.begin_value + h/2 + i * h)
        return s
    
    # Метод трапеций
    def Trapetion(self, n):
        pass
    


    
    def execute_code(self):
        self.analytics_value = self.Analytics_method()
        print(f"Аналитическое значение интеграла : {round(self.analytics_value, 4)}")
        for main_index in range(len(self.funs_links)):
            for index in range(len(INTERVALS_COUNT)):
                mt_integral_value = self.funs_links[main_index](INTERVALS_COUNT[index])
                accuracy = abs(mt_integral_value - self.analytics_value)
                print (f"Метод {METHODS_NAMES[main_index]} при n = {INTERVALS_COUNT[index]} :  {mt_integral_value} Точность : {accuracy} ")


if __name__ == "__main__":
    # Левый и правый предел интегрирования
    a, b = 0, 1
    Integral_value(a,b)

