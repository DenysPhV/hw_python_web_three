from time import time
from datetime import datetime
from multiprocessing import cpu_count, Pool
from concurrent.futures import ProcessPoolExecutor


def factorize(*numbers):
    final_numbers_list = []
    for number in numbers:
        result_for_number = []
        for number_bit in range(1, number + 1):
            if number % number_bit == 0:
                result_for_number.append(number_bit)

        final_numbers_list.append(result_for_number)
    # raise NotImplementedError() # Remove after implementation


if __name__ == "__main__":

    test_numbers = (128, 255, 99999, 10651060)

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    # assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
    #              1521580, 2130212, 2662765, 5325530, 10651060]

    total_cpu = cpu_count()
    print(f"We start the speed testing program")
    print(f"Processes can use the following amount of CPU: {total_cpu}\n")

    print("-----------------------------------------------------------------")
    start_time_1 = time()
    print(f"Simple counting process is started at {datetime.now()}")
    factorize(*test_numbers)
    end_time_1 = time()
    print(f"Simple counting process is finished at {datetime.now()}")
    total_time_1 = end_time_1 - start_time_1
    print(f"Total time for simple counting process is {round(total_time_1, 3)} seconds\n")

    print("-----------------------------------------------------------------")
    start_time_2 = time()
    print(f"Pool counting process is started at {datetime.now()}")
    with Pool(processes=total_cpu) as pool:
        pool.map(factorize, test_numbers)
        pool.close()
        pool.join()
    end_time_2 = time()
    print(f"Pool counting process is finished at {datetime.now()}")
    total_time_2 = end_time_2 - start_time_2
    print(f"Total time for pool counting process is {round(total_time_2, 3)} seconds\n")

    print("-----------------------------------------------------------------")
    start_time_3 = time()
    print(f"Concurrent futures counting process is started at {datetime.now()}")
    with ProcessPoolExecutor(max_workers=total_cpu) as executor:
        executor.map(factorize, test_numbers)
    end_time_3 = time()
    print(f"Concurrent futures counting process is finished at {datetime.now()}")
    total_time_3 = end_time_3 - start_time_3
    print(
        f"Total time for concurrent futures counting process is {round(total_time_3, 3)} seconds\n")

