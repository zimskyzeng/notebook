# Python代码格式化配置

> 本教程使用`black`工具+`filewatcher`插件实现对代码进行格式化；使用`isort`工具+`filewatcher`插件实现对python导入包进行排序优化；

## 一、安装VSC插件
在插件管理中搜索`File Watcher`插件并安装；
> 若是在远程Linux服务，注意需要安装在远端；

## 二、安装Python工具
使用`python3`命令安装`black`和`isort`工具；
```bash
python3 -m pip install black
python3 -m pip install isort
```

## 三、配置VSC
在vscode的工作区配置中，添加如下内容：
```
"filewatcher.commands": [
    {
        "match": ".*\\.py$",
        "isAsync": false,
        "cmd": "cd '${fileDirname}' && /root/.pyenv/versions/3.6.15/envs/gsops/bin/black '${file}' > /tmp/black.log 2>&1",
        "event": "onFileChange"
    },
    {
        "match": ".*\\.py$",
        "isAsync": false,
        "cmd": "cd '${fileDirname}' && /root/.pyenv/versions/3.6.15/envs/gsops/bin/isort '${file}' > /tmp/isort.log 2>&1",
        "event": "onFileChange"
    }
]
```
注意这里需要将实际的`black`工具和`isort`工具实际路径进行替换。这样在保存文件时，即可自动进行格式化并且对导入包进行排序；