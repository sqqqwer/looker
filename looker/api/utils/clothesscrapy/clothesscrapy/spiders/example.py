import scrapy


class LamodaSpider(scrapy.Spider):
    name = 'lamoda'
    allowed_domains = ['www.lamoda.ru']

    def __init__(self, url):
        self.start_urls = [url]

    def parse(self, response):
        item_info = response.xpath(
            '//script[@type="application/ld+json"]/text()')[-1].get()
        item_info_formated = item_info[4:-2]
        json_item_info = eval(item_info_formated)

        price = json_item_info['offers']['price']
        price = price[:price.find('.')]
        price = int(price)

        images = ' '.join(json_item_info['image'])

        yield {
            'price': price,
            'images': images
        }


class WildberriesSpider(scrapy.Spider):
    name = 'wildberries'
    allowed_domains = ['www.wildberries.ru']
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'card.wb.ru',
        'Origin': 'https://www.wildberries.ru',
        'Referer': '',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    item_id = ''

    def __init__(self, url):
        self.headers['Referer'] = url
        self.item_id = url[35:44]
        self.start_urls = [f'https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1785055&ab_testing=false&nm={self.item_id}']

    def request(self, url, callback):
        request = scrapy.Request(url=url, callback=callback,
                                 method='GET', headers=self.headers)
        return request

    def parse(self, response):
        clothes_item = response.json()['data']['products'][0]

        price = clothes_item['sizes'][0]['price']['product']

        images = ''
        photo_url = f'https://basket-15.wbbasket.ru/vol{self.item_id[:4]}/part{self.item_id[:6]}/{self.item_id}/images/c516x688/'
        number_of_pics = clothes_item['pics']
        for number in range(1, number_of_pics+1):
            images += photo_url + f'{number}.webp'
            if number != number_of_pics:
                images += ' '

        yield {
            'price': price,
            'images': images
        }
