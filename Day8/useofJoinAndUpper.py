places=[]

for i in range(5):
    place=input("Enter the name of the place {}: ".format(i+1))
    places.append(place)

print("Places: ",places)

# Using join and upper functions
places_string=", ".join(places)
places_upper=places_string.upper()
print("Places in uppercase: ",places_upper)


