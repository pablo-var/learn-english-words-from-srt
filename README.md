Function that creates a csv with the words sorted by frequency from a srt file. Only words with more than 1 occurrence. <p>
Stops words not included. Only English. 
  
Test example with the film Artificial Intelligence (Steven Spielberg)
- test.srt (Subtitles)
- test.txt (Subtitle text)
- test.csv (Output)
- test.ipynb (Notebook with command)

You can run with command prompt like this:

python srt_to_csv.py file_name.srt csv_name.csv

Dependencies:
- itertools
- nltk
- collenctions
- pandas
- re, sys

Perfect function in order to learn English efficiently:
- You select the film/tv show you are going to watch.
- Apply the srt_to_csv function to the srt file associate.
- Study the most frequent words you don't know before watching the film/tv show with the 'csv_name' output.
- Watch the film/tv show and see if you remember the words!
- It helps for me!

References :
- https://www.webucator.com/blog/2017/04/simple-python-script-extracting-text-srt-file/
- https://docs.python.org/2/library/collections.html
