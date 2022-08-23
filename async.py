import time
import asyncio

async def find_users_async(n):
	for i in range(1, n +1):
		print("{}명 중 {}먕 사용자 조회중".format(n, i))
		await asyncio.sleep(1)
	print(f'> 총 {n} 명 사용자 비동기 조회 완료!')

async def process_async():
	start = time.time()
	await asyncio.wait([
		find_users_async(3),
		find_users_async(2),
		find_users_async(1),
	])
	end = time.time()
	print('비동기 처리 총 소요 시간: {}'.format(end - start))

if __name__ == '__main__':
    asyncio.run(process_async())