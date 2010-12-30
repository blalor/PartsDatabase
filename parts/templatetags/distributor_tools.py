from django import template

register = template.Library()

@register.filter
def link_for_part(distributor_part):
    url_template = "http://www.google.com/search?rls=en&q=%s&ie=UTF-8&oe=UTF-8"
    
    if distributor_part.distributor.name == 'Mouser':
        url_template = "http://www.mouser.com/Search/refine.aspx?KeyWord=%s"
    elif distributor_part.distributor.name == 'Digi-Key':
        url_template = "http://search.digikey.com/scripts/DkSearch/dksus.dll?lang=en&site=US&KeyWords=%s"
    elif distributor_part.distributor.name == 'Jameco':
        url_template = "https://www.jameco.com/webapp/wcs/stores/servlet/ProductDisplay?storeId=10001&langId=-1&catalogId=10001&productId=%s"
    
    return url_template % distributor_part.dist_part_num

link_for_part.is_safe = True


