import logging
import re
from unittest.mock import Mock, patch

from django.http import HttpResponse
from django.test import TestCase
from main.middleware import custom
from user_agents.parsers import UserAgent


logging.disable(logging.CRITICAL)
# Test strings
PC_UA_STRING = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
MOBILE_UA_STRING = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 \
    (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"


class LogTimeTakenMiddlewareTestCase(TestCase):

    @patch("main.middleware.custom.logger")
    def test_call(self, mock_logger):
        request = Mock()
        middleware = custom.LogTimeTakenMiddleware(Mock())
        # It seems inside middleware we call Mock(Mock()) (self.get_response(request))
        middleware(request)
        call_arg = mock_logger.info.call_args[0][0]
        pattern = r'^Time taken: [0-9]+\.[0-9]+ seconds'
        self.assertTrue(re.match(pattern, call_arg))


class CountRequestsMiddlewareTestCase(TestCase):

    @patch("main.middleware.custom.logger")
    def test_call(self, mock_logger):
        request = Mock()
        middleware = custom.CountRequestsMiddleware(Mock())
        middleware(request)
        call_arg = mock_logger.info.call_args[0][0]
        log_msg = 'Handled 1 requests so far'
        self.assertEqual(log_msg, call_arg)

    @patch("main.middleware.custom.logger")
    def test_process_exception(self, mock_logger):
        request = Mock()
        middleware = custom.CountRequestsMiddleware(Mock())
        middleware.process_exception(request, Exception())
        call_arg = mock_logger.info.call_args[0][0]
        log_msg = 'Encountered 1 exceptions so far'
        self.assertEqual(log_msg, call_arg)


class SetUserAgentMiddlewareTestCase(TestCase):

    def test_call(self):
        request = Mock()
        request.META = {"HTTP_USER_AGENT": PC_UA_STRING}
        middleware = custom.SetUserAgentMiddleware(Mock())
        middleware(request)
        self.assertIsInstance(request.user_agent, UserAgent)
        self.assertEqual(request.user_agent.ua_string, PC_UA_STRING)


class BlockMobileMiddlewareTestCase(TestCase):

    def test_call_pc(self):
        request = Mock()
        request.META = {"HTTP_USER_AGENT": PC_UA_STRING}
        # BlockMobileMiddleware depends on SetUserAgentMiddleware
        middleware = custom.SetUserAgentMiddleware(Mock())
        middleware(request)
        middleware = custom.BlockMobileMiddleware(Mock())
        res = middleware(request)
        # Here our request was not blocked
        self.assertIsInstance(res, Mock)

    def test_call_mobile(self):
        request = Mock()
        request.META = {"HTTP_USER_AGENT": MOBILE_UA_STRING}
        middleware = custom.SetUserAgentMiddleware(Mock())
        res = middleware(request)
        middleware = custom.BlockMobileMiddleware(Mock())
        res = middleware(request)
        # Here request gets blocked with 400 code
        self.assertIsInstance(res, HttpResponse)
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.content, b"Mobile devices are not supported")
