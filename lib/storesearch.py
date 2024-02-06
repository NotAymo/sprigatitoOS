import time
import os

print("Searchbar :")
searchbar = input ("Type keywords :")
if searchbar.lower() == "Search":
    exec(open('src/lib/keywordssearch.py').read())