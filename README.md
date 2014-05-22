## About

guestpush will send to APNS providers that allow public, non-authenticated
messages. These providers typically limit the number of requests that can be
sent per hour.

## Usage

    gpush -a TestApplication -s "A Subject" boxcar2:<token>,prowl:<token> "Long message."

You can list multiple recipients separated by commas in the form of `provider:token`.
You can also send to the same user at multiple providers this way.

## Supported push providers

The following providers are configured.

* [Airgram](http://airgramapp.com/)
* [Boxcar2](http://boxcar.io/)
* [Notify My Android](https://www.notifymyandroid.com/)
* [Prowl](http://www.prowlapp.com/)

## FAQs

#### Why not support Pushover or PagerDuty?

Both Pushover and PagerDuty require a registered application. The key feature
of `guestpush` is that unauthenticated messages can be sent.

#### Why not support <something else>

I've included the providers that I know about. If you know of any others let
me know and I'll add them, or open a pull request.

#### I'd like to send messages from authenticated apps

There are several other Python modules available for sending messages
from authenticated apps. Try one of those.
