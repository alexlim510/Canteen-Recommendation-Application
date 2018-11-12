from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

class walking_directions:
    def __init__(self, walking_url):
        self.url = walking_url
        client = urlopen(walking_url)
        page_html = client.read()
        client.close()
        page_soup = soup(page_html, "html.parser")
        self.container = page_soup.div

    def get_from_location(self):
        return self.container.find_all("div", {"class":"locf dir"})[0].text
    
    def get_to_location(self):
        return self.container.find_all("div", {"class":"locf dir"})[1].text
    
    
        # time_lst = ['Total Time', '27 min']
    def get_time_lst(self):
        return [self.container.find_all('div', {'class':'c1'})[0].text, self.container.find_all('div', {'class':'c1'})[1].text]
    # total_time = '27 min'
    def get_total_time(self):
        return self.container.find_all('div', {'class':'c1'})[1].text
    
    def get_distance_lst(self):
        return [self.container.find_all('div', {'class':'c2'})[0].text, self.container.find_all('div', {'class':'c2'})[1].text]
    
    def get_total_distance(self):
        return self.container.find_all('div', {'class':'c1'})[1].text
    
    def get_directions_title(self):
        return [i.text for i in self.container.find_all('h5', {'class':'m_drive'})]
    
    def get_directions_distance(self):
        return [i.text for i in self.container.find_all('div', {'class':'l'})]
    
    def get_directions_directions(self):
        return [i.text for i in self.container.find_all('div', {'class':'r'})]
    
    
class bus_directions:
    def __init__(self, bus_url):
        self.url = bus_url
        client = urlopen(bus_url)
        page_html = client.read()
        client.close()
        page_soup = soup(page_html, "html.parser")
        self.container = page_soup.div

    def get_from_location(self):
        return self.container.find_all("div", {"class":"locf dir"})[0].text
    
    def get_to_location(self):
        return self.container.find_all("div", {"class":"locf dir"})[1].text

    def get_total_time(self):
        return [i.text for i in self.container.find_all('div', {'class':'c1'})]
    
    def get_total_fare(self):
        return [i.text for i in self.container.find_all('div', {'class':'c2'})]
    
    def get_transportation_via(self):
        return [i.text for i in self.container.find_all('div', {'class':'c3'})]

    def get_directions_title(self):
        return [i.text for i in self.container.find_all('h5')]
    
    def get_directions_distance(self):
        return [i.text for i in self.container.find_all('div', {'class':'l'})]
    
    def get_directions_directions(self):
        return [i.text for i in self.container.find_all('div', {'class':'r'})]
"""
bus_url_p_0 = 'http://maps.ntu.edu.sg/m?q=University%20Health%20Service%20Building%20to%20Ananda%20Kitchen&d=b&p=0&fs=m'
bus_url_default = 'http://maps.ntu.edu.sg/m?q=University%20Health%20Service%20Building%20to%20Ananda%20Kitchen&d=b&fs=m'
walk_url = 'http://maps.ntu.edu.sg/m?q=University%20Health%20Service%20Building%20to%20Ananda%20Kitchen&d=w&fs=m'


def walking_url(url):
    client = urlopen(url)
    page_html = client.read()
    client.close()
    
    #html  	parsing
    #print(page_html)
    page_soup = soup(page_html, "html.parser")
    #print(page_soup)
    
    container = page_soup.div
    
    #show from and to in pygame
    from_location = container.find_all("div", {"class":"locf dir"})[0].text
    to_location = container.find_all("div", {"class":"locf dir"})[1].text
    
    print(from_location)
    print(to_location)
    
    # time_lst = ['Total Time', '27 min']
    time_lst = [container.find_all('div', {'class':'c1'})[0].text, container.find_all('div', {'class':'c1'})[1].text]
    # total_time = '27 min'
    total_time = container.find_all('div', {'class':'c1'})[1].text
    
    distance_lst = [container.find_all('div', {'class':'c2'})[0].text, container.find_all('div', {'class':'c2'})[1].text]
    
    total_distance = container.find_all('div', {'class':'c1'})[1].text
    
    
    directions_title = [i.text for i in container.find_all('h5', {'class':'m_drive'})]
    directions_distance = [i.text for i in container.find_all('div', {'class':'l'})]
    directions_directions = [i.text for i in container.find_all('div', {'class':'r'})]
    
    for i in range(len(directions_directions)):
        print(directions_title[i])
        print(directions_distance[i])
        print(directions_directions[i])

def bus_url(url):
    client = urlopen(url)
    page_html = client.read()
    client.close()
    
    #html  	parsing
    #print(page_html)
    page_soup = soup(page_html, "html.parser")
    #print(page_soup)
    
    container = page_soup.div
        
    #show from and to in pygame
    from_location = container.find_all("div", {"class":"locf dir"})[0].text
    to_location = container.find_all("div", {"class":"locf dir"})[1].text
    
    total_time = [i.text for i in container.find_all('div', {'class':'c1'})]
    total_fare = [i.text for i in container.find_all('div', {'class':'c2'})]
    transportation_via = [i.text for i in container.find_all('div', {'class':'c3'})]
    
    for i in range(1, len(total_time)):
        print("Total Time: ", total_time[i])
        print("Total Fare: ", total_fare[i])
        print("Via: ", transportation_via[i])
    
    directions_title = [i.text for i in container.find_all('h5')]
    directions_distance = [i.text for i in container.find_all('div', {'class':'l'})]
    directions_directions = [i.text for i in container.find_all('div', {'class':'r'})]
    
    for i in range(len(directions_directions)):
        print(directions_title[i])
        print(directions_distance[i])
        print(directions_directions[i])

#bus_url(bus_url_p_0)
"""