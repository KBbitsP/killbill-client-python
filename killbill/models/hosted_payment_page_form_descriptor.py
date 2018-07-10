# coding: utf-8

#
# Copyright 2014-2017 Groupon, Inc.
# Copyright 2014-2017 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.19.17-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class HostedPaymentPageFormDescriptor(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'kb_account_id': 'Str',
        'form_method': 'Str',
        'form_url': 'Str',
        'form_fields': 'Dict[String, Object]',
        'properties': 'Dict[String, Object]',
        'audit_logs': 'List[AuditLog]'
    }

    attribute_map = {
        'kb_account_id': 'kbAccountId',
        'form_method': 'formMethod',
        'form_url': 'formUrl',
        'form_fields': 'formFields',
        'properties': 'properties',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, kb_account_id=None, form_method=None, form_url=None, form_fields=None, properties=None, audit_logs=None):  # noqa: E501
        """HostedPaymentPageFormDescriptor - a model defined in Swagger"""  # noqa: E501

        self._kb_account_id = None
        self._form_method = None
        self._form_url = None
        self._form_fields = None
        self._properties = None
        self._audit_logs = None
        self.discriminator = None

        if kb_account_id is not None:
            self.kb_account_id = kb_account_id
        if form_method is not None:
            self.form_method = form_method
        if form_url is not None:
            self.form_url = form_url
        if form_fields is not None:
            self.form_fields = form_fields
        if properties is not None:
            self.properties = properties
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def kb_account_id(self):
        """Gets the kb_account_id of this HostedPaymentPageFormDescriptor.  # noqa: E501


        :return: The kb_account_id of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :rtype: Str
        """
        return self._kb_account_id

    @kb_account_id.setter
    def kb_account_id(self, kb_account_id):
        """Sets the kb_account_id of this HostedPaymentPageFormDescriptor.


        :param kb_account_id: The kb_account_id of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :type: Str
        """


        self._kb_account_id = kb_account_id

    @property
    def form_method(self):
        """Gets the form_method of this HostedPaymentPageFormDescriptor.  # noqa: E501


        :return: The form_method of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :rtype: Str
        """
        return self._form_method

    @form_method.setter
    def form_method(self, form_method):
        """Sets the form_method of this HostedPaymentPageFormDescriptor.


        :param form_method: The form_method of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :type: Str
        """


        self._form_method = form_method

    @property
    def form_url(self):
        """Gets the form_url of this HostedPaymentPageFormDescriptor.  # noqa: E501


        :return: The form_url of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :rtype: Str
        """
        return self._form_url

    @form_url.setter
    def form_url(self, form_url):
        """Sets the form_url of this HostedPaymentPageFormDescriptor.


        :param form_url: The form_url of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :type: Str
        """


        self._form_url = form_url

    @property
    def form_fields(self):
        """Gets the form_fields of this HostedPaymentPageFormDescriptor.  # noqa: E501


        :return: The form_fields of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :rtype: Dict[String, Object]
        """
        return self._form_fields

    @form_fields.setter
    def form_fields(self, form_fields):
        """Sets the form_fields of this HostedPaymentPageFormDescriptor.


        :param form_fields: The form_fields of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :type: Dict[String, Object]
        """


        self._form_fields = form_fields

    @property
    def properties(self):
        """Gets the properties of this HostedPaymentPageFormDescriptor.  # noqa: E501


        :return: The properties of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :rtype: Dict[String, Object]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this HostedPaymentPageFormDescriptor.


        :param properties: The properties of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :type: Dict[String, Object]
        """


        self._properties = properties

    @property
    def audit_logs(self):
        """Gets the audit_logs of this HostedPaymentPageFormDescriptor.  # noqa: E501


        :return: The audit_logs of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :rtype: List[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this HostedPaymentPageFormDescriptor.


        :param audit_logs: The audit_logs of this HostedPaymentPageFormDescriptor.  # noqa: E501
        :type: List[AuditLog]
        """


        self._audit_logs = audit_logs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HostedPaymentPageFormDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
