from django  import template

register=template.Library()

@register.filter(name='replace_char')
def replace_char(valu):
    valu2=valu
    for i in valu:
        print('vawww',i)
    # print("bawwwwwwwwww",valu2)
    
    return valu2