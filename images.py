# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 10:33:50 2020

@author: Hugo
"""
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def start_search():
    # Making search and downloading HTTML
    query = input("What do you want to search?\n")
    
    # build the google query
    search_url = "https://www.google.com/search?safe=on&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    
    r = requests.get(search_url.format(q=query))
    
    # Parsing soup
    soup = BeautifulSoup(r.text)
    # links = soup.find_all("a", {"class": "mimg"})
    links = soup.find_all("img")
    
    i = 1
    for item in links:
        if item.attrs["src"] and "http" in item.attrs["src"]:
            img_obj = requests.get(item.attrs["src"])
            print("Status_code:", img_obj.status_code)
            
            folder_name = query.replace(" ", "_").lower()
            dir_name = f"./{folder_name}"
            # Create folder if none exist
            if not os.path.isdir(dir_name):
                os.makedirs(dir_name)
            
            if img_obj.status_code == 200:     
                print("Getting:", item.attrs["src"])    
                img = Image.open(BytesIO(img_obj.content))
                path = f"./{query}{i}." + img.format.lower()
                img.save(f"./{dir_name}/{path}", img.format)
                i += 1

            else:
                print("An error occured")
    start_search()
    
start_search()