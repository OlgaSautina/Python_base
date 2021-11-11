"""
Реализовать проект «Операции с комплексными числами».
1) Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
2) Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
   выполнив сложение и умножение созданных экземпляров.
   Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.r = real  # реальная часть
        self.im = imaginary  # мнимая часть

    def __add__(self, other):
        real_new = self.r + other.r
        imaginary_new = self.im + other.im
        return ComplexNumber(real_new, imaginary_new)

    def __mul__(self, other):
        real_new = self.r * other.r - self.im * other.im
        imaginary_new = self.r * other.im + self.im * other.r
        return ComplexNumber(real_new, imaginary_new)

    def __str__(self):
        if self.im > 0:
            return f'{self.r} + i*{self.im}'
        else:
            return f'{self.r} - i*{abs(self.im)}'


print('1. Вычисление суммы:')
complex_1 = ComplexNumber(10, 15)
complex_2 = ComplexNumber(4, -5)
sum_complex = complex_1 + complex_2
print(f'({complex_1}) + ({complex_2}) = {sum_complex}')
print('Проверка:')
print(f'(10 + 4) + i * (15 + (-5)) = {10 + 4} + i*{15 + (-5)}')
print('\n')

print('2. Вычисление произведения:')
mul_complex = complex_1 * complex_2
print(f'({complex_1}) * ({complex_2}) = {mul_complex}')
print('Проверка:')
print(f'{10 * 4 - 15 * (-5)} + i*{10 * (-5) + 15 * 4}')

