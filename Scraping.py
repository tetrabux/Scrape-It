import time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

while (1 == 1):

    news_url = "https://timesofindia.indiatimes.com/news"

    uClient = uReq(news_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, 'html.parser')

    containers = page_soup.findAll('span', {'class': 'w_tle'})
    # print(len(containers))

    # print(soup.prettify(containers[0]))

    container = containers[0]
    link = (container.find('a')).get('href')
    nlink = 'https://timesofindia.indiatimes.com' + link
    # print(container.a.text,'\n')
    # print(nlink,'\n\n')

    fileName = 'news2.html'
    f = open(fileName, 'w')
    headers = 'NEWS,Link\n'

    f.write('<html>\n<head> <meta http-equiv="refresh" content="10" /> </head>\n<body>\n')

    for container in containers[20:]:
        News = container.a.text
        Link = 'https://timesofindia.indiatimes.com' + (container.find('a')).get('href')

        # print ("NEWS " + News + '\n')
        # print ("Link to this is " + Link + '\n\n')

        print('<h1>\n\t<a href="' + Link + ' "> ' + News + '</a> \n</h1>\n\n')
        f.write('<h3>\n\t<a href="' + Link + '">' + News + '</a> \n</h3>\n\n')

    f.write('\n\t</body>\n</html>')
    f.close()
    time.sleep(300)