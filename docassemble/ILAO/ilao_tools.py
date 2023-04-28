def list_defendants(users, other_parties, any_opposing, party_label):
  """
  For use in the caption of court forms where defendants/respondents are optional.
  Returns the ALPeopleList that is appropriate given the following:
    any_opposing - if True, then there are defendants/respondents
    party_label - if user is defendant/respondent, then the user list should populate the "defendants" in the caption
  """
  
  if party_label == "defendant" or party_label == "respondent":
    return users
  else:
    if any_opposing == True:
      return other_parties
    else:
      return ""
    
def end_in_county(input_county):
  input_lowercase = input_county.lower()
  if input_lowercase.endswith(" county"):
    return input_county
  else:
    return input_county + " County" 
"""
"""
def ilao_court_county_lookup(court_list, lowercase=False):
  all_court_counties = court_list._load_courts()['address_county'].items()
  filtered_courts = [(-1, "cook")] if lowercase else [(-1, "Cook")]
  for court in all_court_counties:
    if court[1] != "Cook":
      court_name = court[1].lower() if lowercase else court[1]
      filtered_courts.append((court[0],court_name))
  return sorted( filtered_courts, key=lambda y: y[1])
"""
"""
def is_illinois_county(address_input):
  if address_input.state == "IL":
    return True
  else:    
    return False
"""  
"""
def county_in_list(court_list, input_county):
  county_name_storage = input_county.lower()
  if county_name_storage.endswith (" county"):
    county_name_storage = input_county.lower()[0:-7]
  county_found_storage = False
  for item in ilao_get_county_list(court_list):
    if county_name_storage == str(item).lower():
      county_found_storage = True
  if county_found_storage == True:
    return True
  else:
    return False
  
def ilao_get_county_list(court_list, lowercase=False):
  county_list = [*set(court_list._load_courts()['address_county'])]
  county_list.sort()
  return county_list
"""
"""
def check_for_cook(input_address):
  if input_address.county.lower()[:4] == "cook":
    return True
  else:
    return False
