# -*- coding: utf-8 -*-
import re
import json
import sys
import codecs



def compare_str():
    hosts = host_plain()
    groups = group_obj()
    try:
        for key, value in hosts.items():
            for key_1 in groups:
                if key == key_1:
                    groups.update({key: value})
    except ValueError:
        pass
    print(group for group in groups)
    with open("C:\\_python\\results\\results_finish.txt", 'a+') as file:
        for hostname, ipaddr in groups.items():
            file.write("{} {}\n".format(hostname, ipaddr))

def host_plain():
    with codecs.open("C:\_python\\attestaciya\\objects_5_0.C", "r", "utf-8", errors='ignore') as file:
        result_str = []
        index = 0
        dict_parse = {}
        for line in file:
            if re.findall(r'\s+:ClassName\s\(host_plain\)', line):
                index = 1
            elif index == 1:
                name = re.findall(r'\s+:name\s\(\S+\)', line)
                if name:
                    index = 2
                    name_parse = re.findall(r'\b\S+\b', name[0])
            elif index == 2:
                ip_addr = re.findall(r'\s+:ipaddr\s\(\S+\)', line)
                if ip_addr:
                    index = 0
                    ip_addr_parse = re.findall(r'\b\S+\b', ip_addr[0])
                    dict_parse[name_parse[1]] = ip_addr_parse[1]
                    # result_str.append(name_parse[1] + "   " + ip_addr_parse[1])
    with codecs.open("C:\_python\\results\\results_parse.txt", "a+", "cp1251", errors='ignore') as file:
        for line in result_str:
            file.write(line + "\n")
    return dict_parse

def group_obj():
    with codecs.open("C:\_python\\attestaciya\\objects_5_0.C", "r", "utf-8", errors='ignore') as file:
        result_str = []
        index = 0
        dict_name = {}
        ref_obj = None
        for line in file:
            if re.findall(r'\s+:ClassName\s\(network_object_group\)', line):
                index = 1
            elif index == 1:
                name = re.findall(r'\s+:name\s\(\S+\)', line)
                if name:
                    index = 2
                    name_parse = re.findall(r'\b\S+\b', name[0])
                    name_parse[1] = "\n" + "Group:  " + name_parse[1] + "\n"
                    result_str.append(name_parse[1])
                    dict_name[name_parse[1]] = " "
            elif index == 2:
                if re.findall(r'\s+:color', line):
                    index = 0
                elif re.findall(r'\s+:\s\(ReferenceObject', line):
                    ref_obj = 1
                elif ref_obj:
                        if re.findall(r'\s+:Name\s\(\S+\)', line):
                            ref_obj_parse = re.findall(r'\b\S+\b', line)
                            if ref_obj_parse:
                                dict_name[ref_obj_parse[1]] = ""
                                ref_obj = None
                                result_str.append(ref_obj_parse[1])
        with codecs.open("C:\_python\\results\\results_parse_groups.txt", "a+", "cp1251", errors='ignore') as file:
            for line in result_str:
                file.write(line + "\n")
        return dict_name


compare_str()
# group_obj()
# host_plain()