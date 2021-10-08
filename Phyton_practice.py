# counties = ["Arapahoe", "Denver", "Jefferson"]
# counties.insert(1,"El Paso")
# print(counties)
# counties.remove("Arapahoe")
# print(counties)
# counties[1]= "Jefferson"
# counties[2]= "Denver"
# print(counties)
# counties.append("Arapahoe")
# print(counties)
#counties_tuple = ("Arapahoe","Denver","Jefferson")
# print(len(counties_tuple))
#print(counties_tuple[1])
# counties_dict = {}
# counties_dict["Arapahoe"]=422829
# # print(counties_dict)
# counties_dict['Denver']=463353
# counties_dict["Jefferson"]=432438
# # print(counties_dict)
# print(counties_dict.items())
# print(counties_dict.keys())
# print(counties_dict.values())
# print(counties_dict.get("Denver"))
# print(counties_dict['Arapahoe'])


# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# print(voting_data)
# voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})
# voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
# print(voting_data)
# voting_data[1]= ({"county":"Jefferson", "registered_voters": 432438})
# voting_data[2]= ({"county":"Denver", "registered_voters": 463353})
# print(voting_data)
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# print(voting_data)

# # print(len(voting_data))
# # print(voting_data[1])
# print(voting_data["county":"Arapahoe"] == "registered_voters": 11111])

# How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
# # Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calvulate the percentage of votes you received.
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == "Denver":
#     print(counties[1])
# print(counties.items())

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# What is the score?
# score = int(input("What is your test score? "))

# Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')

# What is the score?
# score = int(input("What is your test score? "))

# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#While loops
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

#For loops
# counties = ["Arapahoe","Denver","Jefferson"]
# for county in counties:
#     print(county)

#range()
# for i in range(len(counties)):
#     print(counties[i])

#iterate through a tuple
# counties_tuple = ("Arapahoe","Denver","Jefferson")
# for i in range(len(counties_tuple)):
#     print(counties_tuple[i])
# # or
# for county in counties_tuple:
#     print(county)

#iterate through a dictionary
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# #get keys
# for county in counties_dict.keys():
#     print(county)
# #get values
# for voters in counties_dict.values():
#     print(voters)
#dictionary_name[key]
# for county in counties_dict:
#     print(counties_dict[county])
# #or
# for county in counties_dict:
#     print(counties_dict.get(county))

#sill_drill
# get key-value pairs
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")
#or
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)
# #for range()
#  for i in range(len(voting_data)):
#     print(counties[i])
#To get the values from a list of dictionaries
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
#To get the county name       
# for county_dict in voting_data:
#     print(county_dict['county'])
#To get the registered_voters
# for county_dict in voting_data:
#     print(county_dict['registered_voters'])

#candidate votes
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# print(message_to_candidate)

#skill_drill
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, registered_voters in range(len(voting_data)):
    print(f'{county} county has {registered_voters} registered voters.')
