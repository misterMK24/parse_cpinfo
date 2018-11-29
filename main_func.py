# -*- coding: utf-8 -*-
import re
import json
import sys
import codecs

def main_func():
    with codecs.open("C:\_python\\attestaciya\\objects_5_0.C", "r", "utf-8", errors='ignore') as file:
        result_str = []
        index = 0
        dict_parse = dict.fromkeys('name', 'ipaddr')
        for line in file:
            if re.findall(r'\s+:ClassName\s\(host_plain\)', line):
                index = 1
            elif index == 1:
                name = re.findall(r'\s+:name\s\(\S+\)', line)
                if name:
                    index = 2
                    name_parse = re.findall(r'\b\S+\b', name[0])
                    # print(name_parse[1])
                    # result_str.append(name[0])
            elif index == 2:
                ip_addr = re.findall(r'\s+:ipaddr\s\(\S+\)', line)
                if ip_addr:
                    index = 0
                    ip_addr_parse = re.findall(r'\b\S+\b', ip_addr[0])
                    # print(ip_addr_parse[1])
                    result_str.append(name_parse[1] + "   " + ip_addr_parse[1])
    with codecs.open("C:\_python\\results\\results_parse.txt", "a+", "cp1251", errors='ignore') as file:
        for line in result_str:
            file.write(line + "\n")


main_func()