#yaml的引用 用法；& 锚点和 * 别名，可以用来引用:
#使用python解释器运行。
#结果为josn格式。

import yaml

with open('../datas/import.yaml') as f:
    print(yaml.safe_load(f))
