from char_cleaning import clean, clean_ends
from grammar_elements import punctuations, articles, conjunctions, prepositions, pronouns, prefixes, auxiliary_verbs, adverbs

def words_grinder(strings, clean_punct = True, garbage_list = None):
  # This function will take a Pandas Series of dated strings,
  # and return a long DataFrame of single upper case words;
  # it will eliminate punctuation, spaces,
  # auxiliary verbs, pronouns, and articles

  # Converting all strings to upper case
  strings = strings.str.upper()

  # Eliminating contracted negations
  strings = strings.str.replace("N\'T", '')

  # Eliminating contracted possesives
  strings = strings.str.replace("\'S", '')

  # Cleaning punctuation
  if clean_punct == True:
    strings = clean(strings, punctuations, is_a_word = False, replace_with = '')

  # Trimming empty trailing or leading spaces
  strings = strings.str.strip()

  # Cleaning all words in garbage_list from strings
  for words_list in garbage_list:
    strings = clean(strings, words_list, make_it_upper = True)

  return strings
