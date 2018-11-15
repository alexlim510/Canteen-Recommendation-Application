import json
import math

with open('canteen.json', 'r') as f:
    canteendata = json.load(f)

food_court_1_gps = canteendata['canteen']['Food Court 1']['gps coordinates']
def calculate_distance_using_gps_coordinates(origin_gps, destination_gps):
    distance = math.sqrt((origin_gps[0] - destination_gps[0])**2 + (origin_gps[1] - destination_gps[1])**2)
    return distance 

dist = calculate_distance_using_gps_coordinates(food_court_1_gps, (1.347057, 103.680109))
