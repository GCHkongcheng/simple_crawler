"""
配置文件
"""

# 爬虫配置
CRAWLER_CONFIG = {
    'max_news': 50,
    'delay_min': 1,
    'delay_max': 3,
    'timeout': 10,
    'retry_times': 3
}

# 数据存储配置
DATA_CONFIG = {
    'csv_file': 'data/netease_financial_news.csv',
    'json_file': 'data/netease_financial_news.json',
    'summary_file': 'data/news_summary.csv'
}

# 请求头配置
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}