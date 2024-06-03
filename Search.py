import re
import sys
import os

from colorama import init, Fore

init(autoreset=True)  # 初始化 Colorama，使颜色输出生效

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
try:
    os.sys("git pull")
except:
    pass
# 自动拉取更新

def search_table(query_type, query, md_table):
    # 将Markdown表格转换为二维列表
    table = [re.split(r'\s*\|\s*', row.strip()) for row in md_table.split('\n') if row.strip()]
    headers = table[0]
    # 确定要搜索的列
    if query_type.lower() == 'uid':
        search_col = 1
    elif query_type.lower() == 'up':
        search_col = 2
    elif query_type.lower() == 'id':
        search_col = 3
    else:
        return None

    # 进行搜索
    result = []
    for row in table[2:]:
        if search_col == 1:
            try:
                if int(row[search_col]) == int(query):
                    result.append(row)
            except ValueError:
                pass
        elif row[search_col].lower() == query.lower():
            result.append(row)

    # 格式化输出结果
    if result:
        output = []
        for row in result:
            output.append(Fore.GREEN + f'UID:{row[1]} UP名:{row[2]} b站ID:{row[3]}')
        return '\n'.join(output)
    else:
        return Fore.RED + f'未找到有关{query}的信息。'


# 从文件中读取Markdown表格
def read_md_table(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        md_table = f.read()
    return md_table


# 确认输入是否有效
def is_valid_query_type(query_type):
    return query_type.lower() in ['uid', 'up', 'id']


# ---定义函数 ↑ | ↓ 主程序---


# 用户输入搜索对象并进行验证
while True:
    query_type = input('请输入搜索对象（UID、UP、ID）：')
    if is_valid_query_type(query_type):
        break
    else:
        print(Fore.RED + '无效的搜索对象，请重新输入。')

# 用户输入搜索内容
query = input('请输入搜索内容：')

# 读取Markdown表格
file_path = 'Search-table.md'
md_table = read_md_table(file_path)

# 进行搜索并输出结果
result = search_table(query_type, query, md_table)
if result:
    print(result)
else:
    print(Fore.RED + 'f未找到有关{query}的信息。')

# 等待用户结束程序
input("按Enter键退出程序...")
