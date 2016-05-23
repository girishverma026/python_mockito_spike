import unittest
from mockito import spy, mock, when, verify
  
class DemoTest(unittest.TestCase):
	def testStubbing(self):
	  # create a mock
	  ourMock = mock()

	  # stub it
	  when(ourMock).getStuff("cool").thenReturn("cool stuff")
	  
	  # use the mock
	  self.assertEqual("cool stuff", ourMock.getStuff("cool"))
	  
	  # what happens when you pass different argument?
	  self.assertEqual(None, ourMock.getStuff("different argument"))
  
	def testVerification(self):
	  # create a mock
	  theMock = mock()

	  # use the mock
	  theMock.doStuff("cool")
	  
	  # verify the interactions. Method and parameters must match. Otherwise verification error.

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