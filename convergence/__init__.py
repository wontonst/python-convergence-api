import requests

VALID_TRANSACTION_TYPES = [
    'ccauthonly',
    'ccavsonly',
    'ccsale',
    'ccverify',
    'ccgettoken',
    'cccredit',
    'ccforce',
    'ccbalinquiry',
    'ccgettoken',
    'ccreturn',
    'ccvoid',
    'cccomplete',
    'ccdelete',
    'ccupdatetip',
    'ccsignature',
    'ccaddrecurring',
    'ccaddinstall',
    'ccupdatetoken',
    'ccdeletetoken',
    'ccquerytoken'
]


class ConvergenceException(Exception):
    pass

class Converge(object):
    def __init__(self, merchant_id, user_id, pin, is_demo=False):
        self._merchant_id = merchant_id
        self._user_id = user_id
        self._pin = pin
        self._is_demo = is_demo

    @property
    def xml_endpoint(self):
        if self._is_demo:
            return "https://api.demo.convergepay.com/VirtualMerchantDemo/process.do"
        return "https://api.convergepay.com/VirtualMerchant/process.do"

    def request(self, transaction_type, **kwargs):
        """
        Make request to Converge with transaction type and parameters.
        :param transaction_type: a valid transaction type that's in VALID_TRANSACTION_TYPES
        :param kwargs:
        :return:
        """
        if transaction_type not in VALID_TRANSACTION_TYPES:
            raise ConvergenceException('{} is not a valid transaction type'.format(transaction_type))

        kwargs['ssl_transaction_type'] = transaction_type
        return self._http_request(**kwargs)

    def _http_request(self, **kwargs):
        kwargs['ssl_merchant_id'] = self._merchant_id
        kwargs['ssl_user_id'] = self._user_id
        kwargs['ssl_pin'] = self._pin
        kwargs['ssl_show_form'] = 'false'
        kwargs['ssl_result_format'] = 'ascii'

        response = requests.post(self.xml_endpoint, kwargs)
        response.raise_for_status()
        result = {}
        decoded = response.content.decode('utf-8')
        for line in decoded.split('\n'):
            k, v = line.split('=')
            result[k] = v

        result['success'] = 'errorCode' not in result
        return result
