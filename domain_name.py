#Extract the top level domain from the url of a website

from tld import get_fld


def get_domain_name(url):
    domain_name = get_fld(url)
    return domain_name

