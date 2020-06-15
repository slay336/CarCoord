# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs
from resources.vehicles import event_mapping

with open("bmw_rovers.xml", "r") as file:
    content = file.read().replace("\n", "")

soup = bs(content, features='xml')

for event in soup.contents[0].findAll("event"):
    for pos in event.children:
        if pos.name == 'pos':
            car = event_mapping[event["name"]](float(pos.attrs["x"]), float(pos.attrs["z"]))
            print(car)
