from __future__ import absolute_import

import somemodule.module

class SomeModuleTest(TestCase, LoderModuleMockMixin):

    def setup_loader_module(self):
        return {
            somemodule: {
                '__opts__': {'test': True}

            }
        }