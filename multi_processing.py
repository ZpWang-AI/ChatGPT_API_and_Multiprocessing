##########
# 多进程
import multiprocessing
import time
import random


def worker(num):
    """进程要执行的任务"""
    print(f"Worker {num} 开始执行")
    
    # 在这里编写具体的任务逻辑
    time.sleep(random.random()*3)
    
    print(f"Worker {num} 执行结束")


if __name__ == '__main__':
    multiprocessing.freeze_support()  # 确保正确启动子进程，避免冲突

    # 创建进程列表
    processes = []

    # 创建并启动多个进程
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # 等待所有进程完成
    for p in processes:
        p.join()

    print("所有进程执行完毕")