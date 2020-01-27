"""
Вася, открывший заправку в прошлом уроке, разорился. Конкуренция оказалась слишком большой. Вася предполагает,
что это произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре.
Определите, сколько заправок на самом деле (не только обозначенных точкой) есть на фрагменте карты
https://stepik.org/media/attachments/lesson/245681/map2.osm
"""
import xmltodict

file_read = open("map2.osm", "r", encoding="utf-8")
xml = file_read.read()
file_read.close()

dict_all = xmltodict.parse(xml)
count_amenity_fuel = 0
for als in dict_all["osm"]:
    for al in dict_all["osm"][als]:
        if "tag" in al:
            tags = al["tag"]
            if isinstance(tags, list):
                for tag in tags:
                    if tag["@k"] == "amenity" and tag["@v"] == "fuel":
                        count_amenity_fuel += 1
            else:
                if tags["@k"] == "amenity" and tags["@v"] == "fuel":
                    count_amenity_fuel += 1

print(count_amenity_fuel)
