import multiprocessing
import time

from multiprocessing import Process


def fun1(name):
	print(f'我是{name}函数')
	time.sleep(5)
	print(f'{name}函数执行结束')


def fun2(name, age):
	print(f'我是{name}函数')
	time.sleep(5)
	print(f'{name}函数执行结束')


if __name__ == '__main__':
	print(multiprocessing.cpu_count())
	# 传递参数是元组, 只有一个参数的时候, 后边要加逗号
	p1 = Process(target=fun1, args=('aa',))
	p2 = Process(target=fun2, args=('bb', 12))
	# 开启子进程
	p1.start()
	p2.start()
	# 加入阻塞, 当子进程执行完毕后才会执行主进程
	p1.join()
	p2.join()
	print('over')
