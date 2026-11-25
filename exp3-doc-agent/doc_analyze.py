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

    # 输出文本汇总报告 report.txt
    with open("report.txt", "w", encoding="utf-8") as fw:
        fw.write("=====文档分析Top50高频词报告=====\n")
        if top_50_words:
            for word, count in top_50_words:
                fw.write(f"{word} : {count}\n")
        else:
            fw.write("未获取到有效高频词\n")

    # 4.生成词云，微软雅黑msyh.ttf
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
    # Windows微软雅黑字体
    font = r'C:\Windows\Fonts\msyh.ttc'
    analyze_documents(
        folder_path="./docs",
        font_path=font,
        stopwords_file="stopwords.txt",
        user_dict="user_dict.txt"
    )
