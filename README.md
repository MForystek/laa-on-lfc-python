# LLA on LFC

The project is a simulation of the Load Frequency Control mechanism of the Power System with the addition of performing Load Altering Attacks (LAAs).

The simulated system comprises of 10 generator units dividen into three areas in three different ways based on the IEEE 39-bus system.

The simulation was done as a part of the research at KAUST.

The project uses Python version `3.12.7`.

## Run

To run simulation use `python main.py`.

## Scenarios

### Choose scenario

To choose from the existing scenarios in `main.py` set variable `attack_scenario` to the function from `laa_scenarios.py` which returns the choosen scenario.

#### Example

`attack_scenario = get_simple_5_percent_increase_in_all_areas(sim_time_sec)`

### Create scenario

To learn how to create scenarios check documentation of module `laa_scenarios.py`.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).