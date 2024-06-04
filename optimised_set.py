def min_units_for_value(units, value, count_map):
    if value == 0:
        return 0
    if value in count_map:
        return count_map[value]
    
    min_units = float('inf')
    for unit in units:
        if unit <= value:
            num_units = min_units_for_value(units, value - unit, count_map) + 1
            if num_units < min_units:
                min_units = num_units
                
    count_map[value] = min_units
    return min_units

def calculate_avg_units(units, max_value):
    count_map= {}
    total_units = 0
    for value in range(1, max_value):
        total_units += min_units_for_value(units, value, count_map)
    avg_units = total_units / max_value
    print(count_map)
    return avg_units

# Given units
units = list(map(int,input().split()))
max_value = int(input())

# Calculate the average number of units used
avg_units = calculate_avg_units(units, max_value)
print(f"Average number of units used: {avg_units:.1f}")
