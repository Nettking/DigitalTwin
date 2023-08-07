from calculate_predictions import *

def print_predictions(hours_active_lights, 
                      hours_active_computer, 
                      hours_active_irrigations, 
                      watt_pr_hour_lights, 
                      watt_pr_hour_computer, 
                      watt_pr_hour_irrigations, 
                      days_of_cultivation, 
                      price_of_energy_pr_kilo_watt, 
                      expected_yield_pr_plant, 
                      weight_pr_strawberry, 
                      number_of_pots):
    print("Digital Twin Strawberry Energy Predictions:")
    
    print("Number of pots:", number_of_pots)

    print("Hours active per day (lights):", hours_active_lights)
    print("Hours active per day (computer):", hours_active_computer)
    print("Hours active per day (irrigation):", hours_active_irrigations)

    print("Watt per hour (lights):", watt_pr_hour_lights)
    print("Watt per hour (computer):", watt_pr_hour_computer)
    print("Watt per hour (irrigation):", watt_pr_hour_irrigations)

    print("Total watt per day (lights):", total_watt_pr_day_lights)
    print("Total watt per day (computer):", total_watt_pr_day_computer)
    print("Total watt per day (irrigation):", total_watt_pr_day_irrigations)

    print("Average total watt consumption per day:", average_total_watt_consumption)

    print("Days of cultivation:", days_of_cultivation)
    print("Total energy consumption (Watt):", total_energy_consumption)
    print("Price of energy per kilowatt:", price_of_energy_pr_kilo_watt)
    print("Total cultivation price (Kr):", total_cultication_price)

    print("Expected yield per plant (grams):", expected_yield_pr_plant)
    print("Weight per strawberry (grams):", weight_pr_strawberry)
    
    print("Expected yield (number of strawberries):", number_of_strawberries, "Strawberries")

    print("Price per strawberry (Kr):", price_pr_strawberry, "Kr/Strawberry")


if __name__ == "__main__":
    print_predictions(hours_active_lights, 
                      hours_active_computer, 
                      hours_active_irrigations, 
                      watt_pr_hour_lights, 
                      watt_pr_hour_computer, 
                      watt_pr_hour_irrigations, 
                      days_of_cultivation, 
                      price_of_energy_pr_kilo_watt, 
                      expected_yield_pr_plant, 
                      weight_pr_strawberry, 
                      number_of_pots)