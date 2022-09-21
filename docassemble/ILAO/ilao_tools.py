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