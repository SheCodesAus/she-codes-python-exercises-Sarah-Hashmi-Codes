import csv

# with open("2016_pilbara.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)


# population = []

# # with open("2016_pilbara.csv", encoding= "utf-8") as csv_file:
# #     reader = csv.reader(csv_file)
# #     for line in reader:
# #         population.append(line)

# # print(population)
# # print()

# # for age_group in population:
# #     print(f"{age_group[0]} {age_group[1]}")


# # #alternative way to convert to list of 

# with open('colours_20.csv') as csv_file:
#     reader = csv.reader(csv_file)
#     population = list(reader)

# print(population)



# # # #writing to csv file








# with open("populationp.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")

#     for color in population:
#         csv_writer.writerow([color[1], color[2], color[4]])






# # #writing to csv file




# color= []

# color1 = "Red"
# color2 = "Green"
# color3 = "Blue"
# color4 = "yellow"

# with open("colours_20.csv", encoding= "utf-8") as csv_file:
#     reader = csv.reader(csv_file)

#     for row in color:
#         if color4 in [4]:
#             rows += 1
#         print(row)




 







#open a file in editavle mode
# f = open("file.txt", "w")
# f.write("Hello world")
# f.close()

# # Open a file in readable mode only
# f = open("file.txt", mode="r")
# print(f.read())
# print(f.read())
# f.close()


# with open("file.text", mode="r") as my_file:
#     print(my_file.read())


#question 2

import csv

with open("colours_20_simple.csv") as colours_csv:
    colours_csv_reader = csv.reader(colours_csv)
    header = next(colours_csv_reader)
    casted_colours_list = list(colours_csv_reader)

    for row in colours_csv_reader:
        print(f"{row[2]}, Hex:{row[1]}, RGB:{row[2]}")




#question 4


# red_counter = 0
# green_counter = 0
# blue_counter = 0
# yellow_counter = 0

# with open("colours_20.csv") as colours_csv:
#     reader = csv.reader(colours_csv)

#     for row in reader:
#         if "red" in row[4]:
#             red_counter += 1
#         elif "green" in row[4]:
#             green_counter += 1
#         elif "blue" in row[4]:
#             blue_counter += 1
#         elif "yellow" in row[4]:
#             yellow_counter += 1

# print(f"Red: {red_counter}")
# print(f"Green: {green_counter}")
# print(f"Blue: {blue_counter}")
# print(f"Yellow: {yellow_counter}")


#question 5

max_velocity = 0
min_velocity = 99999999
max_galaxy = ""
min_galaxy = ""

with open(".csv_files/galaxies.csv") as galaxies_csv:
    reader = csv.reader(galaxies_csv)
    next(galaxies_csv)
    for row in reader:
        if int(row[1]) > max_velocity:
            max_velocity = int(row[1])
            max_galaxy = int(row[0])
        
        elif int(row[1]) < max_velocity:
            min_velocity = int(row[1])
            min_galaxy = int(row[0])

print(f"Galaxy {min_galaxy} has the min velocity of {min_velocity}")
print(f"Galaxy {max_galaxy} has the min velocity of {max_velocity}")


