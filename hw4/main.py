import time, threading, multiprocessing, math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

num_processes = 10
sz = 200000


def fib(n):
    ans = list()
    ans.append(0)
    ans.append(1)
    for i in range(2, n + 1):
        ans.append(ans[i - 2] + ans[i - 1])
    return ans[n]


if __name__ == '__main__':

    def easy():
        with open("artifacts/easy.txt", 'w') as f:
            f.write("Threading:\n")
            start_time = time.time_ns()
            thread_list = list()
            for i in range(num_processes):
                t = threading.Thread(target=fib, args=(sz,))
                t.start()
                thread_list.append(t)
            for i in range(num_processes):
                thread_list[i].join()
            end_time = time.time_ns()
            f.write(str(end_time - start_time) + ' nanoseconds\n\n')

            f.write("Multiprocessing:\n")
            start_time = time.time_ns()
            multiprocessing_list = list()
            for i in range(num_processes):
                p = multiprocessing.Process(target=fib, args=(sz,))
                p.start()
                multiprocessing_list.append(p)
            for i in range(num_processes):
                multiprocessing_list[i].join()
            end_time = time.time_ns()
            f.write(str(end_time - start_time) + ' nanoseconds\n')

    def medium():

        class Integer:

            def __init__(self):
                self.value = 0


        def simple_integrate(res, func, a, b, n_iter):
            acc = 0
            step = (b - a) / n_iter
            for i in range(n_iter):
                acc += func(a + i * step) * step
            res.value += acc

        def integrate(func, a, b, *, n_jobs=1, n_iter=10000000):
            with ProcessPoolExecutor(max_workers=n_jobs) as executor:
                step = (b - a) / n_jobs
                n_iter_step = int(n_iter / n_jobs)
                res = Integer()
                logg_time = list()
                start_time = time.time_ns()
                for i in range(n_jobs):
                    logg_time.append(time.time_ns() - start_time)
                    executor.submit(simple_integrate, res, func, a + step * i, a + step * (i + 1), n_iter_step)
                return res.value, logg_time

        with open("artifacts/medium.txt", 'a') as f:
            value, logs = integrate(math.cos, 0, math.pi / 2, n_jobs=10)
            f.write("Logs:\n")
            for i, log in enumerate(logs):
                f.write('Process ' + str(i) + ' started at: ' + str(log) + '\n')
            f.write('\n')

            for i in range(1, 16):
                start_time = time.time_ns()
                integrate(math.cos, 0, math.pi / 2, n_jobs=i)
                end_time = time.time_ns()
                f.write("Number of processes: " + str(i) + ", " + "time = " + str(end_time - start_time) + '\n')



    medium()
