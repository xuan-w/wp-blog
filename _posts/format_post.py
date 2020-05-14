from convert_pandoc import *
import sys

md_name = sys.argv[1]

with open(md_name, encoding = 'utf-8') as fp:
    lines = fp.readlines()

lines = pangu(lines)
lines = replace_quotation_mark(lines)

with open(md_name, 'w', encoding = 'utf-8') as fp:
    fp.writelines(lines)
