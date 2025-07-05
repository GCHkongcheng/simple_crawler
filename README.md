# 网易财经新闻爬虫

这是一个用于爬取网易财经新闻的 Python 爬虫程序。

## 功能特点

- 爬取网易财经主页的最新新闻
- 获取新闻标题、链接、内容
- 支持 CSV 和 JSON 格式数据导出
- 包含数据分析和关键词提取功能
- 防反爬机制，随机延时

## 项目结构

```
crawler2/
├── netease_financial_crawler.py  # 主爬虫程序
├── simple_analysis.py            # 数据分析模块
├── run_crawler.py                # 运行脚本
├── requirements.txt              # 依赖包
├── README.md                     # 说明文档
└── data/                         # 数据存储目录
    ├── news.csv                  # 新闻数据CSV文件
    └── news.json                 # 新闻数据JSON文件
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 1. 运行爬虫（推荐）

```bash
python run_crawler.py
```

### 2. 单独运行爬虫

```bash
python netease_financial_crawler.py
```

### 3. 单独运行数据分析

```bash
python simple_analysis.py
```

## 输出数据

### CSV 格式 (data/news.csv)

包含以下字段：

- title: 新闻标题
- url: 新闻链接
- content: 新闻内容
- crawl_time: 爬取时间

### JSON 格式 (data/news.json)

相同的数据结构，JSON 格式存储

## 数据分析功能

- 新闻数量统计
- 平均标题长度
- 平均内容长度
- 热门关键词提取（基于 jieba 分词）

## 注意事项

1. 请遵守网站的 robots.txt 协议
2. 避免频繁请求，程序已设置随机延时
3. 如遇反爬限制，可能需要调整请求策略
4. 建议在法律允许的范围内使用
5. 确保网络连接稳定

## 常见问题

### Q: 如何修改爬取数量？

A: 运行 `python run_crawler.py` 时会提示输入数量，或直接修改代码中的 `max_news` 参数。

### Q: 爬取失败怎么办？

A: 检查网络连接，或尝试减少爬取数量。网易财经可能有反爬机制。

### Q: 如何查看爬取结果？

A: 数据保存在 `data/` 目录下，可以用 Excel 打开 CSV 文件查看。

## 版本历史

- v1.0: 基础爬虫功能
- v1.1: 添加数据分析功能
- v1.2: 简化代码结构，优化性能
