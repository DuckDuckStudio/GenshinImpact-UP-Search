# GUS，一个根据原神 UID 搜索对应 UP 主的小工具
[![Github LICENSE](https://img.shields.io/github/license/DuckDuckStudio/GenshinImpact-UP-Search)]() ![GitHub issues](https://img.shields.io/github/issues/DuckDuckStudio/GenshinImpact-UP-Search)  
目前实现方法为直接列出对应表格，故可能存在错误或缺漏，如有发现错误请提交 Issues。  
如果你想将自己加入到表格中，则可以提交 PR 或者 Issues。  
如果你想优化搜索程序，请提交 PR 。  

## 如何使用
1. 克隆仓库到本地  
   ```bash
   git clone https://github.com/DuckDuckStudio/GenshinImpact-UP-Search.git
   ```
2. 安装依赖
   ```bash
   pip install -r requirements.txt
   REM 需求生成by芙芙工具箱-开发工具
   ```
3. 运行`Search.py`
   ```python
   python Search.py
   ```
4. 查询你需要查询的内容

完整指令(先`cd`到所需目录):  
```bash
git clone https://github.com/DuckDuckStudio/GenshinImpact-UP-Search.git
cd GenshinImpact-UP-Search
pip install -r requirements.txt
python Search.py
```

如需更新表格请执行以下命令:  
```bash
git pull
```
PS:每次运行程序都会尝试自动运行该命令。  

## 表格说明
由于表格项众多，可能会有过时信息(例如UP改名等)，故所有查出来的对应UP的结果**以UP的ID为准**，你可以对过时的信息进行修改后PR。  

## 特别感谢
*更新可能会有延后，如果没有列出请稍后再来查看。*  
感谢所有为该项目做出贡献的人！  

[![贡献者](https://contrib.rocks/image?repo=DuckDuckStudio/GenshinImpact-UP-Search)](https://github.com/DuckDuckStudio/GenshinImpact-UP-Search/graphs/contributors)

### Stargazers
[![Stargazers](https://reporoster.com/stars/DuckDuckStudio/GenshinImpact-UP-Search)](https://github.com/DuckDuckStudio/GenshinImpact-UP-Search/stargazers)

## 状态
![Alt](https://repobeats.axiom.co/api/embed/aafa6967371b8625e9bb84f7ec3e31abc601f67a.svg "Repobeats analytics image")  