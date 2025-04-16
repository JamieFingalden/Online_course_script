结构思考力课程自动化刷课工具

自动化刷课工具，十分钟内完成课程学习进度！


项目介绍

这是一个专为结构思考力课程设计的自动化刷课工具。通过模拟用户操作，快速完成课程学习进度，节省宝贵时间。


使用方法


1.安装依赖

在命令行中运行以下命令安装所需的依赖库：


```bash
pip install selenium webdriver-manager
```



2.运行脚本

运行脚本：


```bash
python Online_course_script.py
```



3.输入学号和学习进度

按照提示输入以下信息：


• 十位数学号：输入你的完整学号。

• 当前学习进度：输入你当前的学习进度（从 1 开始）。


4.打包成可执行文件

将脚本打包成`.exe`文件：


```bash
pip install pyinstaller
pyinstaller --onefile --noconsole Online_course_script.py
```


打包完成后，生成的`.exe`文件会位于项目目录下的`dist`文件夹中。


运行环境


• 浏览器：务必使用谷歌浏览器（Chrome）。

• Python版本：3.6 或更高版本。

• 依赖库：

• selenium

• webdriver-manager

• pyinstaller


常见问题


运行失败

如果运行时遇到问题，请按照以下步骤解决：


1. 进入[getWebDriver]()下载与自己谷歌浏览器对应的版本驱动。

2. 将下载的驱动文件放在`.py`文件同级文件夹中。


贡献

欢迎参与项目的改进和完善，提出建议或提交 Pull Request。


许可

本项目采用 MIT 开源协议，欢迎自由使用和传播。