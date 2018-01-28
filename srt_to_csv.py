"""
Creates a csv with the most command words from a srt file.
"""
import re, sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from itertools import dropwhile
import pandas as pd


def is_time_stamp(l):
  if l[:2].isnumeric() and l[2] == ':':
    return True
  return False

def has_letters(line):
  if re.search('[a-zA-Z]', line):
    return True
  return False

def has_no_text(line):
  l = line.strip()
  if not len(l):
    return True
  if l.isnumeric():
    return True
  if is_time_stamp(l):
    return True
  if l[0] == '(' and l[-1] == ')':
    return True
  if not has_letters(line):
    return True
  return False

def is_lowercase_letter_or_comma(letter):
  if letter.isalpha() and letter.lower() == letter:
    return True
  if letter == ',':
    return True
  return False

def clean_up(lines):
  """
  Get rid of all non-text lines and
  try to combine text broken into multiple lines
  """
  new_lines = []
  for line in lines[1:]:
    if has_no_text(line):
      continue
    elif len(new_lines) and is_lowercase_letter_or_comma(line[0]):
      #combine with previous line
      new_lines[-1] = new_lines[-1].strip() + ' ' + line
    else:
      #append line
      new_lines.append(line)
  return new_lines

def main(args):
  """
    args[1]: file name
    args[2]: csv name
    args[3]: encoding. Default: utf-8.
      - If you get a lot of [?]s replacing characters,
      - you probably need to change file_encoding to 'cp1252'
  """
  file_name = args[1]
  file_encoding = 'utf-8' if len(args) < 4 else args[3]
  with open(file_name, encoding=file_encoding, errors='replace') as f:
    lines = f.readlines()
    new_lines = clean_up(lines)
  new_file_name = file_name[:-4] + '.txt'
  with open(new_file_name, 'w') as f:
    for line in new_lines:
      f.write(line)
  with open(new_file_name, 'r') as myfile:
    data = re.sub('\W+',' ', myfile.read()).replace('\n', '').lower()
  stop_words = set(stopwords.words("english"))  # load stopwords
  words = [w for w in data.split(" ") if w not in stop_words]
  new_data = Counter(words)
  for key, count in dropwhile(lambda key_count: key_count[1] >= 2, new_data.most_common()):
    del new_data[key]
  df = pd.DataFrame.from_dict(new_data.most_common())
  df.columns = ['word', 'occurrences']
  csv_name = args[2]
  df.to_csv(csv_name, index = False)
if __name__ == '__main__':
    main(sys.argv)