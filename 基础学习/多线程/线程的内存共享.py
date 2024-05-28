import threading

x = 0


def sum1():
	global x
	if lock.acquire():
		# 给造成数据混乱的部分添加锁
		for i in range(100000):
			x += i
			x -= i
		# 锁必须释放, 不然会造成死锁, 导致程序一直阻塞
		lock.release()
	print('sum1', x)


def sum2():
	global x
	# 锁简写
	with lock:
		# 给造成数据混乱的部分添加锁
		for i in range(100000):
			x += i
			x -= i
	print('sum2', x)


if __name__ == '__main__':
	# 锁实例化
	lock = threading.Lock()
	th1 = threading.Thread(target=sum1)
	th2 = threading.Thread(target=sum2)
	th1.start()
	th2.start()
	th1.join()
	th2.join()
	print('over')
