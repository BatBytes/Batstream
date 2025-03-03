import requests
def search_videos(query):
    return requests.get("https://f07b-34-48-161-231.ngrok-free.app/search?query="+query).json()
def get_serverdownload(vid):
    return requests.get("https://f07b-34-48-161-231.ngrok-free.app/get_video?vid="+vid).json()

#results = search_videos("العتاولة")
#print(results)
#print(get_serverdownload("5317f17f9"))
