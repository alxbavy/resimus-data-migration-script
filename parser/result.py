import json
import os
import pathlib
from dataclasses import dataclass


OUTPUT_FILE_NAME = 'flight_result'
CONFIG_ALIASES_NAME = 'resources/config-aliases.json'


@dataclass
class FlightCalcualtionResult:
    keroseneAmount: float = None
    fuelProvision: float = None
    imFluid: float = None
    totalGsm: float = None
    takeoffLanding: float = None
    airSafety: float = None
    receptionRelease: float = None
    drinkingWater: float = None
    cleaning: float = None
    sanitaryMaintenance: float = None
    gangWay: float = None
    towing: float = None
    towingTug: float = None
    airLaunching: float = None
    baggageHatches: float = None
    stepladder: float = None
    snowCleaningFluid: float = None
    parking: float = None
    foodDelivery: float = None
    airportExpenses: float = None
    airportNav: float = None
    routeNav: float = None
    totalNav: float = None
    foreignTotalNav: float = None
    food: float = None
    passengerService: float = None
    terminalUsage: float = None
    passengersDelivery: float = None
    passengerExpenses: float = None
    flightSalary: float = None
    crewDelivery: float = None
    crewMedService: float = None
    techReserves: float = None
    otherVar: float = None
    crewExpenses: float = None
    expensesVar: float = None
    leasing: float = None
    airworthiness: float = None
    salaryFix: float = None
    techReservesFix: float = None
    insuranceCustoms: float = None
    amortization: float = None
    otherProd: float = None
    general: float = None
    nonOperationExpenses: float = None
    fixedExpenses: float = None
    contingency: float = None
    vat: float = None
    flightHourCost: float = None
    blockHourCost: float = None
    flightCost: float = None


def get_routes_count(lines):
    for line in lines:
        splitted_line = line.replace('\n', '').split(';')
        if splitted_line[0].startswith('Прилет, город'):
            splitted_line_with_arrival_cities = splitted_line
    for i, city in enumerate(splitted_line_with_arrival_cities, start=1):
        if city == '':
            return -1 + i - 1


def execute(input_file_name, output_directory, config_file_name):
    with open(config_file_name, 'r', encoding='utf-8') as f:
        ru_field_dict = json.load(f)

    with open(input_file_name, 'r', encoding='utf-8') as f:
        lines: str = f.readlines()

    flight_calculation_results: list[dict] = list()
    for i in range(get_routes_count(lines)):
        flight_calculation_results.append(FlightCalcualtionResult().__dict__)

    for line in lines:
        splitted_line = line.replace('\n', '').split(';')
        result_name_ru = splitted_line[0]
        result_name_field = ru_field_dict.get(result_name_ru)
        if result_name_field is not None:
            for i, flight_calculation_result_dict in enumerate(flight_calculation_results, start=1):
                flight_calculation_result_dict[result_name_field] = float(
                    splitted_line[i].replace(' ', '').replace(',', '.')
                )

    if not os.path.isdir(output_directory):
        os.mkdir(output_directory)

    for i, flight_calculation_result in enumerate(flight_calculation_results, start=1):
        with open(f'{output_directory}/{OUTPUT_FILE_NAME}_{i}.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(flight_calculation_result, indent=4))