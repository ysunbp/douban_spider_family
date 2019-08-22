from parse import parse_url
import json


class DoubanSpider:
    def __init__(self):
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_domestic/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288&_=1566267485795"

    def get_contentf_list(self, html_str):
        dict_data = json.loads(html_str)
        content_list = dict_data["subject_collection_items"]
        total = dict_data["total"]
        return content_list, total

    def save_content_list(self,content_list):
        with open("douban_chinese_series.json","a", encoding = "utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent = 2))
                f.write("\n")
        print("保存成功")

    def run(self):
#1. start_url
        num = 0
        total = 100
        while num<total+18:
            start_url = self.temp_url.format(num)
            #2. 发送请求获取响应
            print(start_url)
            html_str = parse_url(start_url)
            #3. 提取数据
            content_list, total = self.get_contentf_list(html_str)
            #4. 保存
            self.save_content_list(content_list)
            #5. 构造下一页，循环2至5步
            num += 18


if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()
