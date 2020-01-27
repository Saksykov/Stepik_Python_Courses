"""
Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить количество заправок
в интересующем его районе. Вася скачал интересующий его кусок карты OSM
https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать, сколько на нём отмечено
точечных объектов (node), являющихся заправкой. В качестве ответа вам необходимо вывести одно число - количество АЗС.
"""
import xmltodict

file_read = open("map2.osm", "r", encoding="utf-8")
xml = file_read.read()
file_read.close()

dict_all = xmltodict.parse(xml)
count_amenity_fuel = 0
for node in dict_all["osm"]["node"]:
    if "tag" in node:
        tags = node["tag"]
        if isinstance(tags, list):
            for tag in tags:
                if tag["@k"] == "amenity" and tag["@v"] == "fuel":
                    count_amenity_fuel += 1
        else:
            if tags["@k"] == "amenity" and tags["@v"] == "fuel":
                count_amenity_fuel += 1

print(count_amenity_fuel)

