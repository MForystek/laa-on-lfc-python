# LLA on LFC

The project is a simulation of the Load Frequency Control mechanism of the Power System with the addition of Static and Multistep Load Altering Attacks (LAAs).

The simulated system comprises of 10 generator units dividen into three areas in three different ways based on the IEEE 39-bus system.

The simulation was done as a part of the research at KAUST.

## Installation

Recommended Python version: `3.12.7`.

Setup a virtual environment and install required packages.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt`
```

## Run

To run all scenarios from the file `scenarios.json` use 
```bash
python main.py
```

To run a single scenario use
```bash
python main.py --scenario_name <scenario_name>
```

To run scenarios from different file use
```bash
python main.py --file_name <path_to_file>
```

To learn about additional arguments use
```bash
python main.py --help
```

### Create custom scenario

To learn how to create custom scenarios look at the examples in `scenarios.json` and documentation in `laa_scenarios.py`.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).