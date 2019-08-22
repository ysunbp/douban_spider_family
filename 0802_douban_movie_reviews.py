import requests
from retrying import retry


headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Mobile Safari/537.36",
           "Cookie":"bid=TOQcHwbMexI; ll=\"108231\"; _vwo_uuid_v2=DCF642A100F25F6AFBCF4D19B655F48A1|1ca42987b26c2325dcb7ba2da05ef826; trc_cookie_storage=taboola%2520global%253Auser-id%3Dc606c342-5801-4f95-a0fe-6b16854fa28a-tuct42332c2; __utmz=223695111.1564296660.10.10.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __yadk_uid=1KQTtyJx8qNsukyQsKaVR79AQvWKfxk5; UM_distinctid=16ca93945966db-00717973be5828-70286132-3d220-16ca9394597245; _ga=GA1.2.1519956688.1560744787; _gid=GA1.2.373411040.1566207199; Hm_lvt_19fc7b106453f97b6a84d64302f21a04=1566207199; __utmc=30149280; __utmz=30149280.1566263764.14.14.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1566267917%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Ds18nFa01fzPFTNrPUY-gCdgXsZTyY74SiTP5FjYzclYQ4ilQZzXHofy1r26oGU4g%26wd%3D%26eqid%3De0d570900014ebd5000000065d3d45cd%22%5D; _pk_id.100001.4cf6=8fb0636019530680.1562167073.11.1566267917.1564296785.; _pk_ses.100001.4cf6=*; __utma=30149280.1519956688.1560744787.1566263764.1566267917.15; __utmb=30149280.0.10.1566267917; __utma=223695111.6871686.1562167073.1564296660.1566267917.11; __utmb=223695111.0.10.1566267917; __utmc=223695111; ap_v=0,6.0"}
url = "https://movie.douban.com/review/best/?start="

@retry(stop_max_attempt_number = 3)
def parse_url(url):
    print("*"*100)
    response = requests.get(url, headers = headers)
    return response.content.decode()

page = 0
while page < 10:
    url = url + str(page * 20)
    with open ("douban_movie_reviews", "a", encoding = "utf-8")as f:
        f.write(parse_url(url))
    page += 1


