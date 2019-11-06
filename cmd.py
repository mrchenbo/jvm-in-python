import argparse


def parseCmd():
    parser = argparse.ArgumentParser(description='python jvm.')
    parser.add_argument('-version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-cp', action="store", dest="classpath",
                        help="class search path of directories and zip/jar files")
    parser.add_argument('-classpath', action="store", dest="classpath", help="class search path of directories and zip/jar files. \
                            A : separated list of directories, JAR archives, \
                            and ZIP archives to search for class files.")
    parser.add_argument('-Xjre', action="store", dest="Xjre",
                        help="class search path of directories and zip/jar files")
    parser.add_argument('-verbose:inst', dest="verboseInstFlag", action='store_true', help="enable verbose output")
    parser.add_argument('clazz', metavar='class', type=str,
                        nargs=1, help='main class')
    parser.add_argument('args', metavar='args',
                        type=str, nargs='*', help='args')
    return parser.parse_args()
