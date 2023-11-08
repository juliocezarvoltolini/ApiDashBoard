# -*- coding: utf-8 -*-
from django.conf import settings


class ExceptionMessage:
    def __init__(self):
        self.LANGUAGE_CODE = settings.LANGUAGE_CODE

        self.translations = [
            {'lang': 'en-US', 'message-cpf': 'Invalid CPF', 'message-cnpj': 'Invalid CNPJ'},
            {'lang': 'pt-BR', 'message-cpf': 'CPF inválido', 'message-cnpj': 'CNPJ inválido. Obs.: Deve informar apenas números.'},
            {'lang': 'es-ES', 'message-cpf': 'CPF no válido', 'message-cnpj': 'CNPJ no válido. Obs.: Deve informar apenas números.'},
        ]

    def invalid_cpf(self):
        for tr in self.translations:
            if tr['lang'] == self.LANGUAGE_CODE:
                return tr['message-cpf']

    def invalid_cnpj(self):
        for tr in self.translations:
            if tr['lang'] == self.LANGUAGE_CODE:
                return tr['message-cnpj']