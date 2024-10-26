"""
LAA Scenarios
=============

The `laa_scenarios.py` module provides functions to define Load Altering Attack (LAA) scenarios, specifying the start and end times and attack strengths (in per unit, pu) for each area.

Each function in this module has the following signature:

    def get_scenario_name(end: int) -> tuple:

Parameters
----------
:param end: int
    The end time of the simulation in seconds.

Returns
-------
:rtype: tuple

A tuple containing lists of attacks for each area. Each list includes dictionaries with these keys:
- **start** (*int*): The start time of the attack in seconds.
- **end** (*int*): The end time of the attack in seconds.
- **strength** (*float*): Attack strength as a fraction of the load.


Creating a New Scenario
-----------------------
To define a new scenario, create a function that returns the lists of attacks for each area as shown in the example below.

**Structure of the Lists**

The lists of attacks should follow this format:

.. code-block:: python
    area1_attacks = [{"start": start_time1, "end": end_time1, "strength": attack_strength1},
                     {"start": start_time2, "end": end_time2, "strength": attack_strength2},
                     ...,
                     {"start": start_timeN, "end": end, "strength": attack_strengthN}]

The same structure applies to other areas.

Attack Strength
----------------
- **Definition**: The strength parameter specifies the percentage change in load compared to the base system load.
- **Relative to Initial Load**: Each attack strength is relative to the initial load, not cumulative prior values.
- **Example**: A sequence of strengths `0.05` and `-0.05` results in:
    - A 5% load increase (1.05 pu) in the first attack.
    - A return to 0.95 pu, relative to the initial load, in the second attack (NOT 0.9975 pu).

Example
-------
Here's an example of a basic scenario with a 15% load increase in all areas, 5% in each, from 30 seconds until the end of the simulation:

.. code-block:: python
    def get_simple_15_percent_increase_in_all_areas(end: int) -> tuple:
        area1_attacks = [{"start": 30, "end": end, "strength": 0.05}]
        area2_attacks = [{"start": 30, "end": end, "strength": 0.05}]
        area3_attacks = [{"start": 30, "end": end, "strength": 0.05}]
        return area1_attacks, area2_attacks, area3_attacks
"""


