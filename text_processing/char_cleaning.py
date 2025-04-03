# Defining Cleaning Functions

def clean(strings, unwanted_list, is_a_word = True, make_it_upper = True, replace_with = ' ', ):
# clean eliminates unwanted strings from a Series of strings:

  for k in unwanted_list:

    # Eliminating k occurrences within each title in `strings`
    if make_it_upper == True:
      k = k.upper()
    if is_a_word == True:
      k = ' '+k+' '
    strings = strings.str.replace(k, replace_with)

    # Eliminating k occurrences at the ends of each title in `strings`
    k = k.strip()
    strings = strings.map(lambda x: clean_ends(x,k))

  return strings



def clean_ends(string, unwanted_string, make_it_upper = True, replace_with = ''):
  #clean_ends eliminates unwanted strings at the extremities of a string

  if make_it_upper == True:
    k = unwanted_string.upper()
  else:
    k = unwanted_string

  beg = k+' '
  end = ' '+k

  if string.startswith(beg):
    string = string.replace(beg, string

  if string.endswith(end):
    string = string.replace(end, '', 1)

  return string
