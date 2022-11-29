counties = ['Arapahoe','Denver',"Jefferson",'El Paso']

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for new_dict in voting_data:
    county = new_dict.get('county')
    voters = new_dict.get('registered_voters')
    print(f"{county} has {voters:,} registered voters")
   
   
 