import utm

temp_utm = utm.from_latlon(37.16967026158049,127.08544589680444) # ( latitude, longitude)
# retrun value => (EASTING, NORTHING, ZONE_NUMBER, ZONE_LETTER)
print(temp_utm)
print(temp_utm[0])
print(temp_utm[1])
print(temp_utm[2])