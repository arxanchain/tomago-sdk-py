"""
Copyright ArxanFintech Technology Ltd. 2018 All Rights Reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
                 http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import unittest
import mock
import json
import os
import sys
from cryption.crypto import sign
ROOT_PATH = os.path.join(
    os.path.dirname(__file__),
    ".."
    )
sys.path.append(ROOT_PATH)
from tomago.api.blockchain import BlockChain 
from rest.api.api import Client

class Response(object):
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

response_succ = {
    "Code": "0",
    "Message":"{\"channel_id\":\"mychannel\",\"chaincode_id\":\"mycc:\",\"transaction_id\":\"991d9f7658cb6515af4467c74842593158cf99b09c744f6d6137f751436707f9\",\"timestamp\":{\"seconds\":1502867427,\"nanos\":239380560},\"creator_id\":\"CgdPcmcxTVNQEq4GLS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUNMRENDQWRLZ0F3SUJBZ0lSQUtaSGhlQ1pQRStHTUxSVjJXWEJyMTB3Q2dZSUtvWkl6ajBFQXdJd2NERUwKTUFrR0ExVUVCaE1DVlZNeEV6QVJCZ05WQkFnVENrTmhiR2xtYjNKdWFXRXhGakFVQmdOVkJBY1REVk5oYmlCRwpjbUZ1WTJselkyOHhHVEFYQmdOVkJBb1RFRzl5WnpFdVpYaGhiWEJzWlM1amIyMHhHVEFYQmdOVkJBTVRFRzl5Clp6RXVaWGhoYlhCc1pTNWpiMjB3SGhjTk1UY3dOREl5TVRJd01qVTJXaGNOTWpjd05ESXdNVEl3TWpVMldqQmIKTVFzd0NRWURWUVFHRXdKVlV6RVRNQkVHQTFVRUNCTUtRMkZzYVdadmNtNXBZVEVXTUJRR0ExVUVCeE1OVTJGdQpJRVp5WVc1amFYTmpiekVmTUIwR0ExVUVBd3dXVlhObGNqRkFiM0puTVM1bGVHRnRjR3hsTG1OdmJUQlpNQk1HCkJ5cUdTTTQ5QWdFR0NDcUdTTTQ5QXdFSEEwSUFCRlVLdU5DbGl3VjlFNHRtU2JXV2QzdHYvNFpFNms0Q0dJaVkKYUtOSmpIWUk2WVZqbFRNRWwyTnJzU1djT01aMWF5cys5eEoyRXdqc1F2RGFpWkJuSlBlallqQmdNQTRHQTFVZApEd0VCL3dRRUF3SUZvREFUQmdOVkhTVUVEREFLQmdnckJnRUZCUWNEQVRBTUJnTlZIUk1CQWY4RUFqQUFNQ3NHCkExVWRJd1FrTUNLQUlLSXRyelZyS3F0WGt1cFQ0MTltL003eDEvR3FLem9ya3R2NytXcEVqcUpxTUFvR0NDcUcKU000OUJBTUNBMGdBTUVVQ0lRRDNoc0hTMURTOU94N3RxNDZwN3gwUVdQOXljKytNN1hBN1BSZjhMN3dYL1FJZwpVMExkSVhKcmh4QVhYMjl0Qy9xRzJRR1BBNFQ1UVRDS1paY1ZOYUFUL0xRPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==\",\"payload_size\":1888}"
    }

response_fail = {
    "Code": "107",
    "Message":"illegal base64 data at input byte 8",
    }

url = "http://127.0.0.1"
APIKEY = "pWEzB4yMM1518346407"
cert_path = "./cert_path"
cert_store = Client(
        APIKEY,
        cert_path,
        url
        )
bc = BlockChain(cert_store)
client_cipher = "client cipher"
server_cipher = "server cipher"

class TransactionTest(unittest.TestCase):
    """Transaction test. """
    def setUp(self):
        pass

    def test_invoke_succ(self):
        """Test invoke blockchain successfully returned. """

        response_succ = {
            "Code": "0",
            "Message":"{\"channel_id\":\"mychannel\",\"chaincode_id\":\"mycc:\",\"transaction_id\":\"991d9f7658cb6515af4467c74842593158cf99b09c744f6d6137f751436707f9\",\"timestamp\":{\"seconds\":1502867427,\"nanos\":239380560},\"creator_id\":\"CgdPcmcxTVNQEq4GLS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUNMRENDQWRLZ0F3SUJBZ0lSQUtaSGhlQ1pQRStHTUxSVjJXWEJyMTB3Q2dZSUtvWkl6ajBFQXdJd2NERUwKTUFrR0ExVUVCaE1DVlZNeEV6QVJCZ05WQkFnVENrTmhiR2xtYjNKdWFXRXhGakFVQmdOVkJBY1REVk5oYmlCRwpjbUZ1WTJselkyOHhHVEFYQmdOVkJBb1RFRzl5WnpFdVpYaGhiWEJzWlM1amIyMHhHVEFYQmdOVkJBTVRFRzl5Clp6RXVaWGhoYlhCc1pTNWpiMjB3SGhjTk1UY3dOREl5TVRJd01qVTJXaGNOTWpjd05ESXdNVEl3TWpVMldqQmIKTVFzd0NRWURWUVFHRXdKVlV6RVRNQkVHQTFVRUNCTUtRMkZzYVdadmNtNXBZVEVXTUJRR0ExVUVCeE1OVTJGdQpJRVp5WVc1amFYTmpiekVmTUIwR0ExVUVBd3dXVlhObGNqRkFiM0puTVM1bGVHRnRjR3hsTG1OdmJUQlpNQk1HCkJ5cUdTTTQ5QWdFR0NDcUdTTTQ5QXdFSEEwSUFCRlVLdU5DbGl3VjlFNHRtU2JXV2QzdHYvNFpFNms0Q0dJaVkKYUtOSmpIWUk2WVZqbFRNRWwyTnJzU1djT01aMWF5cys5eEoyRXdqc1F2RGFpWkJuSlBlallqQmdNQTRHQTFVZApEd0VCL3dRRUF3SUZvREFUQmdOVkhTVUVEREFLQmdnckJnRUZCUWNEQVRBTUJnTlZIUk1CQWY4RUFqQUFNQ3NHCkExVWRJd1FrTUNLQUlLSXRyelZyS3F0WGt1cFQ0MTltL003eDEvR3FLem9ya3R2NytXcEVqcUpxTUFvR0NDcUcKU000OUJBTUNBMGdBTUVVQ0lRRDNoc0hTMURTOU94N3RxNDZwN3gwUVdQOXljKytNN1hBN1BSZjhMN3dYL1FJZwpVMExkSVhKcmh4QVhYMjl0Qy9xRzJRR1BBNFQ1UVRDS1paY1ZOYUFUL0xRPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==\",\"payload_size\":1888}"
            }
        
        response_fail = {
            "Code": "107",
            "Message":"illegal base64 data at input byte 8",
            }
        mock_do_post = mock.Mock(return_value=Response(200, server_cipher))
        mock_run_cmd = mock.Mock(side_effect=[client_cipher, json.dumps(response_succ)])

        with mock.patch('cryption.crypto.run_cmd', mock_run_cmd):
            with mock.patch('requests.post', mock_do_post):
                body = {
                    "payload": {
                        "chaincode_id": "mycc",
                        "args": ["invoke", "a", "b", "1"]
                        }
                    }

                _, resp = bc.invoke({}, body)
                self.assertEqual(resp["Code"], "0")

    def test_invoke_err(self):
        """Test invoke blockchain error code. """

        mock_do_post = mock.Mock(return_value=Response(401, server_cipher))
        mock_run_cmd = mock.Mock(side_effect=[client_cipher, json.dumps(response_fail)])

        with mock.patch('cryption.crypto.run_cmd', mock_run_cmd):
            with mock.patch('requests.post', mock_do_post):
                body = {
                    "payload": {
                        "chaincode_id": "mycc",
                        "args": ["invoke", "a", "b", "1"]
                        }
                    }
                _, resp = bc.invoke({}, body)
                self.assertEqual(resp["Code"], "107")

    def test_query_succ(self):
        """Test query blockchain successfully returned. """

        response_succ = {"Message":"99"}
        
        mock_do_post = mock.Mock(return_value=Response(200, server_cipher))
        mock_run_cmd = mock.Mock(side_effect=[client_cipher, json.dumps(response_succ)])

        with mock.patch('cryption.crypto.run_cmd', mock_run_cmd):
            with mock.patch('requests.post', mock_do_post):
                body = {
                    "payload": {
                        "chaincode_id": "mycc",
                        "args": ["query", "a"] 
                        }
                    }

                _, resp = bc.query({}, body)
                self.assertEqual(resp["Message"], "99")

    def test_query_err(self):
        """Test query blockchain error code. """

        response_fail = {
            "Code": "107",
            "Message":"illegal base64 data at input byte 8",
            }

        mock_do_post = mock.Mock(return_value=Response(401, server_cipher))
        mock_run_cmd = mock.Mock(side_effect=[client_cipher, json.dumps(response_fail)])

        with mock.patch('cryption.crypto.run_cmd', mock_run_cmd):
            with mock.patch('requests.post', mock_do_post):
                body = {
                    "payload": {
                        "chaincode_id": "mycc",
                        "args": ["query", "a"]
                        }
                    }
                _, resp = bc.query({}, body)
                self.assertEqual(resp["Code"], "107")







    def test_query_txn_succ(self):
        """Test query transaction in blockchain successfully returned. """

        txid = "001"
        response_succ = {
                "Code": "0",
                "Message":"{\"channel_id\":\"mychannel\",\"chaincode_id\":\"mycc:\",\"transaction_id\":\"991d9f7658cb6515af4467c74842593158cf99b09c744f6d6137f751436707f9\",\"timestamp\":{\"seconds\":1502867427,\"nanos\":239380560},\"creator_id\":\"CgdPcmcxTVNQEq4GLS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUNMRENDQWRLZ0F3SUJBZ0lSQUtaSGhlQ1pQRStHTUxSVjJXWEJyMTB3Q2dZSUtvWkl6ajBFQXdJd2NERUwKTUFrR0ExVUVCaE1DVlZNeEV6QVJCZ05WQkFnVENrTmhiR2xtYjNKdWFXRXhGakFVQmdOVkJBY1REVk5oYmlCRwpjbUZ1WTJselkyOHhHVEFYQmdOVkJBb1RFRzl5WnpFdVpYaGhiWEJzWlM1amIyMHhHVEFYQmdOVkJBTVRFRzl5Clp6RXVaWGhoYlhCc1pTNWpiMjB3SGhjTk1UY3dOREl5TVRJd01qVTJXaGNOTWpjd05ESXdNVEl3TWpVMldqQmIKTVFzd0NRWURWUVFHRXdKVlV6RVRNQkVHQTFVRUNCTUtRMkZzYVdadmNtNXBZVEVXTUJRR0ExVUVCeE1OVTJGdQpJRVp5WVc1amFYTmpiekVmTUIwR0ExVUVBd3dXVlhObGNqRkFiM0puTVM1bGVHRnRjR3hsTG1OdmJUQlpNQk1HCkJ5cUdTTTQ5QWdFR0NDcUdTTTQ5QXdFSEEwSUFCRlVLdU5DbGl3VjlFNHRtU2JXV2QzdHYvNFpFNms0Q0dJaVkKYUtOSmpIWUk2WVZqbFRNRWwyTnJzU1djT01aMWF5cys5eEoyRXdqc1F2RGFpWkJuSlBlallqQmdNQTRHQTFVZApEd0VCL3dRRUF3SUZvREFUQmdOVkhTVUVEREFLQmdnckJnRUZCUWNEQVRBTUJnTlZIUk1CQWY4RUFqQUFNQ3NHCkExVWRJd1FrTUNLQUlLSXRyelZyS3F0WGt1cFQ0MTltL003eDEvR3FLem9ya3R2NytXcEVqcUpxTUFvR0NDcUcKU000OUJBTUNBMGdBTUVVQ0lRRDNoc0hTMURTOU94N3RxNDZwN3gwUVdQOXljKytNN1hBN1BSZjhMN3dYL1FJZwpVMExkSVhKcmh4QVhYMjl0Qy9xRzJRR1BBNFQ1UVRDS1paY1ZOYUFUL0xRPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==\",\"payload_size\":1888}"}

        mock_do_get = mock.Mock(return_value=Response(200, server_cipher))
        mock_run_cmd = mock.Mock(return_value=json.dumps(response_succ))

        with mock.patch('cryption.crypto.run_cmd', mock_run_cmd):
            with mock.patch('requests.get', mock_do_get):
                _, resp = bc.query_txn({}, txid)
                self.assertEqual(resp["Code"], "0")


    def test_query_txn_err(self):
        """Test query transaction in blockchain error code. """

        txid = "001"
        response_fail = {
            "Code": "107",
            "Message":"illegal base64 data at input byte 8",
            }

        mock_do_get = mock.Mock(return_value=Response(401, server_cipher))
        mock_run_cmd = mock.Mock(return_value=json.dumps(response_fail))

        with mock.patch('cryption.crypto.run_cmd', mock_run_cmd):
            with mock.patch('requests.get', mock_do_get):
                _, resp = bc.query_txn({}, txid)
                self.assertEqual(resp["Code"], "107")

