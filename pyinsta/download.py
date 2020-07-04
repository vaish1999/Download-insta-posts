#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:55:34 2020

@author: Vaishakh
"""

import requests
import urllib.parse
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import json
import urllib
import os,sys

def post( username = "indianairforce", p1 = 1, p2 = 1 ):
    """
    

    Parameters
    ----------
    username : 
        TYPE->string
        DESCRIPTION->The username of the celebrity. 
        The default is "indianairforce".
    p1 : 
        TYPE->Integer
        DESCRIPTION->The serial number of the post you want 
        to download from the celebrity's feed. 
        The default is 1.
    p2 : 
        TYPE->Integer
        DESCRIPTION->The serial number of the picture in the post(if many) 
        you want to download from the celebrity's feed. 
        The default is 1.

    Returns
    -------
    Saves the picture or video in the instagram_downloads folder

    """
    url = "https://www.instagram.com/{}/".format(username)
    try:
        p_dir=""
        path = os.path.join(p_dir, "instagram_downloads")
        os.mkdir(path,0o777)
    except FileExistsError:
        print("")
    session = requests.session()
    
    
    #opening the URL and parsing it into BeautifulSoup
    try:
        html = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    except:
        print("Page not found or No internet connection")
        sys.exit()
    
    soup = BeautifulSoup(html, 'html.parser')
    tags = (soup.find_all('body'))[0].find_all('script')
    
    s=(str(tags[0])[52:-10])
    
    pic_json=json.loads(s)
    
    temp=pic_json["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][p1-1]["node"]
    
    if temp["is_video"]:
        video_url="https://www.instagram.com/p/"+temp["shortcode"]+"/"
        sess=requests.session()
        video_page = sess.get(video_url,headers={'User-Agent': 'Mozilla/5.0'}).text
        tree=BeautifulSoup(video_page, 'html.parser')
        tags = (tree.find_all('body'))[0].find_all('script')
        s=(str(tags[0])[52:-10])
        pic_json=json.loads(s)
        video_play_url=pic_json["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]["video_url"]
        resource = urllib.request.urlopen(video_play_url)
        output = open("instagram_downloads/"+username +"_"+str(p1)+ ".mp4", "wb")
        output.write(resource.read())
        output.close()

    
    else:
        try:
            pic_url=temp["edge_sidecar_to_children"]["edges"][p2-1]["node"]["display_url"]
            
        except KeyError:
            pic_url=temp["display_url"]
        response = session.get(pic_url, headers={'User-Agent': 'Mozilla/5.0'}).content
        img = Image.open(BytesIO(response))
        img.show()
        img.save("instagram_downloads/"+username+"_"+str(p1)+"_"+str(p2)+".jpg")
        
        
def profile_pic( username = "indianairforce" ):
    """
    

    Parameters
    ----------
    username : 
        TYPE->string
        DESCRIPTION->The username of the celebrity. 
        The default is "indianairforce".

    Returns
    -------
    Saves the profile picture in the instagram_downloads folder

    """
    url = "https://www.instagram.com/{}/".format(username)
    try:
        p_dir=""
        path = os.path.join(p_dir, "instagram_downloads")
        os.mkdir(path,0o777)
    except FileExistsError:
        print("")
    session = requests.session()
    
    
    #opening the URL and parsing it into BeautifulSoup
    try:
        html = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    except:
        print("Page not found or No internet connection")
        sys.exit()
    
    soup = BeautifulSoup(html, 'html.parser')
    tags = (soup.find_all('body'))[0].find_all('script')
    
    s=(str(tags[0])[52:-10])
    
    pic_json=json.loads(s)
    
    profile_pic_url=pic_json["entry_data"]["ProfilePage"][0]["graphql"]["user"]["profile_pic_url_hd"]
    
    response = session.get(profile_pic_url, headers={'User-Agent': 'Mozilla/5.0'}).content
    img = Image.open(BytesIO(response))
    img.show()
    img.save("instagram_downloads/"+username+"_"+"profile_pic.jpg")
        