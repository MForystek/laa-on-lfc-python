"""
LAA Scenarios
-----

The `laa_scenarios.py` module provides a parsing for Load Altering Attack (LAA) scenarios defined in JSON file.

Classes
-------
- ScenariosParser

    A class to parse and manage LAA scenarios.
"""

import json

class ScenariosParser:
    """
    ScenarioParser
    -----
    A class to parse and manage LAA scenarios.

    Methods
    -------
    - __init__(json_file_path: str, end: int) -> None
    
        Initializes the ScenariosParser object by parsing the scenarios from a JSON file.
    
    - get_all_scenarios() -> list
    
        Returns all parsed scenarios.

    - get_scenario_attacks(scenario_name: str) -> list
    
        Returns the attacks for a specific scenario by name.

    Parameters
    ----------
    json_file_path: str
        The path to the JSON file containing the scenarios.
    end: int
        The end time of the attack in seconds.

    Scenario structure after parsing
    -------
    A list of scenarios, where each scenario is a dictionary containing:
    - name (str): The name of the scenario.
    - description (str): A description of the scenario.
    - areas_attacks (list): A list of attacks for each area. Each attack is a dictionary with these keys:
        - start (int): The start time of the attack in seconds.
        - end (int): The end time of the attack in seconds.
        - strength (float): Attack strength as a fraction of the load.

    Example
    -------
    Here's an example of how to use the ScenariosParser class:

    .. code-block:: python
        parser = ScenariosParser("scenarios.json", 300)
        scenario_attacks = parser.get_scenario_attacks("Multi_10_15_16_up_all")
    """
    
    def __init__(self, json_file_path: str, end: int) -> None:
        with open(json_file_path) as json_file:
            self._scenarios = [scenario for scenario in json.load(json_file)]
            for scenario in self._scenarios:
                for i, area_attacks in enumerate(scenario["areas_attacks"]):
                    area_attacks["ends"] = []
                    if len(area_attacks["starts"]) > 1:
                        area_attacks["ends"] = area_attacks["starts"][1:]
                    area_attacks["ends"].append(end)
                    
                    attacks = []
                    for start, end, strength in zip(area_attacks["starts"], area_attacks["ends"], area_attacks["strengths"]):
                        
                        attacks.append({"start": start, "end": end, "strength": strength})
                    scenario["areas_attacks"][i] = attacks
                    
    def get_all_scenarios(self) -> list:
        return self._scenarios
    
    def get_scenario_attacks(self, scenario_name: str) -> list:
        for scenario in self._scenarios:
            if scenario_name == scenario["name"]:
                return scenario["areas_attacks"]
        return []
