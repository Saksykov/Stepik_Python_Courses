"""
В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте.
Ноды могут не только обозначать какой-то точечный объект, но и входить в состав way
(некоторой линии, возможно замкнутой) и не иметь собственных тегов. Для доступного по ссылке
https://stepik.org/media/attachments/lesson/245678/map1.osm фрагмента карты посчитайте,
сколько node имеет хотя бы один вложенный тэг tag, а сколько - не имеют. В качестве ответа введите два числа,
разделённых пробелом.
"""
import xmltodict

read_file = open("map1.osm", "r", encoding="utf-8")
xml = read_file.read()
read_file.close()
map_dic = xmltodict.parse(xml)

nodes_tag = 0
nodes_no_tag = 0
for r in map_dic:
    if "node" in map_dic[r]:
        for i in map_dic[r]:
            if i == "node":
                for j in map_dic[r]["node"]:
                    if "tag" in j:
                        nodes_tag += 1
                    else:
                        nodes_no_tag += 1

print(nodes_tag, nodes_no_tag)
