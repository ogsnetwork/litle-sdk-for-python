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

from litleSdkPythonTest.all.SetupTest import *
import unittest

class TestForceCapture(unittest.TestCase):
    
    def testSimpleForceCaptureWithCard(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106L
        forcecapture.orderId = '12344'
        forcecapture.orderSource = 'ecommerce'
        
        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        forcecapture.card = card
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(forcecapture)
        self.assertEquals("Approved",response.message)

        
    def testSimpleForceCaptureWithToken(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106L
        forcecapture.orderId = '12344'
        forcecapture.orderSource = 'ecommerce'
        
        token = litleXmlFields.cardTokenType()
        token.type = 'VI'
        token.expDate = "1210"
        token.litleToken = "123456789101112"
        token.cardValidationNum = "555"
        forcecapture.token = token
        
        litleXml =  litleOnlineRequest(config)
        response = litleXml.sendRequest(forcecapture)
        self.assertEquals("Approved",response.message)

def suite():
    suite = unittest.TestSuite()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestForceCapture)
    return suite