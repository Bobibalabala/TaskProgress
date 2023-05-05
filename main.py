# coding = utf-8
"""
实现和tqdm模块的任务进度更新功能
"""

import sys
import time

class Progress:
    def __init__(self, total=None, desc=None):
        self.total = total
        self.index = 0
        self.desc = desc
        self.print_update()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.total:
            raise StopIteration
        self.index += 1
        return self.index

    def update(self):
        self.index += 1
        self.print_update()

    def print_update(self, char='#'):
        progress = f"{self.index}/{self.total}"
        bar = f"[{self.index*char:<{self.total}}]"
        if self.desc:
            message = f"{self.desc}:{bar} {progress}"
        else:
            message = f"{bar} {progress}"
        sys.stdout.write('\r')
        sys.stdout.write(message)
        sys.stdout.flush()


def other_func():
    time.sleep(1)


if __name__ == '__main__':
    total = 10
    a = Progress(total=total, desc='test')
    for i in range(total):
        other_func()
        a.update()


