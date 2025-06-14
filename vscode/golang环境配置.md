# Golang环境+Linux配置

## 一、Linux安装Go版本
在Linux机器上安装任意Golang版本，建议是使用最新版本；在安装完成后，配置如下`go env`信息；
```
GO111MODULE=auto
GOPATH=/data/workplace/go
GOPRIVATE=
GOBIN=$GOROOT/bin
```
> 这里重点关注`GOBIN`配置，通过变量引用即可以自动关联第二点vscode的goroot路径；

## 二、VSC配置
在vscode工作区配置如下内容，其中`goroot`即该项目的golang版本安装路径；
```
"go.goroot": "/usr/local/go1.20",
"go.toolsEnvVars": {
   "GOROOT": "/usr/local/go1.20"
}
```

## 三、Linux多个Golang版本管理
推荐放在`/usr/local/`路径下，并以`go1.14`，`go1.20`进行命名，结合第二点使用可以快速配置不同工作区的版本；