import json
import math

# food_court_1_gps = canteendata['canteen']['Food Court 1']['gps coordinates']
# def calculate_distance_using_gps_coordinates(origin_gps, destination_gps):
#     distance = math.sqrt((origin_gps[0] - destination_gps[0])**2 + (origin_gps[1] - destination_gps[1])**2)
#     return distance 

# dist = calculate_distance_using_gps_coordinates(food_court_1_gps, (1.347057, 103.680109))

class distance_sorted:
    def __init__(self, from_coordinates):
        self.from_coordinates = from_coordinates
        with open('canteen.json', 'r') as f:
            canteendata = json.load(f)
        
        json_canteens = canteendata['canteen']
        num_of_canteens = len(json_canteens)
        dic_distance_canteens = {}
        for canteen in json_canteens:
            print(canteen)
            
    



