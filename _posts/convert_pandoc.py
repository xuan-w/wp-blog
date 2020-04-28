#!/usr/bin/python3

import re, os, glob, sys, shutil


def is_empty(s):
    return len(s.strip()) == 0


cjk_ranges = [
    (0x4E00, 0x62FF),
    (0x6300, 0x77FF),
    (0x7800, 0x8CFF),
    (0x8D00, 0x9FCC),
    (0x3400, 0x4DB5),
    (0x20000, 0x215FF),
    (0x21600, 0x230FF),
    (0x23100, 0x245FF),
    (0x24600, 0x260FF),
    (0x26100, 0x275FF),
    (0x27600, 0x290FF),
    (0x29100, 0x2A6DF),
    (0x2A700, 0x2B734),
    (0x2B740, 0x2B81D),
    (0x2B820, 0x2CEAF),
    (0x2CEB0, 0x2EBEF),
    (0x2F800, 0x2FA1F)
]


def is_cjk(char):
    char = ord(char)
    for bottom, top in cjk_ranges:
        if bottom <= char <= top:
            return True
    return False


def join_lines(line1, line2):
    if is_cjk(line2[0]):
        return line1 + line2
    else:
        return line1 + ' ' + line2


def pangu(lines):
    new_lines = []
    for line in lines:
        tlist = []
        n = len(line)
        for i, char in enumerate(line):
            if is_cjk(char) or not char.isalnum():
                tlist.append(char)
            elif i > 0 and is_cjk(line[i - 1]):
                tlist.append(' ' + char)
            elif i < n and is_cjk(line[i + 1]):
                tlist.append(char + ' ')
            else:
                tlist.append(char)
        new_lines.append(''.join(tlist))
    return new_lines


def replace_quotation_mark(lines):
    line = ''.join(lines)
    n = len(line)
    tlist = []
    count = 0
    stack = []
    flag = False
    for i, char in enumerate(line):
        tlist.append(char)
        if is_cjk(char) and count > 0:
            flag = True
        if char == '“':
            stack.append(len(tlist) - 1)
            count += 1
        if char == '”':
            stack.append(len(tlist) - 1)
            count -= 1
            if count < 0:
                count = 0
            if count == 0 and flag:
                for j in stack:
                    if tlist[j] == '“':
                        tlist[j] = '「'
                    if tlist[j] == '”':
                        tlist[j] = '」'
            flag = False
    return ''.join(tlist)


def remove_endings(lines):
    new_lines = []
    temp = None
    for i, line in enumerate(lines):
        n = len(lines)
        if temp is None:
            if not is_empty(line):
                # begin a paragraph
                temp = line[:-1]
        else:
            # end a paragraph
            if is_empty(line):
                new_lines.append(temp + '\n')
                new_lines.append('\n')
                temp = None
            else:
                # continue a paragraph
                temp = join_lines(temp, line[:-1])
    if temp is not None:
        new_lines.append(temp + '\n')
    return new_lines


def correct_img_name(path, new_name):
    old_name = os.path.split(path)[-1]
    stem, ext = os.path.splitext(old_name)
    if ext == '.tmp':
        for name in glob.glob('media/%s*' % stem):
            new_ext = os.path.splitext(name)[1]
            if new_ext != '.tmp':
                ext = new_ext
                break
    return new_name + ext, stem + ext


def process_image(lines):
    prefix = None
    for i, line in enumerate(lines):
        line = re.sub(r'(!\[[^\[\]]*\]\([^()]*\))\{[^{}]*\}', r'\1', line)
        if re.search(r'!\[[^\[\]]*\]\([^()]*\)', line) is not None:
            if prefix is None:
                prefix = input('Please enter image prefix \n')
            org_path = re.search(r'!\[[^\[\]]*\]\(([^()]*)\)', line).group(1)
            img_name = input('Please input new name for %s \n' % org_path)
            img_name = img_name.replace(' ', '-')
            img_name, old_img_name = correct_img_name(org_path, img_name)
            new_path = '../../images/%s-%s' % (prefix, img_name)
            org_alt = re.search(r'!\[([^\[\]]*)\]\([^()]*\)', line).group(1)
            new_alt = input('Please input new alt for %s, original alt was %s \n' % (org_path, org_alt))
            line = re.sub(r'(!\[)[^\[\]]*(\]\()[^()]*(\))', r'\1 ' + new_alt + r' \2' + new_path + r'\3', line)
            shutil.copy('media/' + old_img_name, '../images/' + '%s-%s' % (prefix, img_name))
        lines[i] = line
    return lines


def get_indent(line):
    match = re.search(r'^\s*(?:[0-9a-zA-Z#]\.)?[-+*]?\s+', line)
    if match is not None:
        return len(match.group(0))
    else:
        return 0


def left_strip_quotation(line):
    match = re.search(r'^>?\s+', line)
    if match is not None:
        return line[len(match.group(0)):]
    else:
        return line


def remove_quoted_block(lines):
    new_lines = []
    indentation = 0
    one_end = False
    for line in lines:
        if line[0] == '>':
            new_lines.append(' ' * indentation + left_strip_quotation(line))
        else:
            if line == '\n':
                # if there are two \n, restart indentation count
                if one_end:
                    one_end = False
                    indentation = 0
                else:
                    one_end = True
            else:
                indentation = get_indent(line)
                one_end = False
            new_lines.append(line)
    return new_lines


def get_list_input(input_name):
    tags = []
    while True:
        tag_input = input('Please input %s, d to delete previous input\n' % input_name)
        if tag_input == '':
            break
        if tag_input == 'd' and len(tags) > 0:
            poped = tags.pop()
            print('%s was deleted' % poped)
        else:
            tags.append(tag_input)
    return tags


def generate_head():
    title = input('Please input title\n')
    slug = input('Please input slug for this post\n')
    year = input('Please input year\n')
    month = input('Please input month\n')
    day = input('Please input day\n')
    time = input('Please input time\n')
    tags = get_list_input('tags')
    cats = get_list_input('categories')

    if len(tags) == 0:
        s_tags = '[ ]'
    else:
        s_tags = '\n  - ' + '\n  - '.join(tags)

    if len(cats) == 0:
        s_cats = '  - Uncategorized'
    else:
        s_cats = '  - ' + '\n  - '.join(cats)

    return "---\npost_title: '%s'\npost_name: '%s'\npost_date: '%s-%s-%s %s'\nlayout: post\npublished: true\ntags: %s\ncategories:\n%s\n---\n" % (
        title, slug, year, month, day, time, s_tags, s_cats)


if __name__ == '__main__':
    in_md = sys.argv[1]
    out_md = sys.argv[2]
    # in_md = 'tmp.md'
    # out_md = 'tout.md'
    with open(in_md, encoding='utf-8') as fp, open(out_md, 'w', encoding='utf-8') as outfp:
        lines = fp.readlines()
        head = generate_head()
        lines = remove_quoted_block(lines)
        lines = remove_endings(lines)
        lines = pangu(lines)
        lines = process_image(lines)
        lines = replace_quotation_mark(lines)
        lines = head + lines
        outfp.writelines(lines)
