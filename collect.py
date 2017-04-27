import requests, os, random, time

keywords = ['angry', 'disgust', 'fear', 'sad', 'happy',
            'surprise', 'contempt', 'neutral']
header = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
for keyword in keywords[5:]:
    url = 'https://www.google.com.hk/search?q=%s+%s+face&' \
          'newwindow=1&safe=strict&rlz=1C1CHZL_zh-CN__685__686&' \
          'tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwiigNKv877TAhUMzbwKHec8ATMQsAQIJA&' \
          'biw=1366&bih=662' % (keyword, 'human')
    h = requests.get(url, headers=header)
    text = h.text
    h.close()
    maxpos = len(text)
    start = text.index('"ou"')
    print(keyword)
    pos = start
    cnt = 0
    if not os.path.exists('data_collect/' + keyword):
        os.mkdir('data_collect/' + keyword)
    while (pos < maxpos and text[pos:].__contains__('"ou":') and cnt <= 80):
        pos = text.index('"ou":', pos)
        print(pos)
        endpos = text.index('"', pos + 6)
        picurl = text[pos + 6:endpos]
        pos += 1
        print(picurl)
        time.sleep(5 * random.random())
        # pich = requests.get(picurl, headers=header, timeout=100)
        try:
            pich = requests.get(picurl, headers=header, timeout=(1, None))
            print('writing...')
            f = open('data_collect/' + keyword + '/pic%d.png' % cnt, 'wb')
            f.write(pich.content)
            f.close()
            pich.close()
            cnt += 1
        except:
            continue

