"""
Edison Neto, This software simply converts a number in some numerical
base to decimal.

Copyright (C) 2018 Edison Neto
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""


class Converter():

    def __init__(self, number):
        self.number = number

    def convert_int_to_decimal(self, base):
        decimal = 0
        # Gets each digit of the number.
        for each_digit in enumerate(reversed(self.number)):
            result = int(each_digit[1]) * (base**each_digit[0])
            print("{} * {}^{} = {}".format(
                    each_digit[1], base, each_digit[0], result))

            decimal += result

        print("Final result: {}".format(decimal))

    def convert_float_to_decimal(self, base):
        # This separates the number into the integer part and the float part.
        number = self.number.split('.')
        number_integer_part = number[0]
        number_float_part = number[1]

        # Calculus of the float part.
        # The negative length is used to calculate the number's float part.
        negative_length = (0 - len(number_float_part))
        number_float_part = number_float_part[::-1]

        # Reverts the order of the number so it can calculate correctly.
        number_float_part_reversed = []
        for number in number_float_part:
            number_float_part_reversed.append(number)

        float_results = 0
        for index in range(negative_length, 0):
            result = int(number_float_part_reversed[index]) * (base**index)
            print("{} * {}^{} = {}".format(
                    number_float_part_reversed[index], base, index, result))
            float_results += result

        # Calculus of the integer part.
        integer_results = 0
        for each_digit in enumerate(reversed(number_integer_part)):
            result = int(each_digit[1]) * (base**each_digit[0])
            print("{} * {}^{} = {}".format(
                    each_digit[1], base, each_digit[0], result))

            integer_results += result

        final_result = integer_results + float_results
        print(final_result)

    def convert_hexadecimal_to_decimal(self):
        # Splits in the dot.
        base = 16
        number = self.number.split('.')
        int_number_in_decimal = []
        float_number_in_decimal = []

        for digit in number[0]:
            if digit == "A" or digit == "a":
                int_number_in_decimal.append(10)
            elif digit == "B" or digit == "b":
                int_number_in_decimal.append(11)
            elif digit == "C" or digit == "c":
                int_number_in_decimal.append(12)
            elif digit == "D" or digit == "d":
                int_number_in_decimal.append(13)
            elif digit == "E" or digit == "e":
                int_number_in_decimal.append(14)
            elif digit == "F" or digit == "f":
                int_number_in_decimal.append(15)
            else:
                int_number_in_decimal.append(int(digit))

        if len(number) > 1:
            for digit in number[1]:
                if digit == "A" or digit == "a":
                    float_number_in_decimal.append(10)
                elif digit == "B" or digit == "b":
                    float_number_in_decimal.append(11)
                elif digit == "C" or digit == "c":
                    float_number_in_decimal.append(12)
                elif digit == "D" or digit == "d":
                    float_number_in_decimal.append(13)
                elif digit == "E" or digit == "e":
                    float_number_in_decimal.append(14)
                elif digit == "F" or digit == "f":
                    float_number_in_decimal.append(15)
                else:
                    float_number_in_decimal.append(int(digit))

        negative_length = (0 - len(float_number_in_decimal))
        number_float_part = float_number_in_decimal[::-1]

        number_float_part_reversed = []
        for number in number_float_part:
            number_float_part_reversed.append(number)

        float_results = 0
        for index in range(negative_length, 0):
            result = int(number_float_part_reversed[index]) ** (base**index)
            print("{} * {}^{} = {}".format(
                    number_float_part_reversed[index], base, index, result))

            float_results += result

        # Integer calculus
        integer_results = 0
        for each_digit in enumerate(reversed(int_number_in_decimal)):
            result = int(each_digit[1]) * (base**each_digit[0])
            print("{} * {}^{} = {}".format(
                    each_digit[1], base, each_digit[0], result))

            integer_results += result

        final_result = integer_results + float_results
        print(final_result)

    def is_int(self):
        # Checks if the variable is an integer.
        try:
            int(self.number)
            return True
        except ValueError:
            return False

    def is_float(self):
        # Checks if the variable is a number.
        try:
            float(self.number)
            return True
        except ValueError:
            return False
