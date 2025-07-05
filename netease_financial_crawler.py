import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
import random
import os
from datetime import datetime

class NeteaseFinancialCrawler:
    def __init__(self):
        self.base_url = "https://money.163.com/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def get_news_links(self):
        """获取新闻链接"""
        try:
            response = self.session.get(self.base_url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            news_list = []
            # 查找新闻链接
            for link in soup.find_all('a', href=True):
                href = link.get('href')
                title = link.get_text(strip=True)
                
                # 过滤财经新闻
                if href and title and len(title) > 10:
                    if 'money.163.com' in href or '/money/' in href:
                        full_url = href if href.startswith('http') else f"https://money.163.com{href}"
                        news_list.append({'title': title, 'url': full_url})
            
            return news_list[:20]  # 返回前20条
            
        except Exception as e:
            print(f"获取新闻链接失败: {e}")
            return []
    
    def get_news_content(self, url):
        """获取新闻内容"""
        try:
            response = self.session.get(url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 尝试多种选择器获取内容
            content_selectors = [
                'div.post_content_main',
                'div.post_body', 
                'div.content',
                'div.post_text'
            ]
            
            content = ""
            for selector in content_selectors:
                content_div = soup.select_one(selector)
                if content_div:
                    content = content_div.get_text(strip=True)
                    break
            
            return content
            
        except Exception as e:
            print(f"获取内容失败: {e}")
            return ""
    
    def crawl(self, max_news=20):
        """爬取新闻"""
        print("开始爬取网易财经新闻...")
        
        # 获取新闻链接
        news_links = self.get_news_links()
        if not news_links:
            print("未获取到新闻链接")
            return []
        
        print(f"获取到 {len(news_links)} 条新闻链接")
        
        news_data = []
        for i, news in enumerate(news_links[:max_news]):
            print(f"爬取第 {i+1} 条: {news['title'][:30]}...")
            
            content = self.get_news_content(news['url'])
            
            news_data.append({
                'title': news['title'],
                'url': news['url'],
                'content': content,
                'crawl_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
            # 随机延时
            time.sleep(random.uniform(1, 2))
        
        print(f"成功爬取 {len(news_data)} 条新闻")
        return news_data
    
    def save_data(self, news_data, csv_file='data/news.csv', json_file='data/news.json'):
        """保存数据"""
        if not news_data:
            print("没有数据需要保存")
            return
        
        # 创建目录
        os.makedirs('data', exist_ok=True)
        
        # 保存CSV
        df = pd.DataFrame(news_data)
        df.to_csv(csv_file, index=False, encoding='utf-8-sig')
        print(f"CSV数据已保存到 {csv_file}")
        
        # 保存JSON
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(news_data, f, ensure_ascii=False, indent=2)
        print(f"JSON数据已保存到 {json_file}")

def main():
    crawler = NeteaseFinancialCrawler()
    
    # 爬取新闻
    news_data = crawler.crawl(max_news=20)
    
    if news_data:
        # 保存数据
        crawler.save_data(news_data)
        
        # 显示统计
        print(f"\n=== 爬取统计 ===")
        print(f"总计: {len(news_data)} 条新闻")
        print(f"平均标题长度: {sum(len(n['title']) for n in news_data) / len(news_data):.1f} 字符")
        print(f"平均内容长度: {sum(len(n['content']) for n in news_data) / len(news_data):.1f} 字符")
    else:
        print("未获取到任何数据")

if __name__ == "__main__":
    main()