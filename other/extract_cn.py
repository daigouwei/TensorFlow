import re


def extract_cn(str):
    pattern = re.compile(u'([\u4e00-\u9fa5])')
    return pattern.findall(str)


if __name__ == '__main__':
    str_list = ['rgwr我123！！！', u'sbvisjwr是']
    res_str_list = []
    for str in str_list:
        res_str_list.append(extract_cn(str))
    print(res_str_list)
