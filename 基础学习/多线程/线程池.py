import threading
import time
from concurrent.futures import ThreadPoolExecutor, wait


def fun(i):
	print(threading.current_thread().name)
	print(f'{i}开始')
	time.sleep(3)
	print(f'{i}结束')


if __name__ == '__main__':
	t_list = [x for x in range(20)]
	"""
	使用submit方式
	pool = ThreadPoolExecutor(5)  # 参数可以默认
	
	for i in range(10):
		pool.submit(fun, i)
	
	# 简写
	pool = ThreadPoolExecutor(5)  # 参数可以默认
	task_list = [pool.submit(fun, i) for i in t_list]
	wait(task_list)  # 等待线程池全部执行完毕
	"""

	# 使用map方式
	pool = ThreadPoolExecutor()
	pool.map(fun, t_list)
	print('over')
