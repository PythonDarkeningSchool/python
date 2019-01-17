"""Problem description:

Como control de etapa publicitaria se requiere que el rendimiento
en millas por galon de gasolina que los fabricantes de automoviles
usan como fines publicitarios este basado en un buen numero de pruebas
efectuadas en diversas condiciones. Al tomar una muestra de n = 50
automoviles se registran las siguientes observaciones en millas
por galon.
"""

from __future__ import print_function
import math
from tabulate import tabulate

# number of class
CLASS_NUMBER = 7
# the decimals to subtract to the first value of the class border
FIRST_VALUE_SUBTRACTION = 0.3
# the numbers of elements in the class border matrix allowed to be in the raw_data
LIMIT = 2
# the float number to add in class interval for round it
ADDITION_TO_CLASS_INTERVAL = .2


def raw_data():
    """Raw data for the cars

    return:
        - milles_per_galon: which is the cars' row data
    """

    milles_per_galon = [
        27.9, 29.3, 31.8, 22.5, 34.2,
        34.2, 32.7, 26.5, 26.4, 31.6,
        35.6, 31.0, 28.0, 33.7, 32.0,
        28.5, 27.5, 28.8, 31.2, 28.7,
        30.0, 28.7, 33.2, 30.5, 27.9,
        31.2, 29.5, 28.7, 23.0, 30.1,
        30.5, 31.3, 24.9, 26.8, 29.9,
        28.7, 30.4, 31.3, 32.7, 30.3,
        33.5, 30.5, 30.6, 35.1, 28.6,
        30.1, 30.3, 29.6, 31.4, 32.4,
    ]

    return milles_per_galon


class AdvertisingControl(object):

    HIGHER_VALUE = max(raw_data())
    LOWER_VALUE = min(raw_data())
    LOWER_VALUE_CONTENT = LOWER_VALUE - FIRST_VALUE_SUBTRACTION

    @staticmethod
    def class_interval(addition=0.0):
        """The class interval of the cars' row data

        @params:
            - addition: which is a float number to round the
                        interval.
        return:
            - interval: which is the class interval
        """

        value = (AdvertisingControl.HIGHER_VALUE - AdvertisingControl.LOWER_VALUE) / CLASS_NUMBER
        # get only one decimal
        interval = math.floor(value * 10 ** 1) / 10 ** 1

        return interval + addition

    def class_border_matrix(self):
        """Creates a class border matrix

        return:
            - class_border_matrix: the class border matrix
        """

        interval = self.class_interval(ADDITION_TO_CLASS_INTERVAL)
        class_border_matrix = []

        # creating class border matrix [0, 0]
        for row in range(CLASS_NUMBER):
            # appending an empty list
            class_border_matrix.append([])
            if not row:
                # the first value in the array
                class_border_matrix[row].append(
                    AdvertisingControl.LOWER_VALUE - FIRST_VALUE_SUBTRACTION)
            else:
                last_matrix_value = class_border_matrix[row - 1][0]
                # get only one decimal
                operation = last_matrix_value + interval
                class_border_matrix[row].append(
                    math.floor(operation * 10 ** 1) / 10 ** 1)

        # creating class border matrix [0, 1]
        count = 0
        for _ in class_border_matrix:
            try:
                next_row_value = class_border_matrix[count + 1][0]
                operation = next_row_value - 0.1
            except IndexError:
                # this is the last matrix value
                # in order to get the last value we have to sum the latest value + the class interval
                previous_value = class_border_matrix[CLASS_NUMBER - 2][1]
                operation = previous_value + interval

            value_to_add = math.floor(operation * 10 ** 1) / 10 ** 1
            class_border_matrix[count].append(value_to_add)
            count += 1

        return class_border_matrix

    def show_data(self):
        matrix = self.get_matrix()
        interval = self.class_interval() + ADDITION_TO_CLASS_INTERVAL
        subtraction_value = FIRST_VALUE_SUBTRACTION

        print("Higher value       :  {}\n"
              "Lower value        :  {}\n"
              "Class interval     :  {}\n"
              "Subtraction value  :  {}\n".format(
                AdvertisingControl.HIGHER_VALUE,
                AdvertisingControl.LOWER_VALUE,
                interval,
                subtraction_value))

        print(matrix)

    def evaluate_matrix(self):
        matrix = self.class_border_matrix()
        data = raw_data()
        count = 0
        elements_in_raw_data = []

        for element in matrix:
            value_a = element[0]
            value_b = element[1]
            if value_a in data:
                elements_in_raw_data.append(value_a)
                count += 1
            elif value_b in data:
                elements_in_raw_data.append(value_b)
                count += 1

        if count > 2:
            print("err: there are {} elements in the raw data\n"
                  "{}\n".format(count, elements_in_raw_data))
        else:
            print("elements in row data are: {}\n"
                  "{}\n".format(count, elements_in_raw_data))

    def get_matrix(self):
        """Get the class border matrix in a table format"""

        content = self.class_border_matrix()
        headers = ["index", "From", "To"]
        index_range = CLASS_NUMBER + 1
        table = tabulate(
            content, headers, 'fancy_grid', missingval='?', stralign='center', numalign='center',
            showindex=range(1, index_range))

        return table


if __name__ == "__main__":
    obj = AdvertisingControl()
    obj.evaluate_matrix()
    obj.show_data()

