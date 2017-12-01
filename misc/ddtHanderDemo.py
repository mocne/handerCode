# -*- coding: utf-8 -*-

import ddt
import unittest

# test data
test_data1 = [
	{'username': 'zhangsan', 'pwd': 'zhangsan'},
	{'username': 'lisi', 'pwd': 'lisi'},
	{'username': 'wanger', 'pwd': 'wanger'},
	{'username': 'mazi', 'pwd': 'mazi'}
]

test_data2 = [
	{'username': 'sanzang', 'pwd': 'sanzang'},
	{'username': 'wukong', 'pwd': 'wukong'},
	{'username': 'wuneng', 'pwd': 'wuneng'},
	{'username': 'wujing', 'pwd': 'wujing'}
]

@ddt.ddt
class Test(unittest.TestCase):
	def setUp(self):
		print('start to test')

	def tearDown(self):
		print('test end !')
	
	@ddt.data(*test_data1)
	def test_ddt1(self, data):
		print(test_data1)

	@ddt.data(*test_data2)
	def test_ddt2(self, data):
		print(test_data2)

if __name__ == '__main__':
	sart_time = datatime.datatime.now()

	unittest.main()

	end_time = datatime.datatime.now()
	str((endtime - starttime).mi) + "毫秒"