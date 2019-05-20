
fqdn = 'cancer.bhp.org.bw'

cancer_sites = (
    ('040', 'gaborone'),
    ('060', 'francistown'),
    ('1', 'reviewer')
)


def get_site_id(name):
    return [site for site in cancer_sites if site[1] == name][0][0]
