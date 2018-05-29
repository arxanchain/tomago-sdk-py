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

import json
from rest.api.common import APIKEYHEADER, ROUTETAG
from common import VERSION

class BlockChain(object):
    """A blockchain client implementation."""

    def __init__(self, client):
        """Init blockchain client with Client."""

        self.__route_tag = "tomago"
        self.__path = "blockchain"
        self.__client = client


    def __set_header(self, header):
        """Set wallet client header"""

        if APIKEYHEADER not in header:
            header[APIKEYHEADER] = self.__client.get_apikey()
        if ROUTETAG not in header:
            header[ROUTETAG] = self.__route_tag

        return header


    def __set_params(self, header, req_path, url_params={}, body={}):
        header = self.__set_header(header)
        if req_path:
            request_url = "/".join([
                    self.__client.get_ip(),
                    self.__route_tag,
                    VERSION,
                    self.__path,
                    req_path 
                    ])
        else:
            request_url = "/".join([
                    self.__client.get_ip(),
                    self.__route_tag,
                    VERSION,
                    self.__path,
                    ])
        if url_params:
            params = "&".join("{}={}".format(x, url_params[x]) \
                    for x in url_params)
            request_url = "?".join([request_url, params])

        self.__client.set_url(request_url)
        req_params = {
                "body": body,
                "headers": header
                }
        return req_params


    def invoke(self, header, body):
        """Invoke a blockchain."""

        req_path = "blockchain/invoke"
        method = self.__client.do_post
        req_params = self.__set_params(
                header,
                req_path,
                body=body
                )
        return self.__client.do_request(
                req_params,
                method
                )


    def query(self, header, body):
        """Query status of a blockchain."""

        req_path = "blockchain/query"
        method = self.__client.do_post
        req_params = self.__set_params(
                header,
                req_path,
                body=body
                )
        return self.__client.do_request(
                req_params,
                method
                )


    def query_txn(self, header, txnid):
        """Query status of a transaction in the blockchain."""

        req_path = "blockchain/query/" + txnid 
        method = self.__client.do_get
        req_params = self.__set_params(
                header,
                req_path
                )
        return self.__client.do_request(
                req_params,
                method
                )