def get_simple_5_up_area1(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": 0.05}]
    return area1_attacks, [], []


def get_simple_10_up_area1(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": 0.1}]
    return area1_attacks, [], []


def get_simple_10_up_all(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": 0.04}]
    area2_attacks = [{"start": 30, "end": end, "strength": 0.03}]
    area3_attacks = [{"start": 30, "end": end, "strength": 0.03}]
    return area1_attacks, area2_attacks, area3_attacks


def get_simple_20_up_all(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": 0.07}]
    area2_attacks = [{"start": 30, "end": end, "strength": 0.07}]
    area3_attacks = [{"start": 30, "end": end, "strength": 0.06}]
    return area1_attacks, area2_attacks, area3_attacks


def get_simple_50_up_all(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": 0.17}]
    area2_attacks = [{"start": 30, "end": end, "strength": 0.17}]
    area3_attacks = [{"start": 30, "end": end, "strength": 0.16}]
    return area1_attacks, area2_attacks, area3_attacks


def get_simple_5_down_area1(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": -0.05}]
    return area1_attacks, [], []


def get_simple_10_down_area1(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": -0.1}]
    return area1_attacks, [], []

def get_simple_10_down_all(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": -0.04}]
    area2_attacks = [{"start": 30, "end": end, "strength": -0.03}]
    area3_attacks = [{"start": 30, "end": end, "strength": -0.03}]
    return area1_attacks, area2_attacks, area3_attacks

def get_simple_20_down_all(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": -0.07}]
    area2_attacks = [{"start": 30, "end": end, "strength": -0.07}]
    area3_attacks = [{"start": 30, "end": end, "strength": -0.06}]
    return area1_attacks, area2_attacks, area3_attacks


def get_simple_50_down_all(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": -0.17}]
    area2_attacks = [{"start": 30, "end": end, "strength": -0.17}]
    area3_attacks = [{"start": 30, "end": end, "strength": -0.16}]
    return area1_attacks, area2_attacks, area3_attacks


def get_simple_7_up_area1(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": 0.07}]
    return area1_attacks, [], []


def get_simple_7_up_area2(end: int) -> tuple:
    area1_attacks = []
    area2_attacks = [{"start": 30, "end": end, "strength": 0.07}]
    area3_attacks = []
    return area1_attacks, area2_attacks, area3_attacks


def get_simple_8_up_area3(end: int) -> tuple:
    area1_attacks = []
    area2_attacks = []
    area3_attacks = [{"start": 30, "end": end, "strength": 0.08}]
    return area1_attacks, area2_attacks, area3_attacks
    

def get_simple_5_up_area1_and_8_up_area2(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": 0.1}]
    area2_attacks = [{"start": 30, "end": end, "strength": 0.03}]
    area3_attacks = []
    return area1_attacks, area2_attacks, area3_attacks


def get_simple_7_up_area1_and_8_up_area3(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": 0.07}]
    area2_attacks = []
    area3_attacks = [{"start": 30, "end": end, "strength": 0.08}]
    return area1_attacks, area2_attacks, area3_attacks


def get_simple_6_up_area2_and_4_up_area3(end: int) -> tuple:
    area1_attacks = []
    area2_attacks = [{"start": 30, "end": end, "strength": 0.06}]
    area3_attacks = [{"start": 30, "end": end, "strength": 0.04}]
    return area1_attacks, area2_attacks, area3_attacks


def get_simple_5_up_area1_and_5_up_area2_and_5_up_area3(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": end, "strength": 0.05}]
    area2_attacks = [{"start": 30, "end": end, "strength": 0.05}]
    area3_attacks = [{"start": 30, "end": end, "strength": 0.05}]
    return area1_attacks, area2_attacks, area3_attacks


def get_multistep_5_up_area1_then_7_up_area1(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": 90, "strength": 0.05},
                     {"start": 90, "end": end, "strength": 0.07}]
    return area1_attacks, [], []


def get_multistep_5_up_area2_then_7_up_area2(end: int) -> tuple:
    area2_attacks = [{"start": 30, "end": 90, "strength": 0.05},
                     {"start": 90, "end": end, "strength": 0.07}]
    return [], area2_attacks, []


def get_multistep_5_up_area3_then_8_up_area3(end: int) -> tuple:
    area3_attacks = [{"start": 30, "end": 90, "strength": 0.05},
                     {"start": 90, "end": end, "strength": 0.08}]
    return [], [], area3_attacks


def get_multistep_10_then_11_then_13_areas1_2(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": 90, "strength": 0.05},
                     {"start": 90, "end": 150, "strength": 0.06},
                     {"start": 150, "end": end, "strength": 0.07}]
    area2_attacks = [{"start": 30, "end": 150, "strength": 0.05},
                     {"start": 150, "end": end, "strength": 0.06}]
    return area1_attacks, area2_attacks, []


def get_multistep_10_then_13_then_15_areas1_3(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": 90, "strength": 0.05},
                     {"start": 90, "end": 150, "strength": 0.07},
                     {"start": 150, "end": end, "strength": 0.08}]
    area3_attacks = [{"start": 30, "end": 90, "strength": 0.05},
                     {"start": 90, "end": 150, "strength": 0.06},
                     {"start": 150, "end": end, "strength": 0.07}]
    return area1_attacks, [], area3_attacks


def get_multistep_10_then_13_then_15_areas2_3(end: int) -> tuple:
    area2_attacks = [{"start": 30, "end": 90, "strength": 0.05},
                     {"start": 90, "end": 150, "strength": 0.07},
                     {"start": 150, "end": end, "strength": 0.08}]
    area3_attacks = [{"start": 30, "end": 90, "strength": 0.05},
                     {"start": 90, "end": 150, "strength": 0.06},
                     {"start": 150, "end": end, "strength": 0.07}]
    return [], area2_attacks, area3_attacks


def get_multistep_10_then_15_then_17_all(end: int) -> tuple:
    area1_attacks = [{"start": 30, "end": 90, "strength": 0.04},
                     {"start": 90, "end": 150, "strength": 0.05},
                     {"start": 150, "end": end, "strength": 0.06}]
    area2_attacks = [{"start": 30, "end": 90, "strength": 0.03},
                     {"start": 90, "end": 150, "strength": 0.05},
                     {"start": 150, "end": end, "strength": 0.06}]
    area3_attacks = [{"start": 30, "end": 90, "strength": 0.03},
                     {"start": 90, "end": end, "strength": 0.05}]
    return area1_attacks, area2_attacks, area3_attacks