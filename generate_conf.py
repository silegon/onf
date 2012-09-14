#!/usr/bin/python
#coding:utf-8
import json
import sys
import os
from django.template import Context, Template
from django.conf import settings

ERROR_MARK = '$$ERROR$$'
settings.configure(DEBUG=False, TEMPLATE_DEBUG=False, 
                   TEMPLATE_STRING_IF_INVALID=ERROR_MARK,
                  )

def fill_conf(ctx, mode):
    ctx_f = open(ctx, 'r')
    ctx = json.load(ctx_f,
                    encoding="utf-8",
                   )
    template_file = os.path.join(ctx['main']['template_path'], ctx['main']['template_filename'])
    template_f = open(template_file, 'r')
    template = Template(template_f.read())
    ctx_mode = ctx['main']['mode'][mode]
    conf_path = ctx_mode['path']
    conf_filename = ctx_mode['filename']
    conf_destination = os.path.join(conf_path, conf_filename)
    conf_content = ctx_mode['ctx']
    context = {}
    for d in conf_content:
        sub_ctx = ctx[d]
        context.update(sub_ctx)

    output_f = open(conf_destination, 'w')
    output = template.render(Context(context))
    if ERROR_MARK in output:
        print "Rendering data error!!"
    output_f.write(output)
    output_f.close()


if __name__ == '__main__':
    commands = sys.argv
    if len(commands) == 3:
        ctx = sys.argv[1]
        mode = sys.argv[2]
        fill_conf(ctx, mode)
        print 'Done!'
    else:
        print """
        Useage:python generate_conf.py {ctx_name} {mode}
        Example:python generate_conf.py settings.ctx develop

        more info:https://github.com/silegon/onf
        """
