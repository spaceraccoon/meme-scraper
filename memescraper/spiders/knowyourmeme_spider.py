import scrapy


class KnowYourMemeSpider(scrapy.Spider):
    name = 'knowyourmeme'
    start_urls = ['http://sfbay.craigslist.org/search/npo']

    def start_requests(self):
        yield scrapy.Request(
            'https://knowyourmeme.com/memes/%s/photos/page/1' %self.meme
        )
        
    def parse(self, response):
        # Select fixed 200px width images
        image_urls = response.xpath('//div[@class="item"]//img/@data-src').extract()
        # image_urls = [i.replace('masonry', 'original') for i in image_urls]
        yield {
            'image_urls': response.xpath('//div[@class="item"]//img/@data-src').extract()
        }
        
        next_href = response.xpath(
            "//a[@class='next_page']/@href").extract_first()
        if next_href:
            yield scrapy.Request(response.urljoin(next_href))