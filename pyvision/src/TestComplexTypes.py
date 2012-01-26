#!/usr/bin/env python
#########################################################
#	Name: 	Test_ComplexTypes.py		#
#	Description: TODO	#
#########################################################

import unittest
import logging
from datetime import datetime, timedelta

from ComplexTypes import Control

class TestComplexTypes(unittest.TestCase):
    def setUp(self):
        logging.debug("Initializing variables ")
        self.control = Control()

    def test_Initialisation(self):
        c = Control()
        a = Alert()

    def test_Empty(self):
        logging.info("Testing ")
        self.control.seconds = None
        self.control.starting = None
        self.control.command = None
        answer = self.control.schedule()
        logging.debug(type(answer))
        logging.debug(type(datetime.now()))
        self.assertIs(answer, None, msg = "Answer value is " + str(answer))

    def test_ZeroPeriodNoStartingDate(self):
        self.control.seconds = 0
        self.control.starting = None
        answer = self.control.schedule()
        self.assertIs(answer, None, msg = "Answer value is " + str(answer))

    def test_ZeroPeriodPastStarting(self):
        self.control.seconds = 0
        delta = timedelta(days = 10)
        self.control.starting = datetime.now() - delta
        answer = self.control.schedule()
        self.assertIs(answer, None, msg = "Answer value is " + str(answer))
    
    def test_ZeroPeriodFuturStarting(self):
        self.control.seconds = 0
        delta = timedelta(days = 1)
        self.control.starting = datetime.now() + delta
        answer = self.control.schedule()
        self.assertTrue(answer == self.control.starting)

    def test_NegativePeriod(self):
        self.control.seconds = -100
        self.control.starting = datetime.now()
        answer = self.control.schedule()
        self.assertTrue(answer == None)

    def testPositivePeriodPastStarting(self):
        self.control.seconds = 100
        delta = timedelta(days = 1)
        now = datetime.now()
        self.control.starting = datetime.now() - delta
        answer = self.control.schedule()
        self.assertGreaterEqual(answer, now)


    def testPositivePeriodNoStarting(self):
	self.control.seconds = 100
        now = datetime.now()
        self.control.starting = None
        answer = self.control.schedule()
        self.assertGreaterEqual(answer, now)

    def testPositivePeriodFutureStarting(self):
	self.control.seconds = 100
        delta = timedelta(days = 1)
        now = datetime.now()
        self.control.starting = now + delta
        answer = self.control.schedule()
        self.assertEqual(answer, now + delta)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    unittest.main()
