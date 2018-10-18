# User guide:
# put the test files and this script under the same directory, open your bash under this path,
# python version should be python 3.5 and don't forget to add your python to environment variables
# type the instruction as following:
# python c1.py [filename]


# Following programming languages can be scanned by this tool
# Java, C/C++, Javascript, Typescript, python
# html/css is not included in this tool. Because the comment symbol is <!----> or /**/ alone.
# So all the comment line will be within comment block.
# Therefore it is meaningless in this problem

import os,re,argparse,sys


class LineCalculator:

    def __init__(self):
        self.type = None

        self.total_lines = 0
        self.single_line = 0
        self.multi_lines = 0
        self.comment_lines = 0
        self.block_line_comment = 0
        self.todo = 0

        self.text = None
        self.f = None # define file object

    def file_input(self, path, filename):
        self.__init__()
        self.type = filename.split('.')[-1]
        self.f = open(path)
        self.text = self.f.read()
        self.f.close()
        if self.type == "c" or self.type == "cpp" or self.type == "js" or \
                        self.type == "java" or self.type == "ts":
            self.get_c()
        elif self.type == "py":
            self.get_py()
        else:
            print("Invalid file type")

# handle the case for c/c++, java, javascript, typescript
# because they share the same comment judge standard

    def get_c(self):
        lines = self.text.split('\n')
        self.total_lines = len(lines)
        is_string = False
        is_single = False
        is_multi = False
        i=0
        while i < len(self.text):
            # handle the case for string. The symbols would be invalid in string
            if ((self.text[i] == "\'") or (self.text[i] == "\"")) and is_string is False:
                is_string = True
                i += 1
                while (i<len(self.text)) and ((self.text[i] != "'") or (self.text[i] != "\"")):
                    i += 1
                is_string = False
            # handle the cases of single line calculating
            if (i+1<len(self.text)) and (self.text[i] == "/") and (self.text[i+1] == "/") and (is_single is False):
                is_single = True
                self.single_line += 1
                i += 2
                is_todo = False
                while self.text[i]!='\n':
                    if self.text[i:i+4].upper() == "TODO" and is_todo is False:  # multiple todos in single line comment regarded as one
                        self.todo += 1
                        is_todo = True
                    i += 1
                is_single = False
                is_todo = True
            # handle the cases of comments within a block
            if (i+1<len(self.text)) and (self.text[i] == "/") and (self.text[i+1] == "*") and (is_multi is False):
                is_multi = True
                self.block_line_comment += 1 # calculate block
                i += 2
                while not (self.text[i] == "*" and self.text[i+1] == "/"):
                    if self.text[i] == '\n':
                        self.multi_lines += 1
                    i += 1
                i += 2
                self.multi_lines += 1
                is_multi = False
            i += 1

# calculate python file comments
    def get_py(self):
        self.total_lines = len(self.text.split('\n'))
        i = 0
        lines = re.sub(r"\'\'\'.*?\'\'\'", " ", self.text, flags=re.S).split('\n')  #replace all the string within '''''' with space
        while i < len(lines):
            if i<len(lines):
                line = re.sub(r"\'.*?\'", " ", lines[i])  # replace all the string within "" or '' with space
                line = re.sub(r"\".*?\"", " ", line)

                if re.search(r"#(\s*)todo", line, flags=re.I):   # only the comment starts with "todo" will be regarded as todo
                    self.todo += 1
                if lines[i].lstrip().startswith("#"):
                    count = 1
                    i += 1
                    while lines[i].lstrip().startswith("#"):
                        count += 1
                        i += 1
                    if count > 1:
                        self.multi_lines += count
                        self.block_line_comment += 1
                    else:
                        self.single_line += 1
                else:
                    if line.find("#") != -1:
                        self.single_line += 1
                i += 1

    def print_result(self):
        print("Total # of lines: "+str(self.total_lines))
        print("Total # of comment lines: " + str(self.single_line + self.multi_lines))
        print("Total # of single line comments: "+str(self.single_line))
        print("Total # of comment lines within block comments: "+str(self.multi_lines))
        print("Total # of block line comments: "+str(self.block_line_comment))
        print("Total # of TODOs: " + str(self.todo))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", default="false", nargs='*')

    args = parser.parse_args(sys.argv[1:])
    filename=args.filename[0]
    c=LineCalculator()
    c.file_input(filename)
    c.print_result()

