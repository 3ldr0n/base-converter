"""
Edison Neto, This software simply converts a number in some numerical
base to decimal

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

from converter import Converter


def get_base():
    number = ''
    while type(number) != "int":
        number = input("Type the base(number): ")
        try:
            number = int(number)
            return number
        except ValueError:
            print("This should be a number")

    return number


if __name__ == '__main__':
    number = str(input("Type the number: "))
    base = get_base()

    number = Converter(number)

    if base == 16:
        number.convert_hexadecimal_to_decimal()
    elif number.is_int():
        number.convert_int_to_decimal(base)
    elif number.is_float():
        number.convert_float_to_decimal(base)
