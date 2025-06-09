import asyncio


async def fun(i):
	print('我是fun函数开始:', i)
	await asyncio.sleep(2)
	print('我是fun函数结束:', i)
	return i


def call_back(f):
	print(f.result())


async def main():
	tasks = []
	for i in range(5):
		task = asyncio.create_task(fun(i))
		tasks.append(task)

	done, pending = await asyncio.wait(tasks)

	for d in done:
		print('返回值', d.result())

if __name__ == '__main__':
	# loop = asyncio.get_event_loop()
	# loop.run_until_complete(main())
	asyncio.run(main())
