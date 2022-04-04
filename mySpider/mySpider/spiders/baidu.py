import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        filename = "news.html"
        open(filename, 'wb').write(response.body)
        # open("news.html","wb").write(response.body).close()

        # 存放老师信息的集合
        #items = []
        # print("====="+response.body)

        # for each in response.xpath("//div[@class='li_txt']"):
        #     # 将我们得到的数据封装到一个 `ItcastItem` 对象
        #     item = ItcastItem()
        #     # extract()方法返回的都是unicode字符串
        #     name = each.xpath("h3/text()").extract()
        #     title = each.xpath("h4/text()").extract()
        #     info = each.xpath("p/text()").extract()
        #
        #     # xpath返回的是包含一个元素的列表
        #     item['name'] = name[0]
        #     item['title'] = title[0]
        #     item['info'] = info[0]
        #
        #     items.append(item)

        # 直接返回最后数据
        #return items
