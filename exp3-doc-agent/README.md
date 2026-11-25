```
# 本地文档智能审查与摘要Agent 实验报告

## 一、实验目的

1. 掌握Python批量文件读取与文本预处理的方法。
2. 熟练运用jieba库完成中文分词、停用词过滤、加载自定义专业词典。
3. 掌握wordcloud库参数配置，生成具有业务意义的词云可视化图像。
4. 体验Vibe Coding工作流，学会编写结构化Prompt引导AI完成代码架构设计与实现。

## 二、实验环境

- Python版本：3.11.9（≥3.8）
- 依赖库：jieba、wordcloud、matplotlib、numpy、pillow
- 开发工具：PyCharm
- 部署平台：GitHub + GitHub Pages

环境安装命令：

```bash
pip install jieba wordcloud matplotlib numpy pillow
```

## 三、实验需求边界（Vibe‑Coding 准备）

输入：存放多个 txt/md 文档的文件夹路径、停用词表、自定义专业词典。

处理流程：批量读取文件 → 文本清洗 → 加载自定义词典 → jieba 精确模式分词 → 过滤停用词与单字符词汇 → 统计词频。

输出：Top50 高频词词云 PNG 图片；保存关键词汇总报告 report.txt。

~~~~约束：增加异常处理，捕获文件不存在、编码错误；配置中文字体，解决中文方框乱码。

## 四、结构化 Prompt（Vibe Coding 使用）

> 
> 将下面 Prompt 交给 AI，用来生成项目基础代码框架

```
需求背景：我需要开发一个本地文档分析工具，用于批量处理文件夹中的文本文件，提取高频词并生成词云。
明确约束:
1. 使用os遍历指定目录下的所有.txt 文件。
2. 使用jieba进行分词，要求支持加载自定义词典user_dict.txt 和停用词表 stopwords.txt。
3. 使用wordcloud生成词云，需指定中文字体路径font_path='msyh.ttc'，背景色为白色，尺寸为1000x800。
4. 代码需包含详细的注释，并处理可能的文件读取异常。
输出要求:请提供完整的Python代码，并简要说明如何配置停用词表和自定义词典。
```

## 五、项目文件结构

```
python实验‑本地文档智能审查与摘要
├─ doc_analyze.py        # 主程序
├─ docs/                 # 待分析文本目录
│  └─ test1.txt
├─ stopwords.txt         # 停用词表，UTF‑8编码，一行一个词
├─ user_dict.txt         # jieba自定义专业词典
├─ report.txt            # 输出：Top50词频汇总报告
├─ document_wordcloud.png# 输出：词云可视化图片
└─ README.md             # 本实验报告
```

## 六、完整核心代码

```
import os
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def analyze_documents(folder_path, font_path, stopwords_file=None, user_dict=None):
    # 1.加载自定义词典
    if user_dict and os.path.exists(user_dict):
        jieba.load_userdict(user_dict)

    # 加载停用词
    stopwords = set()
    if stopwords_file and os.path.exists(stopwords_file):
        with open(stopwords_file, 'r', encoding='utf-8') as f:
            stopwords = set([line.strip() for line in f])
    else:
        stopwords = {"的", "了", "和", "在", "是", "我", "你", "他", "我们", "他们",
                     "为", "以", "等", "并", "对", "与"}

    all_words = []
    # 2.批量读取文件夹txt文档
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                words = jieba.lcut(text)
                filtered_words = [w for w in words if len(w) > 1 and w not in stopwords]
                all_words.extend(filtered_words)
                print(f"成功处理文件: {filename}")
            except Exception as e:
                print(f"处理文件{filename} 时发生错误: {e}")

    if not all_words:
        print("未提取到有效词汇，请检查文件路径或内容。")
        return

    # 3.统计词频，取Top50
    word_counts = Counter(all_words)
    top_50_words = word_counts.most_common(50)
    print(f"\nTop 50 高频词：\n{top_50_words}")

    # 输出文本汇总报告
    with open("report.txt", "w", encoding="utf-8") as fw:
        fw.write("=====文档分析Top50高频词报告=====\n")
        if top_50_words:
            for word, count in top_50_words:
                fw.write(f"{word} : {count}\n")
        else:
            fw.write("未获取到有效高频词\n")

    # 4.生成词云
    wordcloud = WordCloud(
        font_path=font_path,
        width=1000,
        height=800,
        background_color='white',
        max_words=50,
        collocations=False
    )
    wordcloud.generate_from_frequencies(dict(top_50_words))

    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("本地文档高频词云分析")
    plt.show()

    output_image = "document_wordcloud.png"
    wordcloud.to_file(output_image)
    print(f"\n词云图片已保存至: {output_image}")

if __name__ == '__main__':
    # Windows微软雅黑字体路径
    font = r'C:\Windows\Fonts\msyh.ttc'
    analyze_documents(
        folder_path="./docs",
        font_path=font,
        stopwords_file="stopwords.txt",
        user_dict="user_dict.txt"
    )
```

## 七、实验运行结果

1. 控制台输出：打印处理的文件名，输出 Top50 高频词列表；
2. 程序自动生成`report.txt`，保存全部词频统计；
3. 输出`document_wordcloud.png`词云可视化图片。

词云效果图：![document_wordcloud.png](document_wordcloud.png)

## 八、实验注意事项

1. wordcloud 中文乱码方框：必须指定 Windows 系统中文字体`msyh.ttc`；
2. stopwords.txt、user_dict.txt 保存编码必须为 UTF‑8，每行存放一个词语；
3. Vibe Coding 开发技巧：不要一次性写全部需求，分模块调试：文件读取 → 分词统计 → 词云生成。

## 九、Agent 进阶拓展方向

1. 蒙特卡洛模拟：针对文档不确定性指标编写模拟脚本，做概率分布预测；
2. 对接大模型 API：将 Top50 关键词送入大模型，自动生成文档审查意见与摘要；
3. watchdog 监控文件夹：新增文档自动执行整套分析，实现无人值守智能 Agent。

## 十、实验总结

本次实验完成本地文档智能审查 Agent 原型。实现批量读取文本、jieba 分词、停用词过滤、词频统计、词云可视化。掌握 Vibe Coding 开发模式，通过结构化 Prompt 辅助 AI 编码，实现异常捕获。最后通过 GitHub Pages，将实验报告发布成网页用于作业提交。
