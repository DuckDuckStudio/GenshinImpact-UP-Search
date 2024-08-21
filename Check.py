import re
import sys
from colorama import init, Fore

init(autoreset=True)  # 初始化 Colorama，使颜色输出生效

def check_markdown_table(filename):
    err_flag = 0
    try:
        # 读取Markdown文件中的所有行
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 定义三个集合，用于检查重复项
        uid_set = set()  # 用于存储UID值
        id_set = set()  # 用于存储ID值
        up_set = set() # 用于存储UP值
        uid_up_id_set = set()  # 用于存储UID、UP和ID组成的元组

        # 遍历每一行并进行检查
        for line_num, line in enumerate(lines[2:], start=3):  # 从第三行开始遍历
            fields = line.strip().split('|')
            uid = fields[1].strip()
            up = fields[2].strip()
            id = fields[3].strip()

            # 检查是否缺少UID、UP或ID中的任何一个值
            if not uid:
                print(f"{Fore.RED}异常项：缺少UID值（位于第 {line_num} 行）")
                err_flag = 1
            if not up:
                print(f"{Fore.RED}异常项：缺少UP值（位于第 {line_num} 行）")
                err_flag = 1
            if not id:
                print(f"{Fore.RED}异常项：缺少ID值（位于第 {line_num} 行）")
                err_flag = 1
            if not uid or not up or not id:
                continue  # 如果缺少任何一个值，直接跳过后续的格式检查

            # 检查是否存在完全重复的组合
            uid_up_tuple = (uid, up, id)
            if uid_up_tuple in uid_up_id_set:
                print(f"{Fore.BLUE}重复项：UID、UP和ID均相同 - {uid_up_tuple}（位于第 {line_num} 行）")
                err_flag = 2
                flag = 1
            else:
                uid_up_id_set.add(uid_up_tuple)

            # 检查重复的UID
            if uid in uid_set:
                # 如果没有完全重复
                if flag != 1:
                    print(f"{Fore.YELLOW}异常项：UID相同但其他值不同 - {uid_up_tuple}（位于第 {line_num} 行）")
                    err_flag = 1

            # 检查UID的格式是否正确
            if not re.match(r'^\d{9}$', uid):
                print(f"{Fore.RED}异常项：UID格式不正确 - {uid}（位于第 {line_num} 行）")
                err_flag = 1
            else:
                uid_set.add(uid)

            # 检查ID的格式是否正确
            if not id.isdigit():
                print(f"{Fore.RED}异常项：ID格式不正确 - {id}（位于第 {line_num} 行）")
                err_flag = 1
            else:
                id_set.add(id)

            flag = 0

        # 输出检查结果
        print(f"{Fore.GREEN}检查完成！")
        return err_flag
    except IndexError as e:
        print(f"{Fore.RED}错误: 索引错误: {e}\n请检查是否有多余空行。")
        err_flag = 3
        return err_flag

if __name__ == "__main__":
    filename = "Search-table.md"
    sys.exit(check_markdown_table(filename))
