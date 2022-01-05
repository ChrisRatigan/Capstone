import scrapy
from time import sleep
#from bs4 import BeautifulSoup

class RawSpider(scrapy.Spider):
    name = "raw"
    allowed_domains=['cnn.com']
    start_urls = [
        'https://www.cnn.com/2021/12/01/entertainment/ben-affleck-jennifer-lopez/index.html',
        'https://www.cnn.com/2021/12/01/us/michigan-oxford-high-school-shooting-wednesday/index.html',
        'https://www.cnn.com/2021/12/01/health/us-omicron-variant-confirmed-case/',
        'https://www.cnn.com/politics/live-news/supreme-court-roe-v-wade-abortion-case-12-01-21/index.html',
        'https://www.cnn.com/world/live-news/omicron-covid-19-variant-12-01-21/h_6c81d8966c7e1f4c9bcceb6bb10cf1ad'
    ]
    #start_urls = [
    #    'http://quotes.toscrape.com/page/1/',
    #    'http://quotes.toscrape.com/page/2/',
    #]
    
    #/html/body/div/article/div/div/div/p/span/a
    #/html/body/div/div/div/article/div/div/div/div/div/p/a    
    
    def parse2(self, response):
        sleep(0.1)
        data = {
           'profile_picks' : ['https://www.cnn.com'+res for res in response.xpath('//h3[contains(@class, cd__head)]//a/@href').getall()],
        }
        
        for pick in data['profile_picks']:
            yield scrapy.Request(pick, callback=self.parse)

    def parse(self, response):
        sleep(0.1)
        data = {
            'author' : response.xpath('//p[contains(@class, "byline")]').getall(),
            #'author1' : response.xpath('/html/body/div/article/div/div/div/p/span/a').getall(),
            #'author2' : response.xpath('/html/body/div/div/div/article/div/div/div/div/div/p/a').getall(),
            'author3' : response.xpath('//p[contains(@data-type, "byline")]').getall(),
            'author4' : ' '.join(response.css('div.byline__names ::text').getall()),
            'author5' : ' '.join(response.css('div.Authors__writers ::text').getall()),
            
            'profile_url' : ['https://www.cnn.com'+res for res in response.xpath('//p[contains(@class, "byline")]//a/@href').getall()],
            'profile_url2' : ['https://www.cnn.com'+res for res in response.xpath('//div[contains(@class, "Authors")]//a/@href').getall()],
            
            'title' : response.css('h1.pg-headline').getall(),
            
            'profile_picks' : ['https://www.cnn.com'+res for res in response.xpath('//h3[contains(@class, cd__head)]//a/@href').getall()],
            
            'content1' : ' '.join(response.css('div.zn-body__paragraph ::text').getall()),
            #'content2' : ' '.join(response.css('p.sc-gZMcBi render-stellar-contentstyles__Paragraph-sc-9v7nwy-2 dCwndB ::text').getall()),
            'content3' : response.xpath('/html/body/div/div/div/article/div/div/div/article/div/p').getall(),
            'content4' : response.css('p.paragraph.inline-placeholder ::text').getall(),
            'url' : response.url
        }
   
        
        #authors = {
        #    'author1' : response.xpath('/html/body/div/article/div/div/div/p/span/a').getall(),
        #    'author2' : response.xpath('/html/body/div/div/div/article/div/div/div/div/div/p/a').getall()
        #}
            
        #content = {
            #'content1' : response.xpath('/html/body/div/article/div/div/div/div/section/div//text()').get()
            #'content2' : ''.join(response.css('div.l-container *::text').extract()) #.get()
            #'content' : ' '.join(response.css('div.zn-body__paragraph ::text').getall()),
            #'content2' : ' '.join(response.css('div.sc-bdVaJa.post-content-rendered.render-stellar-contentstyles__Content-sc-9v7nwy-0.erzhuK ::text').getall())
        #}
        #if(data['author']!=[]):
        #    print(data['profile_url'])
        #    print(" \n\n")
        
        #for key in list(data.keys()):
        #    if(data[key]=='' or data[key]==[]):
        #        del data[key]
        
        
        #print('new article \n\n')
            
        #print(content['content'])
        yield data
        
        #if('profile_picks' in data.keys()):
        #    for pick in data['profile_picks']:
        #        yield scrapy.Request(pick, callback=self.parse)
        
        #yield {
        #    'author' : response.xpath('/html/body/div/article/div/div/div/p/span/a').getall()
        #}
        if('profile_url' in data.keys()):
            for link in data['profile_url']:
                yield scrapy.Request(link, callback=self.parse2)
        
        if('profile_url2' in data.keys()):
            for link in data['profile_url2']:
                yield scrapy.Request(link, callback=self.parse2)
        
        if('content3' in data.keys()):
            next_pages = response.xpath('/html/body/div/div/div/article/div/div/div/article/div/p/a/@href').getall()
            for next_page in next_pages:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
#    def parse(self, response):
#        for quote in response.css('div.quote'):
#            yield {
#                'text': quote.css('span.text::text').get(),
#                'author': quote.css('small.author::text').get(),
#                'tags': quote.css('div.tags a.tag::text').getall(),
#            }