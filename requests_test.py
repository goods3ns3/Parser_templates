import requests
import lxml.html


HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
# LOGIN_DATA = {
#     'login_omen': '1',
#     'submiter': 'ok',
#     'login': 'genius',
#     'pass': '1111',
#     'ok': 'ok'
#     }
COOKIES = {'__cfduid': 'ddf4c248af1a698d8c3c97a06b291ca4a1617369679',
           'csrftoken': 'CKSECmDBT9bCzXxuHVCWnO6u7dN3FZBeRMLm7fbzkGMoZXUGfEMUmAg38amN2A33',
           '_ga': 'GA1.2.2127454017.1617369688',
           '_gid': 'GA1.2.1976664137.1617369688',
           'is_human': '1',
           'dwf_photo_stats_async': 'False',
           'dwf_use_comment_recaptcha': 'False',
           'sessionid': 'eyJ0ZXN0Y29va2llIjoid29ya2VkIn0:1lSL9s:HMCx6Kk9YogNpdic-nwpbMlymPM',
           'anonymous_user_id': 'c45ae181-a7cd-498e-a004-aede07c0506a',
           'client_width': '923'}
URL = 'https://pixabay.com/photos/search/'

with requests.Session() as s:
    try:
        responce = s.get(URL, headers=HEADERS, cookies=COOKIES)
        tree = lxml.html.document_fromstring(responce.text)
        result = tree.xpath('//*[@id="content"]/div/div[3]/div/h1/text()')
        print(result)
    except Exception as e:
        print(e)
