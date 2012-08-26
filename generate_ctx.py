#!/usr/bin/python
#coding:utf-8
import re
import os
import json
import sys

conf_dict = {
    "main":{
        "template_filename":"",
        "template_path":"",
        "mode":{
            "develop":{
                "ctx":["ctx_base","ctx_develop"],
                "filename":"",
                "path":"",
            },
            "work":{
                "ctx":["ctx_base","ctx_work"],
                "filename":"",
                "path":"",
            },
        },
    },
    "ctx_base":{"":"",},
    "ctx_develop":{"":"",},
    "ctx_work":{"":"",},
}

def gc(template_filename):
    """
    Generate the empty context file
    """
    if not template_filename.endswith('template'):
        return "Template name error"
    else:
        file_name = template_filename.split('.')[0]
    context_file_name = file_name + '.ctx' 
    if os.path.exists(context_file_name):
        return "Tempalte already exists, you can edit or remove it."
    context_file = open(context_file_name, 'w')
    template_file = open(template_filename, 'r')
    template = template_file.read()

    conf_dict['main']['template_filename'] = template_filename

    template_values = {}
    for item in re.findall('{{(.*?)}}', template):
        item = item.strip()
        #context_file.write(item + ' =  \n')
        template_values['%s'%item] = ""
    conf_dict['ctx_base'] = template_values
    json.dump(conf_dict,
        context_file,
        skipkeys=False,
        ensure_ascii=False,
        check_circular=True,
        allow_nan=False,
        sort_keys=True,
        indent=2,
        encoding='utf-8',
        )
    context_file.close()
    template_file.close()
    return "Done!"

if __name__ == '__main__':
    commands = sys.argv
    if len(commands) == 2:
        result = gc(commands[1])
        print result
    else:
        print """
            Useage:$pythona generate_ctx.py {tempalte_name}
            Example:$python generate_ctx.py settings.py.template

            more info:https://github.com/silegon/onf
            """

