from icrawler.builtin import BingImageCrawler
name = "相葉雅紀"
crawler = BingImageCrawler(storage={"root_dir": name})
crawler.crawl(keyword=name, max_num=200)