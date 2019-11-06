from cmd import parseCmd
from jvm import newJVM


def main():
    cmd = parseCmd()
    newJVM(cmd).start()

# python .\java.py -Xjre "C:\Program Files\Java\jre1.8.0_161" java.lang.Object
# ch09.exe -Xjre "C:\Program Files\Java\jre1.8.0_161" -classpath "E:\experment\jmv.py" Main
main()
