#Copyright (c) 2011-2012 Litle & Co.
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.

import unittest
import TestConfigOverride
import TestCreateFromDom
import TestLitleOnline
import TestPostGenerationScript
import TestProcessResponse
import TestLitleBatchRequest
import TestLitleBatchResponse
import TestConfiguration

testconfigoverride = TestConfigOverride.suite()
testcreatefromdom = TestCreateFromDom.suite()
testlitleonline = TestLitleOnline.suite()
testpostgenerationscript = TestPostGenerationScript.suite()
testprocessresponse = TestProcessResponse.suite()
testlitlebatchrequest = TestLitleBatchRequest.suite()
testlitlebatchresponse = TestLitleBatchResponse.suite()
testconfiguration = TestConfiguration.suite()


unittest.TextTestRunner().run(testconfigoverride)
unittest.TextTestRunner().run(testcreatefromdom)
unittest.TextTestRunner().run(testlitleonline)
unittest.TextTestRunner().run(testpostgenerationscript)
unittest.TextTestRunner().run(testprocessresponse)
unittest.TextTestRunner().run(testlitlebatchrequest)
unittest.TextTestRunner().run(testlitlebatchresponse)
unittest.TextTestRunner().run(testconfiguration)
