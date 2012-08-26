onf
===
方便项目配置文件在不同环境下的修改和转换。


运行环境
--------
Python 2.7
Django 1.4(使用Django中的 template组件)

使用步骤
--------
处理所需的配置文件，将需要自动填充的字段改为django模板变量。以Django项目中的settings.py为例，改成如下样式:

    5 DEBUG = {{debug_statu}}
    6 TEMPLATE_DEBUG = {{template_debug_statu}}
    7 TEMPLATE_STRING_IF_INVALID = '{{template_string_if_invalid}}'
    8 
    9 ADMINS = (
    10     ('{{username}}', '{{user_email}}')
    11 )
    ……

做完后将settings.py文件重命名为文件[settings.py.template](https://github.com/silegon/onf/blob/master/settings.py.template)。模板文件都以template为后缀。

运行$python generate_ctx.py settings.py.template

运行后会生成settings.ctx 文件，为填充模板的内容文件json格式。

可以按照[settings.ctx.example](https://github.com/silegon/onf/blob/master/settings.ctx.example)的式样填充自己所需的内容。在添加的参数时有几点需要注意的地方。

main字典块参数解释:

    template_filename 该内容文件对应的模板文件名
    template_path     对应模板文件所在的文件目录
    mode              操作模式
        develop       开发模式
            ctx       对应模式的内容组，例如内容为["ctx_base","ctx_develop"]的时候，填充模板的内容就为ctx_base字典与ctx_develop字典
            path      对应配置文件应该写入的位置
        work          工作模式 
    ……              (可以自定个各种模式)
    ctx_base          基础的内容块
    ctx_develop       develop模式的内容块
    ……              (可以继续添加各个内容快)

运行$python generate_conf.py settings.py.ctx develop 就可以将所需的配置文件生成到指定地方了。

