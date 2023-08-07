from energy_prediction.print_predictions import *

def manage_payload(payload):
    param_name = payload["parameter"]
    param_value = payload["value"]

    if param_name == "hours_active_lights":
        global hours_active_lights
        hours_active_lights = float(param_value)

    elif param_name == "hours_active_computer":
        global hours_active_computer
        hours_active_computer = float(param_value)

    elif param_name == "hours_active_irrigations":
        global hours_active_irrigations
        hours_active_irrigations = float(param_value)

    elif param_name == "watt_pr_hour_lights":
        global watt_pr_hour_lights
        watt_pr_hour_lights = float(param_value)

    elif param_name == "watt_pr_hour_computer":
        global watt_pr_hour_computer
        watt_pr_hour_computer = float(param_value)

    elif param_name == "watt_pr_hour_irrigations":
        global watt_pr_hour_irrigations
        watt_pr_hour_irrigations = float(param_value)

    elif param_name == "days_of_cultivation":
        global days_of_cultivation
        days_of_cultivation = float(param_value)

    elif param_name == "price_of_energy_pr_kilo_watt":
        global price_of_energy_pr_kilo_watt
        price_of_energy_pr_kilo_watt = float(param_value)

    elif param_name == "expected_yield_pr_plant":
        global expected_yield_pr_plant
        expected_yield_pr_plant = float(param_value)

    elif param_name == "weight_pr_strawberry":
        global weight_pr_strawberry
        weight_pr_strawberry = float(param_value)

    elif param_name == "number_of_pots":
        global number_of_pots
        number_of_pots = int(param_value)

    return param_name