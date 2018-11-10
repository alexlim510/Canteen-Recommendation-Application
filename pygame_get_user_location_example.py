import pygame

## define event handler for mouse click. 
## this event handler will be fired (activated) when user clicks a mouse button anywhere in the display window
def MouseClick():
   finish = False
   while finish == False:
   ## pygame.event.get() retrieves all events made by user
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
           finish = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            finish = True

   return (mouseX, mouseY)


def get_user_location():
   
   ## make necessary initializations for Width, Height
   W = 1000
   H = 800
   font = pygame.font.SysFont("monospace", 20)
   text1 = font.render("Canteen2", True, (0, 0, 0))
   
   # initialize display window, call it screen
   screen = pygame.display.set_mode((W, H))
   
   # read image file and rescale it to the window size
   screenIm = pygame.image.load("NTU_Campus.png")
   screenIm = pygame.transform.scale(screenIm, (W , H))
   
   # add the image over the screen object
   screen.blit(screenIm,(0, 0))   
   
   # add the text over the screen object
   screen.blit(text1 , (200,300))
   
   #will update the contents of the entire display window
   pygame.display.flip()
   
   while True:
   # get outputs of Mouseclick event handler 
    buttonX, buttonY = MouseClick()
    print((buttonX , buttonY))

def main():
    pygame.init()
    get_user_location()

if __name__ == '__main__':
   main()




"""
from math import pi,sqrt,sin,cos,atan2

def haversine(pos1, pos2):
    lat1 = float(pos1['lat'])
    long1 = float(pos1['long'])
    lat2 = float(pos2['lat'])
    long2 = float(pos2['long'])

    degree_to_rad = float(pi / 180.0)

    d_lat = (lat2 - lat1) * degree_to_rad
    d_long = (long2 - long1) * degree_to_rad

    a = pow(sin(d_lat / 2), 2) + cos(lat1 * degree_to_rad) * cos(lat2 * degree_to_rad) * pow(sin(d_long / 2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    km = 6367 * c
    mi = 3956 * c

    return {"km":km, "miles":mi}




from math import pi,sqrt,sin,cos,atan2

nanyang_staff_housing_gps_coordinates = (1.352433, 103.687333)
nanyang_staff_housing_png_coordinates = (887, 374)
LKCLT_gps_coordinates = (1.342309, 103.682506)
LKCLT_png_coordinates = (207, 631)
# difference in latitude = 0.010124 in coordinates and 680 in pixels
# difference in longitude = 0.004826 in coordinates and -257 in pixels


def haversine(pos1, pos2):
    lat1 = 1.352433
    long1 = 103.687333
    lat2 = 1.342309
    long2 = 103.682506

    degree_to_rad = float(pi / 180.0)

    d_lat = (lat2 - lat1) * degree_to_rad
    d_long = (long2 - long1) * degree_to_rad

    a = pow(sin(d_lat / 2), 2) + cos(lat1 * degree_to_rad) * cos(lat2 * degree_to_rad) * pow(sin(d_long / 2), 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    km = 6367 * c
    mi = 3956 * c

    return {"km":km, "miles":mi}

print(haversine(3,4))
"""