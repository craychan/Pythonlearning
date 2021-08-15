# import packages
import requests
import re
import time

#user Agent
userAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}

# fuction define <baidu news dig with data clean and format>
def baidu(company):
    url = 'https://www.baidu.com/s? tn=news&rtt=4&bsst=1&cl=2&wd=' + company
    res = requests.get(url, headers = userAgent).text

# Regular Express filter
    p_href = '<h3 class="news-title_1YtI1">.*?<a href="(.*?)"'
    p_title = '<h3 class="news-title_1YtI1">.*?>(.*?)</a>'
    p_info = '<div class="news-source_Xj4Dv">.*?>(.*?)</div>'

    # Filter
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    info = re.findall(p_info, res, re.S)

    source = []
    # date = []

    for i in range(len(title)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])
        info[i] = re.sub('<.*?>', '', info[i])

        source.append(info[i])
        source[i] = source[i].strip()
        source[i] = re.sub('\s', '', source[i])

    file1 = open("C:/Users/Raymond/Desktop/Data_Dig_Report.txt", "a")
    file1.write(company + ' Data Digging Completed!' + '\n' + '\n')

    for i in range(len(title)):
        file1.write(str(i+1) + '.' + title[i] + '(' + source[i] + ')' + '\n')
        file1.write(href[i] + '\n')

    file1.write('- - - - - - - - - - - - - - - - ' + '\n' + '\n')
    file1.close()
# Continue to dig news by call function baidu()
print("Please input second for period digging: ")
t = input()
t = int(t)
while True:
    companys = ['华能信托', '阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
    for i in companys:
        try:
            baidu(i)
            print(i + '百度新闻爬取成功')
        except:
            print(i + '百度新闻爬取失败')
    print('-------------------------------百度新闻爬取结束------------------------------------------')
    time.sleep(t)

if __name__ == '__main__':
    main()

