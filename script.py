# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:
    #this function changes the strings into floats without the prefix M or B and 'Damages not recorded' is retained
def update_damages(damages):
    updated_damages = []
    for element in damages:
        if element == "Damages not recorded":
            updated_damages.append(element)
        else:
            conversion = {"M": 1000000, "B": 1000000000}
            #the gollowing line of code takes the number part of the string and multiplies it by the conversion of the letter part of the string and appends it to updated damages
            # ex: '1.54B' becomes 1.54*1000000000 and 1540000000 is appended to updated_damages
            updated_damages.append(float(element[:-1])*conversion[element[-1]])
    return updated_damages     

#test
#print(update_damages(damages)) 
#save the updated damages list to updated_damage
updated_damage = update_damages(damages)

# write your construct hurricane dictionary function here:
def hurricane_dict_data(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricane = {}
    #the following for loop adds a key,value pair to hurricane where the key is the name of the hurricane and the value is the dictionary of data of that hurricane
    for i in range(len(names)):
        hurricane[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind" : max_sustained_winds[i], "Areas Affected" : areas_affected[i], "Damage" : updated_damage[i], "Death": deaths[i]}
    return hurricane

#test

#saves the hurricane dictionary data to the variable hurricane
hurricane = hurricane_dict_data(names, months, years, max_sustained_winds, areas_affected, updated_damage, deaths)

#print(hurricane)
# write your construct hurricane by year dictionary function here:
hurricane_by_year = {}
for value in hurricane.values():
    current_year = value["Year"]
    current_cane = value
    
    if current_year not in hurricane_by_year:
         hurricane_by_year[current_year] = current_cane
    else:
        hurricane_by_year[current_year] = [hurricane_by_year[current_year], current_cane]
#print(hurricane_by_year)

# write your count affected areas function here:
def count_affected_areas(hurricane_dict):
    count_affected_areas = {}
    for value in hurricane_dict.values():
        current_affected_areas = value["Areas Affected"]
        for area in current_affected_areas:
            if area in count_affected_areas:
                count_affected_areas[area] += 1
            else:
                count_affected_areas[area] = 1
    return(count_affected_areas)
                
count_affected_areas = count_affected_areas(hurricane) 
    

# write your find most affected area function here:
def most_affected_area(count_affected_areas):
    current_max = 0
    for area in count_affected_areas:
        if count_affected_areas[area] > current_max:
            current_max = count_affected_areas[area]
            max_area = area
    return {max_area:current_max}

#print(most_affected_area(count_affected_areas))
# write your greatest number of deaths function here:
def greatest_num_of_deaths(hurricane):
    name_death_dict = {}
    for value in hurricane.values():
        name_death_dict[value["Name"]] = value["Death"]
    current_max = 0
    for name in name_death_dict:
        if name_death_dict[name] > current_max:
            current_max = name_death_dict[name]
            most_deaths = name
    return {most_deaths: current_max}

#print(greatest_num_of_deaths(hurricane))
        
# write your catgeorize by mortality function here:
mortality_scale = {0:0, 1:100, 2:500, 3:1000, 4:10000}

def mortality_scale(hurricane):
    mortality_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for value in hurricane.values():
        if value["Death"] == 0:
            mortality_dict[0].append(value)
        elif value["Death"] < 100:
            mortality_dict[1].append(value)
        elif value["Death"] < 500:
            mortality_dict[2].append(value)
        elif value["Death"] < 1000:
            mortality_dict[3].append(value)
        elif value["Death"] < 10000:
            mortality_dict[4].append(value)
        else:
            mortality_dict[5].append(value)
    return mortality_dict
     
print(mortality_scale(hurricane))

# write your greatest damage function here:
def greatest_damage(hurricane):
    greatest_damage = 0
    for value in hurricane.values():
        if value["Damage"] == "Damages not recorded":
            continue
        if value["Damage"] > greatest_damage:
            greatest_damage = value["Damage"]
            greatest_cane = value["Name"]
    return {greatest_cane:greatest_damage}

print(greatest_damage(hurricane))

# write your catgeorize by damage function here:

def damage_scale(hurricane):
    damage_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for value in hurricane.values():
        if value["Damage"] == "Damages not recorded":
            continue
        elif value["Damage"] == 0:
            damage_dict[0].append(value)
        elif value["Damage"] < 100000000:
            damage_dict[1].append(value)
        elif value["Damage"] < 1000000000:
            damage_dict[2].append(value)
        elif value["Damage"] < 10000000000:
            damage_dict[3].append(value)
        elif value["Damage"] < 50000000000:
            damage_dict[4].append(value)
        else:
            damage_dict[5].append(value)
    return damage_dict
     
print(damage_scale(hurricane))