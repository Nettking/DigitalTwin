from default_values import *

total_watt_pr_day_lights = hours_active_lights * watt_pr_hour_lights
total_watt_pr_day_computer = hours_active_computer * watt_pr_hour_computer
total_watt_pr_day_irrigations = hours_active_irrigations * watt_pr_hour_irrigations

average_total_watt_consumption = total_watt_pr_day_lights + total_watt_pr_day_computer
total_energy_consumption = days_of_cultivation * average_total_watt_consumption


total_cultication_price = total_energy_consumption * price_of_energy_pr_kilo_watt / 1000


number_of_strawberries = int((expected_yield_pr_plant / weight_pr_strawberry) * number_of_pots)

price_pr_strawberry = total_cultication_price / number_of_strawberries