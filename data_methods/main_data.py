import cython

from data_methods.methods.compiled_jit import JitCompile
from data_methods.methods.current_method import CurrentMethod
from data_methods.methods.cython_method import CythonMethod
from data_methods.methods.function_vectorise import VectoriseFunction
from data_methods.methods.parallel_map import ParallelMap


def run_app():
    large_size=10000
    # 10,000 = 2.1080s
    # 100,000 = 8.8982s
    # 1,000,000 = 76.0185s
    # JitCompile(large_size=large_size).run_transformation2()

    # 10,000 = 3.2101s
    # 100,000 = 7.0964s
    # 1,000,000 = 48.3064s
    # 8,000,000 = 388.1569s
    a_match_count = ParallelMap(large_size=large_size).run_transformation1()

    # 10,000 = 2.3090s
    # 100,000 = 22.9494s
    # CurrentMethod(large_size=large_size).run_transformation1()

    # 10,000 = 2.3133s
    # 100,000 = 23.2184s
    # VectoriseFunction(large_size=large_size).run_transformation1()

    # 10,000 = 2.1382s
    # 100,000 = 21.4323s
    # if cython.compiled:
    #     print("Running as cython")
    # else:
    #     print("Running as python")
    # CythonMethod(large_size=large_size).run_transformation1()

    print("bye")


if __name__ == '__main__':
    run_app()