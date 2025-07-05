"""
简化版运行脚本
"""
from netease_financial_crawler import NeteaseFinancialCrawler
from simple_analysis import analyze_news

def main():
    print("=== 网易财经新闻爬虫 ===")
    
    # 获取用户输入
    max_news = int(input("输入爬取数量 (默认20): ") or "20")
    
    # 爬取新闻
    crawler = NeteaseFinancialCrawler()
    news_data = crawler.crawl(max_news=max_news)
    
    if news_data:
        # 保存数据
        crawler.save_data(news_data)
        
        # 数据分析
        analyze_news()
        
        print("\n✅ 完成！数据保存在 data/ 目录")
    else:
        print("❌ 爬取失败")

if __name__ == "__main__":
    main()