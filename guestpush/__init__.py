# -*- coding: utf-8 -*-

# Copyright 2014 Brian Bennett
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
guestpush will send to APNS providers that allow public, non-authenticated
messages. These providers typically limit the number of requests that can be
sent per hour.
"""


import requests


def send(provider_recipient, message):
    provider, recipient = provider_recipient.split(':')
    method = globals()[provider]
    method(recipient, message)


def airgram(applicaiton, subject, recipient, message):
    """
    Send push notifications to Airgram app
    See http://airgramapp.com/
    """
    api = 'https://api.airgramapp.com/1/send_as_guest'
    payload = {'email': recipient,
               'msg': '%s -- %s -- %s' % (applicaiton, subject, message)}
    return __call_provider(api, payload)


def boxcar():
    """
    This method is reserved for the legacy Boxcar API and App which was replaced
    with Boxcar 2. It's included only to avoid confusion. The legacy API and app
    are not supported. You should use boxcar2 instead.
    """
    return 501


def boxcar2(application, subject, recipient, message):
    """
    Send push notifications to Boxcar 2 app.
    See http://boxcar.io/
    """
    api = 'https://new.boxcar.io/api/notifications'
    payload = {'user_credentials': recipient,
               'notification[title]': '%s -- %s' % (application, subject),
               'notification[long_message]': message,
               'notification[sound]': 'digital-alarm'}
    return __call_provider(api, payload)


def nma(application, subject, recipient, message):
    """
    Send push notifications to Notify My Android.
    See http://notifymyandroid.com/
    """
    api = 'https://www.notifymyandroid.com/publicapi/notify'
    payload = {'apikey': recipient,
               'application': application,
               'event': subject,
               'description': message}
    return __call_provider(api, payload)


def prowl(application, subject, recipient, message):
    """
    Send push notifications to Prowl, a Growl client.
    See http://prowlapp.com/
    """
    api = 'https://api.prowlapp.com/publicapi/add'
    payload = {'apikey': recipient,
               'application': application,
               'event': subject,
               'description': message}
    return __call_provider(api, payload)


def __call_provider(api, payload):
    """
    Call remote HTTP endpoint.
    """
    r = requests.post(api, data=payload, verify=False)
    return r.status_code


def notify(application, subject, provider_recipient_list, message):
    """
    Generic notification method. When passed a list with elements in the format
    of provider:recipient, the appropriate provider will be called for the
    specified recipient.
    """
    for provider_recipient in provider_recipient_list.split(','):
        provider, recipient = provider_recipient.split(':')
        method = globals()[provider]
        r = method(application, subject, recipient, message)
        print r
