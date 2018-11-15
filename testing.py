import pygame
import web_scrapper
#import google_maps
#from pygame.locals import *

pygame.init()


# take this to be top left point
hall_12_bus_stop_coordinates = (1.351937, 103.680543)
hall_12_pixel_coordinates = (317, 503) # when scale = 3

# take this to be bottom right point
hall_1_bus_stop_coordinates = (1.345645, 103.687804)
hall_1_pixel_coordinates = (799, 926) # when scale = 3

difference_in_pixels = (hall_1_pixel_coordinates[0] - hall_12_pixel_coordinates[0], hall_1_pixel_coordinates[1] - hall_12_pixel_coordinates[1])
difference_in_coordinates = (hall_1_bus_stop_coordinates[0] - hall_12_bus_stop_coordinates[0], hall_1_bus_stop_coordinates[1] - hall_12_bus_stop_coordinates[1])

map = pygame.image.load('map.png')
scale = 3 # used to scale the image
display_width = round(map.get_width() / scale)
display_height = round(map.get_height() / scale)
screen = pygame.display.set_mode([display_width,display_height])

scaled_map = pygame.transform.scale(map, (display_width, display_height))

click = (0, 0)

def event_handler():
    for event in pygame.event.get():
        #print(event) # this prints all the events detected by pygame.
        if event.type == pygame.QUIT:
            pygame.quit()
            quit() # stop python program execution 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pos()
            #print(click)
            #print(difference_in_pixels)
            ratio = ((click[0]-hall_12_pixel_coordinates[0])/difference_in_pixels[0], (click[1]-hall_12_pixel_coordinates[1])/difference_in_pixels[1])
            #print(ratio)
            new_coordinates = (hall_12_bus_stop_coordinates[0]+difference_in_coordinates[0]*ratio[1], hall_12_bus_stop_coordinates[1]+difference_in_coordinates[1]*ratio[0])
            print(new_coordinates)
            return new_coordinates
        
#            destination = "Pioneer Food Court"
#            walking_url = convert_coordiantes_walking_html(new_cooridnates, destination)
#            bus_url = convert_coordinates_bus_html(new_cooridnates, destination)[0]
#            print()
#            print()
#            print(bus_url)
#            bus_dir = web_scrapper.bus_directions(bus_url)
#            print()
#            print()
#            print()
#            print('From:', bus_dir.get_from_location())
#            print('To:', bus_dir.get_to_location())
#            time_lst = bus_dir.get_total_time()
#            fare_lst = bus_dir.get_total_fare()
#            via_lst = bus_dir.get_transportation_via()
#            print(time_lst[0], time_lst[1])
#            print(fare_lst[0], fare_lst[1])
#            print(via_lst[0], via_lst[1])
#            title = bus_dir.get_directions_title()
#            distance = bus_dir.get_directions_distance()
#            directions_lst = bus_dir.get_directions_directions()
#            for i in range(len(directions_lst)):
#                print(title[i])
#                print(distance[i])
#                print(directions_lst[i])


game_running = True

while game_running:
    event_handler()
    screen.blit(scaled_map, (0, 0))
    pygame.display.flip()