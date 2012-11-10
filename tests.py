'''
Created on 10.11.2012

@author: jussikin
'''
import unittest
from datetime import datetime
import Arki

class Test(unittest.TestCase):

    def testUuusivuosi(self):
        uusivuosi = datetime(year=2013,day=1,month=1)
        self.assertFalse(Arki.isWorkday(uusivuosi), "New year should be holyday")
    
    def testNormalDay(self):
        normalDay = datetime(year=2012,day=8,month=11)
        self.assertTrue(Arki.isWorkday(normalDay), "year=2012,day=8,month=11 Should be normal work day ")
        
    def testSaturdayDay(self):
        sat = datetime(year=2012,day=10,month=11)
        self.assertFalse(Arki.isWorkday(sat), "year=2012,day=10,month=11 Should not be workday")
        
    def testSundayDay(self):
        sun = datetime(year=2012,day=11,month=11)
        self.assertFalse(Arki.isWorkday(sun), "year=2012,day=11,month=11 Should not be workday")
        
    def testEasterDay(self):
        sun = datetime(year=2017,day=16,month=4)
        self.assertFalse(Arki.isWorkday(sun), "year=2017,day=16,month=4 Should not be workday")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()