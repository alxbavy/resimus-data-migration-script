# Flight Calculation Script

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The script uses a configuration file located at `resources/config-aliases.json`. This file should contain alias mappings required for processing the input data.

Example `config-aliases.json`:
```json
{
    "Керосин": "keroseneAmount",
    "Обеспечение ГСМ": "fuelProvision",
   ...
}
```

## Running the Script

To execute the script, run the following command:

```bash
python script.py <input_file> <output_directory>
```

- `<input_file>`: Path to the input file containing flight data (e.g., `resources/test_flight_table.txt`).
- `<output_directory>`: Directory where the output JSON files will be saved.

### Example

```bash
python script.py test_flight_table.txt results
```

This command processes the input file and saves the result files in the specified output directory.

## Output

The script generates JSON files for each flight result in the output directory.

## Avaliable fields for config
*(Last Update 03.09.2024)*
```
keroseneAmount
fuelProvision
imFluid
totalGsm
takeoffLanding
airSafety
receptionRelease
drinkingWater
cleaning
sanitaryMaintenance
gangWay
towing
towingTug
airLaunching
baggageHatches
stepladder
snowCleaningFluid
parking
foodDelivery
airportExpenses
airportNav
routeNav
totalNav
foreignTotalNav
food
passengerService
terminalUsage
passengersDelivery
passengerExpenses
flightSalary
crewDelivery
crewMedService
techReserves
otherVar
crewExpenses
expensesVar
leasing
airworthiness
salaryFix
techReservesFix
insuranceCustoms
amortization
otherProd
general
nonOperationExpenses
fixedExpenses
contingency
vat
flightHourCost
blockHourCost
flightCost
```