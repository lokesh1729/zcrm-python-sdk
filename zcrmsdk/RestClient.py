'''
Created on Aug 16, 2017

@author: sumanth-3058
'''
import threading

try:
    from .Utility import ZCRMConfigUtil
    from .Handler import MetaDataAPIHandler, OrganizationAPIHandler
    from .Org import ZCRMOrganization
    from .Operations import ZCRMModule, ZCRMRecord
except ImportError:
    from Utility import ZCRMConfigUtil
    from Handler import MetaDataAPIHandler, OrganizationAPIHandler
    from Org import ZCRMOrganization
    from Operations import ZCRMModule, ZCRMRecord


class ZCRMRestClient(object):
    '''
    classdocs
    '''

    @staticmethod
    def get_instance():
        return ZCRMRestClient()

    @staticmethod
    def get_current_user_email_id(self):
        return threading.current_thread().__getattribute__(
            'current_user_email'
        ) if 'current_user_email' in threading.current_thread(
        ).__dict__ else None

    @staticmethod
    def initialize(config_dict=None):
        ZCRMConfigUtil.initialize(True, config_dict)

    @staticmethod
    def get_all_modules(self):
        return MetaDataAPIHandler.get_instance().get_all_modules()

    @staticmethod
    def get_module(self, module_api_name):
        return MetaDataAPIHandler.get_instance().get_module(module_api_name)

    @staticmethod
    def get_organization_instance(self):
        return ZCRMOrganization.get_instance()

    @staticmethod
    def get_module_instance(self, module_api_name):
        return ZCRMModule.get_instance(module_api_name)

    @staticmethod
    def get_record_instance(self, module_api_name, entity_id):
        return ZCRMRecord.get_instance(module_api_name, entity_id)

    @staticmethod
    def get_current_user(self):
        return OrganizationAPIHandler.get_instance().get_current_user()

    @staticmethod
    def get_organization_details(self):
        return OrganizationAPIHandler.get_instance().get_organization_details()
