import json,requests
from fake_useragent import UserAgent

def getIdFromUrl(url):
    return(requests.get(url).text.split('[{"pageID":"')[1].split('"')[0])
def getFacebookPageFromName(name):
    cookies = {
        'wd': '1920x1080',
    }
    ua = UserAgent(use_cache_server=False,verify_ssl=False)
    headers = {
        'User-Agent': ua.firefox,
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://www.facebook.com/ads/library/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.facebook.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'TE': 'Trailers',
    }

    params = (
        ('ad_type', 'all'),
        ('country', ''),
        ('is_mobile', 'false'),
        ('q', name),
        ('session_id', '""'),
    )


    data = {
      '__user': '0',
      '__a': '1',
      '__dyn': '""',
      '__csr': '',
      '__req': '1',
      '__beoa': '0',
      '__pc': 'PHASED:DEFAULT',
      'dpr': '1',
      '__ccg': 'UNKNOWN',
      '__rev': '""',
      '__s': '""',
      '__hsi': '""',
      '__comet_req': '0',
      'lsd': '""',
      'jazoest': '""',
      '__spin_r': '""',
      '__spin_b': 'trunk',
      '__spin_t': '""'
    }

    response = requests.post('https://www.facebook.com/ads/library/async/search_typeahead/', headers=headers, params=params, cookies=cookies, data=data)
    data = json.loads(response.text.replace("for (;;);",""))["payload"]["pageResults"]
    return(data)
def getAdsFromId(id):
    cookies = {
        'wd': '1920x1080',
    }
    ua = UserAgent(use_cache_server=False,verify_ssl=False)

    headers = {
        'User-Agent': ua.firefox,
        'Accept': '*/*',
        'Accept-Language': 'en,en-US;q=0.5',
        'Referer': 'https://www.facebook.com/ads/library/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.facebook.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
    }


    data = {
      '__user': '0',
      '__a': '1',
      '__dyn': '""',
      '__csr': '',
      '__req': '1',
      '__beoa': '0',
      '__pc': 'PHASED:DEFAULT',
      'dpr': '1',
      '__ccg': 'UNKNOWN',
      '__rev': '""',
      '__s': '""',
      '__hsi': '""',
      '__comet_req': '0',
      'lsd': '""',
      'jazoest': '""',
      '__spin_r': '""',
      '__spin_b': 'trunk',
      '__spin_t': '""'
    }



    params = (
        ('session_id', '""'),
        ('count', '30'),
        ('active_status', 'all'),
        ('ad_type', 'all'),
        ('countries[0]', 'ALL'),
        ('impression_search_field', 'has_impressions_lifetime'),
        ('view_all_page_id', id),
        ('sort_data[direction]', 'desc'),
        ('sort_data[mode]', 'relevancy_monthly_grouped'),
    )

    response = requests.post('https://www.facebook.com/ads/library/async/search_ads/', headers=headers, params=params, cookies=cookies, data=data)
    data = json.loads(response.text.replace("for (;;);",""))
    result = []
    if data["payload"]["results"]!=[]:
        for res in data["payload"]["results"]:
            for re in res:
                result.append(re)
        return(result)
    else:
        return([])
