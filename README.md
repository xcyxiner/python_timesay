# 时光说 网站奖池数据分析
* 使用python 显示折线图
* 使用python 结合numpy以及pandas进行统计分析
* 计算毛利润 总奖池
* 计算净利润 总奖池-出题人奖励(总奖池*4%)-获胜方奖励(总奖池*95%*获胜方占比)


# 参考资料
* [Python-Matplotlib 7 饼状图](https://www.cnblogs.com/zsr0401/p/6405538.html)
* [Scrapy入门教程](https://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)


# 前置条件

```
python 2.7
pip install numpy 
pip install matplotlib
pip install pandas
pip install csv
pip install Scrapy
```


# 相关脚本

```
1.py matplotlib 饼状图
1.sh scrapy执行命令以及shell调试
2.py matplotlib 折线图以及 pandas 统计 总奖池,根据列表
3.py 已完成的答题详情页面URL地址测试
4.py 获胜方的比率(总奖池95%为基础）以及奖池奖金
```


# 结果相关

```
timesay/
├── money.json   --总奖池保存结果
├── money.png    --总奖池统计折线图
├── money.txt    --总奖池统计结果
├── scrapy.cfg
├── timesay
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── items.py    --数据保存的模型类
│   ├── items.pyc
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   ├── settings.pyc
│   └── spiders
│       ├── __init__.py
│       ├── __init__.pyc
│       ├── tsTotalMoney.py   --爬虫脚本
│       └── tsTotalMoney.pyc
├── url.json      --每期地址
├── url2.json     --测试期的地址
└── win.json      --获胜方比率以及总奖池金额
```