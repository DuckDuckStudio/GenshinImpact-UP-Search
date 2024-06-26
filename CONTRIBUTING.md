# GUS贡献文档
你可以通过 [提交Issues](https://github.com/DuckDuckStudio/GenshinImpact-UP-Search/issues) 、 [提交PR](https://github.com/DuckDuckStudio/GenshinImpact-UP-Search/pulls) 等方式贡献本工具。  
提交前请先查阅表格中是否已有该UP的账号，或者在Issues或PR中存在关于该UP的信息，如有，则可在对应 Issues或PR 下评论修改。如果表格中的信息不全且没有相关Issues/PR，则可以自己创建一个Issues/PR。  
如为一个UP多个账号，请将他们放在一起！  

> [!NOTE]
> 请确保对应信息正确再提交修改！！！不要看到UID就认为这就是那个UP的账号，多看几个相关视频！  

## 关于优化搜索程序
你可以在 Issues 中说明你希望实现的效果，或者直接修改后 PR 。  

## 关于添加表格
你可以直接将内容填入`Search-table.md`文件中，然后 PR 。  
也可以提交 Issues ，当然直接改比较简单，~~还能占个贡献者的位置。~~  
也欢迎各位将自己的UID以及对应UP账号提交上来哦，即使没什么人看。  

### 关于收录对应账号的要求
至少发布过 1 个有关自己账号的视频。  
没有频繁切换账号。  
非国际服账号。  

## 关于错误的数据
如果你发现查到的数据有误，请提交 Issues 或直接 PR 修改。  

# 如何自查错误
你可以运行仓库中的`Check.py`来确定是否存在重复项或异常项。  
其中，以下为重复项:  
- 与其他项完全一致的项

以下为异常项:  
- 缺少任意一值的项
- `UID`值相同但其他值不同的项
- `UID`或`ID`格式不正确的项

# 各个文件的作用
- `CONTRIBUTING.md` → 贡献文档
- `README.md` → 展示文件
- `Search-table.md` → 数据表格
- `Search.py` → 查询程序
- `LICENSE` → GPL-3许可证
- `Check.py` → 表格检查
