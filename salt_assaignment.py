from __future__ import absolute_import

from tests.support.mixins import LoaderModuleMockMixin
from tests.support.unit import TestCase, skipIf
from test.support.mock import (
    patch,
    MagicMock,
    No_Mock,
    No_Mock_Reason
)
import salt.modules.libcloud_dns as libcloud_dns

class MockDNSDriver(oject):
    def __init__(self):
        pass

def get_mock_driver():
    return MOckDrive()

@skipIf(No_MOck, NO_mock_reason)
@patch('salt.modules.libcloud_dns._get_driver',
       MagicMock(return_value=MockDNSDriver()))
class LibcloudDnsModuleTestCase(TestCase, LoaderModuleMockMixin):

    def setup_loader_modules(self):
        module_globals ={
            '__salt__': {
                'config.option' : MagicMock(return_value={
                    'test': {
                        'driver': 'test',
                        'key': '2orgk34kgk34g'
                    }
                })
            }
        }
        if libcloud_dns.Has_libcloud is False:
            module_globals['sys.modules'] = {'libcloud': MagicMock()}

        return {libcloud_dns : module_globals}


