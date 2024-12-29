import numpy as np
import argparse

from genparams import GenParams
from simulation import StateInputOutputVectors, Simulation
from laa_scenarios import ScenariosParser

# Argument parsing
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the LAA simulation. By default, it runs all scenarios in the scenarios.json file.")
    parser.add_argument("-f", "--file_path", type=str, default="scenarios.json", help="The path to the JSON file containing the scenarios.")
    parser.add_argument("-s", "--scenario_name", type=str, default=None, help="The name of the scenario to run.")
    parser.add_argument("-t", "--sim_time_sec", type=int, default=300, help="The end time of the simulation in seconds.")
    parser.add_argument("-e", "--end", type=int, default=300, help="The end time of the attacks in seconds.")
    parser.add_argument("-pc", "--print_continuous_matrices", action="store_true", help="Print the state space matrices in continuous form.")
    parser.add_argument("-pd", "--print_discrete_matrices", action="store_true", help="Print the state space matrices in discrete form.")
    parser.add_argument("-pa", "--plot_all", action="store_true", help="Apart from frequency, also plot RoCoF, Tie-Lines output, ACE, and LFC controller output.")
    args = parser.parse_args()
    if args.end > args.sim_time_sec:
        parser.error("The end time of the attack must be less than or equal to the simulation time.")
    return args


if __name__ == "__main__":
    args = parse_args()
    
    # GENERAL PARAMETERS
    f0 = 60 # Hz
    base_MV = 250 # MV
    n = 3 # number of Areas

    # Generator parameters
    D = np.array([0.015, 0.014, 0.015])
    H = np.array([5.031, 6.051, 3.741])

    # Turbine and governor parameters 
    Tt_general = [0.4, 0.36, 0.42, 0.44, 0.32, 0.4, 0.3, 0.4, 0.41, 0.48]
    Tg_general = [0.08, 0.06, 0.07, 0.06, 0.06, 0.08, 0.07, 0.07, 0.08, 0.06]

    # Droop characteristic
    R_general = [3, 3, 3.3, 2.7273, 2.6667, 2.5, 2.8235, 3, 2.9412, 2.3465]

    # Tie-lines, matrix
    Tij = np.array([[   0,  0.2, 0.25],
                    [ 0.2,    0, 0.12],
                    [0.25, 0.12,    0]])

    
    # SPLITS PARAMETERS
    number_of_splits = 3
    
    # Number of Governor-Turbines in each Area
    m1 = [3, 6, 1]
    m2 = [2, 3, 5]
    m3 = [4, 2, 4]

    # Automatic Generation Control (AGC) parameters
    # Alfa only if many Governor-Turibne in one Area, must sum to 1 in one Area
    alpha1 = [np.array([0.4, 0.6, 0]),
              np.array([0.55, 0.45, 0, 0, 0, 0]),
              np.array([1])]
    alpha2 = [np.array([0.4, 0.6]),
              np.array([0.55, 0.45, 0]),
              np.array([0.34, 0.33, 0.33, 0, 0])]
    alpha3 = [np.array([0.4, 0.6, 0, 0]),
              np.array([0.55, 0.45]),
              np.array([0.34, 0.33, 0.33, 0])]

    Split1_parameters = GenParams(f0, base_MV, n, m1, D, H, Tt_general, Tg_general, R_general, alpha1, Tij)
    Split2_parameters = GenParams(f0, base_MV, n, m2, D, H, Tt_general, Tg_general, R_general, alpha2, Tij)
    Split3_parameters = GenParams(f0, base_MV, n, m3, D, H, Tt_general, Tg_general, R_general, alpha3, Tij)
    GeneratorsParametersList = [Split1_parameters, Split2_parameters, Split3_parameters]
    
    
    # TIME PARAMETERS
    time_step_sec = 0.01
    indexes = np.arange(int(args.sim_time_sec/time_step_sec))
    T = np.array(indexes*time_step_sec, dtype=np.float64).tolist()
    
    
    # LFC CONTROLLERS PARAMETERS
    setpoint = 0
    K = np.array([[4.5, 1.1, 2.8],
                  [4, 1.1, 2.5],
                  [3.8, 1.2, 2.4]])


    # LOAD CHANGE
    initial_loads_pu = np.array([np.zeros(len(T)) for _ in range(n)])
    parser = ScenariosParser("scenarios.json", args.sim_time_sec)
    scenarios = parser.get_all_scenarios()
    for scenario in scenarios:
        if args.scenario_name is not None and scenario["name"] != args.scenario_name:
            continue
                
        for split in range(1): #range(number_of_splits):
            gen_params = GeneratorsParametersList[split]
            state_in_out_vectors = StateInputOutputVectors(gen_params.n, gen_params.m, T, time_step_sec,
                                                        initial_loads_pu, scenario["areas_attacks"])
            simulation = Simulation(gen_params.f0, gen_params.base_MV, gen_params.n, gen_params.m,
                                    gen_params.D, gen_params.H, gen_params.Tt, gen_params.Tg,
                                    gen_params.R, gen_params.alpha, gen_params.beta, gen_params.Tij,
                                    K, setpoint, time_step_sec, T, indexes,
                                    state_in_out_vectors.get_x(), state_in_out_vectors.get_w(),
                                    state_in_out_vectors.get_u(), state_in_out_vectors.get_y())
            simulation.run_and_plot_results(args.print_continuous_matrices, args.print_discrete_matrices,
                                            args.plot_all, scenario)
        
        if scenario["name"] == args.scenario_name:
            break