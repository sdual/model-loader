# -*- coding: utf-8 -*-

import multiprocessing as mp
import time


class ModelRefreshProcessCreator:

    def __init__(self, results_queue):
        self.results_queue = results_queue

    def create_process(self):
        task = Task().append_task
        process = mp.Process(target=task, args=(self.results_queue,))
        process.daemon = True
        process.start()
        print('process is created.')


class Task:

    def append_task(self, queue):
        time.sleep(5)
        queue.put('test string')


class ResultExtractor:

    def __init__(self, results_queue):
        self.results_queue = results_queue

    def extract(self, arg):
        if not self.results_queue.empty():
            result = self.results_queue.get()
            print(arg, 'extract result.')
            print(result)
        else:
            print('reuslts is empty.')
