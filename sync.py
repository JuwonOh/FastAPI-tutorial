import time

# 데이터 조회를 하는 함수 만들기


def find_users_sync(n):
    for i in range(1, n + 1):
        print("{}명 중 {}먕 사용자 조회중".format(n, i))
        time.sleep(1)
    print("총 {}명 사용자 비동기 조회 완료!".format(n))

# 요청을 동기 처리하는 함수 만들기


def process_sync():
    start = time.time()
    find_users_sync(3)
    find_users_sync(2)
    find_users_sync(1)
    end = time.time()
    print("동기 처리 총 소요시간: {}".format(end - start))


if __name__ == '__main__':
    process_sync()
