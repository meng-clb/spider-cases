import threading
import time


def fun(i):
	print(threading.current_thread().name)
	print(f'{i}开始')
	time.sleep(3)
	print(f'{i}结束')


if __name__ == '__main__':
	"""
	# 属于单线程
	# for i in range(5):
		# th = threading.Thread(target=fun, args=(i,), name='th1')
		# th.start()
		# th.join()
	"""
	t_list = []
	# 并发执行5个线程
	for i in range(5):
		th = threading.Thread(target=fun, args=(i,), name='th1')
		# 线程对象添加到列表中
		t_list.append(th)
	# 循环开启子线程
	for t in t_list:
		t.start()
	# 循环阻塞子线程
	for i in t_list:
		i.join()
	print('over')
