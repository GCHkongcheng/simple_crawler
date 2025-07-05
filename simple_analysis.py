import pandas as pd
import jieba
from collections import Counter

def analyze_news(csv_file='data/news.csv'):
    """简单的新闻分析"""
    try:
        df = pd.read_csv(csv_file, encoding='utf-8-sig')
        
        print("=== 数据分析 ===")
        print(f"新闻总数: {len(df)}")
        print(f"平均标题长度: {df['title'].str.len().mean():.1f}")
        print(f"平均内容长度: {df['content'].str.len().mean():.1f}")
        
        # 关键词分析
        all_titles = ' '.join(df['title'].tolist())
        words = jieba.lcut(all_titles)
        
        # 过滤停用词
        stop_words = {'的', '了', '在', '是', '与', '和', '有', '为', '将', '已', '等', '中', '上', '下'}
        filtered_words = [w for w in words if len(w) > 1 and w not in stop_words]
        
        print("\n热门关键词:")
        word_count = Counter(filtered_words)
        for word, count in word_count.most_common(10):
            print(f"{word}: {count}")
            
    except Exception as e:
        print(f"分析失败: {e}")

if __name__ == "__main__":
    analyze_news()