import scrapy

class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    start_urls = ['https://ca.indeed.com/jobs?q=legal%20clerk&l=Toronto%2C%20ON&vjk=e142ac760f26f301'] #Update this ONLY

    def parse(self, response):
        jobs = response.css('div.slider_container')                         #Parse job names, locations, employers and link
        jobLinkCollection = response.css('div.mosaic-zone')
        jobsList = jobs.css('h2.jobTitle')
        allJobNames = jobsList.css('span::text').getall()
        parsedNames = [value for value in allJobNames if value != 'new']
        parsedLocations = jobs.css('div.companyLocation::text').getall()
        parsedCompany = jobs.css('span.companyName::text').getall()

        parsedLinks = []
        for link in jobLinkCollection.css('a.tapItem'):
            parsedLinks.append("https://ca.indeed.com"+link.attrib['href'])
        
        i = 0
        while (i < len(parsedNames)):
            yield{
                'Name': parsedNames[i],
                'Employer': parsedCompany[i],
                'Location': parsedLocations [i],
                'Link': parsedLinks[i]
            }
            i = i + 1

        nextLocation = response.css('div.pagination')
        nextLink = "https://ca.indeed.com"+nextLocation.css('a').attrib['href']         #Find next page and run
        if nextLink is not None:
            yield response.follow(nextLink, callback=self.parse)

