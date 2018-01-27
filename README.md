Function that creates a csv with the words sorted by frequency from a srt file. Only words with more than 1 occurrence
Non-stops words not included. Only English.

Run it like this:

python srt_to_csv.py file_name.srt csv_name.csv

Dependencies:
- itertools
- nltk
- collenctions
- pandas
- re, sys

Perfect function in order to learn english efficiently:
- You select the film/tv show you are going to see.
- Apply the srt_to_csv function to the srt file associate.
- Study the most frequent words you don't know before see the film with the 'csv_name' output.
- Wath the film/tv show and see if you remember the words!
- It helps for me!

Reference : https://www.webucator.com/blog/2017/04/simple-python-script-extracting-text-srt-file/
