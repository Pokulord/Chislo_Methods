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
        self.funs_links = [self.Middle_Triangles , self.Trapetion, self.Simpson_method]
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
        h = (self.end_value - self.begin_value)/n 
        s = h*(self.integrated_function(self.begin_value) + self.integrated_function(self.end_value))/ 2
        for i in range(1, n -1):
            s = s + h * self.integrated_function(self.begin_value + i * h)

        return s 
    
    # Метод Симпсона
    def Simpson_method(self, n):
        h = (self.end_value - self.begin_value) / (2 * n)
        s1 = 0
        s2 = 0
        for i in range(1 , n):
            x1 = self.begin_value + (2*i - 1) * h
            s1 = s1 + self.integrated_function(x1)
            x2 = x1 + h 
            s2 = s2 + self.integrated_function(x2)
        s = h/3*(self.integrated_function(self.begin_value) + 4* s1 + 2 * s2 - self.integrated_function(self.end_value))
        return s

    


    
    def execute_code(self):
        self.analytics_value = self.Analytics_method()
        print(f"Аналитическое значение интеграла : {round(self.analytics_value, 4)}")
        for main_index in range(len(self.funs_links)):
            print ("-" * 40)
            for index in range(len(INTERVALS_COUNT)):
                mt_integral_value = self.funs_links[main_index](INTERVALS_COUNT[index])
                accuracy = abs(self.analytics_value - mt_integral_value)
                print (f"Метод {METHODS_NAMES[main_index]} при n = {INTERVALS_COUNT[index]} :  {mt_integral_value} Точность : {round(accuracy,4)} ")


if __name__ == "__main__":
    # Левый и правый предел интегрирования
    a, b = 0, 1
    Integral_value(a,b)

