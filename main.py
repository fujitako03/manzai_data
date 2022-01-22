import argparse

from src.scraping.waraitext import WaraiTextCrawler

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('start', metavar='start_index', type=int,
                    help='Start index (page url post-x)')
parser.add_argument('-n', '--num', default=1, metavar='neta_num', type=int,
                    help='Number of Neta to get.')
args = parser.parse_args()  

def main():
    crawler = WaraiTextCrawler(
        start_index=args.start,
        neta_num=args.num,
    )
    crawler.main()

if __name__=='__main__':
    main()
