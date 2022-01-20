from src.scraping.waraitext import WaraiTextCrawler


def main():
    crawler = WaraiTextCrawler(
        start_index=1,
        neta_num=10000,
    )
    crawler.main()

if __name__=='__main__':
    main()
