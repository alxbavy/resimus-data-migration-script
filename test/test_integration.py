import json
import os
import shutil
import unittest

from script import main


class TestIntegration(unittest.TestCase):

    OUTPUT_DIR_NAME = 'resources/results'

    def test_flight_calculation_result_with_int_values_txt(self):
        self.INPUT_FILE_NAME = 'resources/test_flight_table_with_int_values.txt'

        main(self.INPUT_FILE_NAME, self.OUTPUT_DIR_NAME)

        for i in range(1, 3+1):
            assert os.path.isfile(f'{self.OUTPUT_DIR_NAME}/flight_result_{i}.json'), f'Cannot find flight result with number {i}'

        assert not os.path.isfile(f'{self.OUTPUT_DIR_NAME}/flight_result_4.json')

        with open(f'{self.OUTPUT_DIR_NAME}/flight_result_1.json', 'r') as test_file:
            test_data_dict = json.load(test_file)
            assert test_data_dict['keroseneAmount'] == 575113

        with open(f'{self.OUTPUT_DIR_NAME}/flight_result_2.json', 'r') as test_file:
            test_data_dict = json.load(test_file)
            assert test_data_dict['keroseneAmount'] == 610313

    def test_flight_calculation_result_with_float_vaules_csv(self):
        self.INPUT_FILE_NAME = 'resources/test_flight_table_with_float_values.csv'

        main(self.INPUT_FILE_NAME, self.OUTPUT_DIR_NAME)

        for i in range(1, 3 + 1):
            assert os.path.isfile(
                f'{self.OUTPUT_DIR_NAME}/flight_result_{i}.json'), f'Cannot find flight result with number {i}'

        assert not os.path.isfile(f'{self.OUTPUT_DIR_NAME}/flight_result_4.json')

        with open(f'{self.OUTPUT_DIR_NAME}/flight_result_1.json', 'r') as test_file:
            test_data_dict = json.load(test_file)
            assert test_data_dict['keroseneAmount'] == 575113.00

        with open(f'{self.OUTPUT_DIR_NAME}/flight_result_2.json', 'r') as test_file:
            test_data_dict = json.load(test_file)
            assert test_data_dict['keroseneAmount'] == 610312.50

    def tearDown(self):
        shutil.rmtree(self.OUTPUT_DIR_NAME)


if __name__ == '__main__':
    unittest.main()
