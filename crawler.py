from icrawler.builtin import BingImageCrawler
name = "ηΈθιη΄"
crawler = BingImageCrawler(storage={"root_dir": name})
crawler.crawl(keyword=name, max_num=200)