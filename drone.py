import json
from itertools import combinations

def calculate_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)  # Manhattan distance

def calculate_time(distance, speed):
    return distance / speed  # Time in seconds

def assign_orders_to_drones(drones, orders):
    assignments = []
    available_drones = [d for d in drones if d['available']]
    
    # Sort orders by shortest distance first, then by deadline
    orders.sort(key=lambda o: (calculate_distance(0, 0, o['delivery_x'], o['delivery_y']), o['deadline']))
    
    for drone in available_drones:
        assigned_orders = []
        remaining_payload = drone['max_payload']
        remaining_distance = drone['max_distance']
        total_travel_time = 0
        total_distance_covered = 0
        
        current_x, current_y = 0, 0  # Start at (0,0)
        
        for order in orders[:]:  # Iterate over a copy to allow removal
            travel_distance = calculate_distance(current_x, current_y, order['delivery_x'], order['delivery_y'])
            travel_time = calculate_time(travel_distance, drone['speed']) / 60  # Convert to minutes
            
            if (
                remaining_payload >= order['package_weight'] and
                remaining_distance >= travel_distance
            ):
                assigned_orders.append({
                    'order': order['id'],
                    'time_taken': round(total_travel_time + travel_time, 2),  # Incremental travel time
                    'distance': travel_distance
                })
                remaining_payload -= order['package_weight']
                remaining_distance -= travel_distance
                total_travel_time += travel_time
                total_distance_covered += travel_distance
                current_x, current_y = order['delivery_x'], order['delivery_y']
                orders.remove(order)  # Remove assigned order from available list
        
        # Confirm round trip return to (0,0)
        return_distance = calculate_distance(current_x, current_y, 0, 0)
        return_time = calculate_time(return_distance, drone['speed']) / 60
        total_travel_time += return_time
        total_distance_covered += return_distance
        
        if assigned_orders:
            assignments.append({
                'drone': drone['id'],
                'orders': assigned_orders,
                'total_time': round(total_travel_time, 2),
                'total_distance': total_distance_covered
            })
    
    return assignments

# Load input JSON
def main():
    with open('input1.json', 'r') as f:
        data = json.load(f)
    
    drones = data['drones']['fleet']
    orders = data['orders']
    
    result = assign_orders_to_drones(drones, orders)
    
    # Save output JSON
    with open('output.json', 'w') as f:
        json.dump({'assignments': result}, f, indent=4)
    
    print("Optimized assignments saved in output.json")

if __name__ == "__main__":
    main()
