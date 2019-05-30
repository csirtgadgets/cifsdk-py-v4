

from cifsdk.client.http import HTTP as Client
from cifsdk.constants import REMOTE, TOKEN


def search(filters={}):
    if len(filters) == 0:
        filters = {
            'itype': 'ipv4',
            'tags': 'botnet'
        }

    cli = Client()

    