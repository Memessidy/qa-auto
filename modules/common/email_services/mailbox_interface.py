from .api_classes.maildrop_service_api import MailDrop
from .api_classes.guerrillamail_service_api import GuerrillaMail
from collections import namedtuple

Service = namedtuple('Service', 'name_of_service class_of_service domain_name')

services = [Service('maildrop', MailDrop, '@maildrop.cc'),
            Service('guerrillamail', GuerrillaMail, '@guerrillamail.com')]


class MailBox:
    def __init__(self, service, mailbox_name):
        self.__mailbox_name = mailbox_name
        self.__subject_name = "Proton Verification Code"
        self.__time_to_sleep = 5
        self.__service = service
        self.__tries_count = 10
        self.__mail_box = None
        self.__get_mail_box()

    def __get_mail_box(self):
        self.__mail_box = self.__service(mailbox=self.__mailbox_name,
                                         subject_name=self.__subject_name,
                                         sleeping_time=self.__time_to_sleep,
                                         tries_to_stop=self.__tries_count)

    def get_verification_code(self):
        return self.__mail_box.get_code_by_many_tries()


def get_mail_box(nickname):
    for service in services:
        yield MailBox(service.class_of_service, nickname), nickname + service.domain_name
