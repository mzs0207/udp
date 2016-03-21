#!/usr/bin/python
# coding:utf8
import mechanize
import cookielib


class  network(object):
    def __init__(self):
        pass

    def getBrowser(self):
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()

        # option
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)

        # Follows refresh 0 but not hangs on refresh > 0
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # debugging?
        # br.set_debug_http(True)
        # br.set_debug_redirects(True)
        # br.set_debug_responses(True)

        # User-Agent (this is cheating, ok?)
        userAgetnt='Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
        br.addheaders = [('User-agent', userAgetnt)]
        return br



