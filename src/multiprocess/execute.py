# -*- coding: utf-8 -*-

import multiprocessing as mp
from model_refresh_process import ModelRefreshProcessCreator
from model_refresh_process import ResultExtractor
import time


def main():

    results = mp.JoinableQueue()
    results.join()  # wait until jobs queue is empty.
    create_process(results)


def create_process(results_queue):
    for i in range(10):
        extractor = ResultExtractor(results_queue)
        extractor.extract(i)

        if i == 3:
            mp_creator = ModelRefreshProcessCreator(results_queue)
            mp_creator.create_process()
        time.sleep(2)
    time.sleep(10)

if __name__ == '__main__':
    main()
