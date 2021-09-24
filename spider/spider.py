import requests

def spider(base_url,not_found_text=""):
    custom_404_page = False

    with open('common.txt','r') as wordlist:
        for w in wordlist:
            word = w[:-1]
            
            if base_url[-1] != '/': base_url += '/'  #append "/" to the end of the base url
            url = base_url + word

            r = requests.get(url)

            if not_found_text: custom_404_page = True
            
            if custom_404_page:
                if (not_found_text not in r.text) and (r.status_code == 200):
                        print('find this url, might be interesting:', url)
                        
            elif r.status_code == 200:
                print('find this url, might be interesting:', url)

