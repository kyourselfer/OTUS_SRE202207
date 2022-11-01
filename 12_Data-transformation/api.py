import requests

def fetch(url, params):
    headers = params['headers']
    body = params['body']
    if params['method'] == 'GET':
        return requests.get(url, headers=headers)
    if params['method'] == 'POST':
        return requests.post(url, headers=headers, data=body)

r1 = fetch("http://api.open-notify.org/iss-now.json", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "upgrade-insecure-requests": "1",
    "cookie": "__utmc=254308054; __utmz=254308054.1664426565.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=254308054.96291170.1664426565.1664426565.1664452027.2"
  },
  "referrerPolicy": "strict-origin-when-cross-origin",
  "body": None,
  "method": "GET"
});

r2 = fetch("http://127.0.0.1:5000/", {
  "headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"106\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Linux\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "cookie": "grafana_sess=2e6d46db66a4d816; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19KUBRwowjrKjwhXjaT68pU24EMWeEc3sE%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX1%2BRhY%2FIU%2BWb7so5saD0dfKhwufkX6qqhZg%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX19B%2BKNkNYHSwOOy%2B2rJhn2UCCJvEGPI6AgJ0ZYvYnUgVfQP%2Bk3MVjKkgIKuCbqXwx4QwY%2BgfQ3bmg%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX18%2BiwWYkcehqsdG2eX2Id8Au3xy3VMGyPI%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B149fHpUDLNP%2Brb0LA7Znl%2BzGQXUjSO9Q%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX18xrwFyYSNrCvKLnxp7sAudMYmSuAiJzVhMIRCG6DbQdP5pttRJShAsPPLTWgyHFaPjn36OcqGjFGXTG6wHbzKIIwngyEOBiuZ7MCyxrteKjHmwjAxIttHBHneF4S4psv1XTXqwud1ajLE8jLcr4dijgit9yRgPgT0%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2FUEYraP7w6D2bpSSWkOJmKNsqWMSq1c0quWFP721voFJ14YIbJT5DftfhWZ05Wg4eSdFaanxMEW7ciZfK0ghIiyGG4VyZcp88RHOgz55wTNMLHFa8kDYboLPS5I7fSIyEle9G92vtMm77l9BlKiZ6w9FoRYvgiq%2F0%3D; rl_session=RudderEncrypt%3AU2FsdGVkX19ixVrFlfC%2FEf9ykW8QvOrRHCvdGLLR%2BWDubVCSle5WKuD8h5CladomR5KRKfIeyCnnvwChS%2FedcNIwWU6%2BvuSyXqhCwF0pA%2BPPuS28OU6Sa1X0j%2BYhnOSnwmBRFedJvG3yPSChch54lQ%3D%3D",
    "Referer": "http://127.0.0.1:5000/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  },
  "body": None,
  "method": "GET"
});

#r = requests.get("http://api.open-notify.org/iss-now.json")
print(r2.status_code)
print(r2.text)
r21 = r2.text
print(r2.json())

long1 = r1.json()["iss_position"]["longitude"] # Долгота
lang1 = r1.json()["iss_position"]["latitude"]   # Широта
print("lo:"+long1, "la:"+lang1)