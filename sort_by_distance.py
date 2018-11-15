import json
import math
import web_scrapper

# food_court_1_gps = canteendata['canteen']['Food Court 1']['gps coordinates']
# def calculate_distance_using_gps_coordinates(origin_gps, destination_gps):
#     distance = math.sqrt((origin_gps[0] - destination_gps[0])**2 + (origin_gps[1] - destination_gps[1])**2)
#     return distance 

# dist = calculate_distance_using_gps_coordinates(food_court_1_gps, (1.347057, 103.680109))

def convert_coordiantes_walking_html(from_coordinates, destination):
    # url for reference 
    # http://maps.ntu.edu.sg/m?q=1.3535285933806145%2C+103.68827099377593&sch_btn=Go&font=+m&t=+Pioneer+Food+Court
    return 'http://maps.ntu.edu.sg/m?q=' + str(from_coordinates[0]) + '%2C+' + str(from_coordinates[1]) + '&sch_btn=Go&font=+m&t=+' + '+'.join(destination.split(' '))

def convert_coordinates_bus_html(from_coordinates, destination):
    # usually for bus there are three options
    # lst of the three bus options
    bus_lst = []
    # http://maps.ntu.edu.sg/m?q=Tanjong%20Hall%20of%20Residence%20-%20Block%2020B%20to%20Pioneer%20Food%20Court&d=b&p=0&fs=m
    bus_0 = 'http://maps.ntu.edu.sg/m?q=' + str(from_coordinates[0]) + '%2C+' + str(from_coordinates[1]) + '%20to%20' + '+'.join(destination.split(' ')) + '&d=b&p=0&fs=m'
    bus_1 = 'http://maps.ntu.edu.sg/m?q=' + str(from_coordinates[0]) + '%2C+' + str(from_coordinates[1]) + '%20to%20' + '+'.join(destination.split(' ')) + '&d=b&p=1&fs=m'
    bus_2 = 'http://maps.ntu.edu.sg/m?q=' + str(from_coordinates[0]) + '%2C+' + str(from_coordinates[1]) + '%20to%20' + '+'.join(destination.split(' ')) + '&d=b&p=2&fs=m'
    bus_lst.extend([bus_0, bus_1, bus_2]) 
    return bus_lst
            
class distance_sorted:
    def __init__(self, from_coordinates):
        self.from_coordinates = from_coordinates
        with open('canteen.json', 'r') as f:
            canteendata = json.load(f)
        
        json_canteens = canteendata['canteen']
        # num_of_canteens = len(json_canteens)
        self.dic_distance_canteens = {}
        for canteen in json_canteens:
        # canteen = 'food court 1'
            print(canteen)
            walking_html = convert_coordiantes_walking_html(from_coordinates, canteen)
            bus_html = convert_coordinates_bus_html(from_coordinates, canteen)
            walking_distance_obj = web_scrapper.walking_directions(walking_html)
            bus_distance_obj_0 = web_scrapper.bus_directions(bus_html[0])
            bus_distance_obj_1 = web_scrapper.bus_directions(bus_html[1])
            bus_distance_obj_2 = web_scrapper.bus_directions(bus_html[2])
            self.dic_distance_canteens[canteen] = [{'walking_distance_obj': walking_distance_obj}, {'bus_distance_obj_0to2)': [bus_distance_obj_0, bus_distance_obj_1, bus_distance_obj_2]}]
    
    def get_distance_dictionary(self):
        return self.dic_distance_canteens

        

distance = distance_sorted((1.3479599, 103.6854919))
distance_dic = distance.get_distance_dictionary()
walk = distance_dic['Food Court 1'][0]['walking_distance_obj']
walk.get_total_distance()
walk.get_total_time()