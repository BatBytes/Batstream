# Coded BY -> t.me/BatByte .
import requests,re
from bs4 import BeautifulSoup
import base64
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
###----->>> <<<-----###

def search_videos(query):
    url = "https://ser.brstej.com/search.php"
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }
    params = {'keywords': query}
    
    all_videos = []
    page = 1
    
    while True:
        params['page'] = page
        response = requests.get(url, params=params, headers=headers, verify=False)
        soup = BeautifulSoup(response.text, "html.parser")

        videos = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3")
        if not videos:
            break 
        
        for video in videos:
            #print(video)
            title_tag = video.find("h3").find("a")
            title = title_tag.text.strip() if title_tag else None
            vid = title_tag["href"].split("vid=")[1] if title_tag else None
            image = re.findall('src="(.*?)" ',str(video))[0].split("?")[0]
            all_videos.append({
                "title": title,
                "vid": vid,
                "image": image
            })
        
        next_page = soup.find("a", href=True, string=str(page + 1))
        if next_page:
            page += 1
        else:
            break
    if len(all_videos) == 0:
        return {"success":False,"result":all_videos,"By":"t.me/BatByte"}
    return {"success":True,"result":all_videos,"By":"t.me/BatByte"}

def get_serverdownload(vid):
    url = "https://ser.brstej.com/play.php?vid="+vid

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://ser.brstej.com/watch.php?vid='+vid,
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(url, headers=headers, verify=False)
    
    if response.status_code != 200:
        return {"success":False,"result":[],"By":"t.me/BatByte"}
    soup = BeautifulSoup(response.text, "html.parser")
    return {"success":True,"result":[btn.get("data-embed-url") for btn in soup.find_all("button", class_="watchButton") if btn.get("data-embed-url")],"By":"t.me/BatByte"}


#results = search_videos("العتاولة")
#print(results)
#print(get_serverdownload("4fd4c705c"))
