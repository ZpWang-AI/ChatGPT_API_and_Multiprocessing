import threading
import time
import random


def worker(num):
    """线程要执行的任务"""
    print(f"Worker {num} 开始执行")
    
    # 在这里编写具体的任务逻辑
    time.sleep(random.random()*3)

    print(f"Worker {num} 执行结束")


# 创建线程列表
threads = []

# 创建并启动多个线程
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print("所有线程执行完毕")