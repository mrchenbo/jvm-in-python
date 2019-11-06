使用python语言编写的jvm

# 开发运行环境
python 3.7.3

# 运行
python .\java.py -Xjre "C:\Program Files\Java\jre1.8.0_161" java.lang.Object

注：类名需要全限定名

## 支持命令行参数
python java.py -h 查看

# 实现的功能
- 支持类加载
- 支持类解析
- 实现了102条jvm指令
- 支持方法调用
- 支持数组和字符串
- 实现了部分本地方法调用
- 支持了异常处理

# 参考资料
《自己动手写Java虚拟机》 张秀宏

《The Java® Virtual Machine Specification Java SE 8 Edition》
