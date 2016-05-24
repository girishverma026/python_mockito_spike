import unittest
from mockito import spy, mock, when, verify
  
class DemoTest(unittest.TestCase):

	def testDemo(self):
		demoMock = spy(Demo())
		when(demoMock).method2().thenReturn('mockedmethod2')

		self.assertEqual(demoMock.method1(), 'method1')
		self.assertEqual(demoMock.method2(), 'mockedmethod2')

		verify(demoMock).method1()
		verify(demoMock).method2()




class Demo(object):
	def method1(self):
		return 'method1'

	def method2(self):
		return 'method2'