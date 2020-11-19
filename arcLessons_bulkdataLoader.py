from arcgis import GIS
import json
import csv

count=1

gis=GIS('http://xxxxxx.maps.arcgis.com','','')

# Option types: PDF, DOC, MP4 (dump), and ZIP

#Read CSV and loop over all non-MP4 records
file = csv.reader(open('data/ArcLessons2020.csv'), delimiter=',')
for line in file:
    try:
        if (line[1][-3:] is not 'mp4') or (line[1][-3:] is not 'zip'):
            print(line[0], " :: ", line[1][-3:])
            data = "_backup/arclessons/" + line[1]
            item_properties = {
                "title": line[0],
                "tags" : "ArcLessons, legacy, 1997-2007, lessons",
                "snippet": line[3],
                "description": "Date originally posted: " + line[2]+ "<br /> Original author on file: " + line[5]  + "<br /> Description: " + line[3],
                "type": "GeoPackage",
                "folder": "library",
                "access": "org",
                "licenseInfo": "Where possible this content is licensed under Creative Commons (BY-NC-SA)",
                "typeKeywords": "Data"
                }
            item = gis.content.add(item_properties, data, folder='library')
            item.share(org=True)
    except:
        print('Record error: ', line[0])

print('done.')