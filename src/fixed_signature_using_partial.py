from functools import partial
from typing import Callable


# このように特定の入出力型の関数を期待されることがあります
def load_filtered_numbers(filter_func: Callable[[int], bool]) -> list[int]:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return list(filter(filter_func, numbers))


# 特定の入出力型の関数の挙動を変えるのに、部分適用を使う例
def filter_func(divisor: int, item: int) -> bool:
    return item % divisor == 0


def main() -> None:
    # 2で割り切れる数をフィルタリング
    divisible_by_2 = partial(filter_func, divisor=2)
    result = load_filtered_numbers(divisible_by_2)
    print(f"2で割り切れる数: {result}")

    # 3で割り切れる数をフィルタリング
    divisible_by_3 = partial(filter_func, divisor=3)
    result = load_filtered_numbers(divisible_by_3)
    print(f"3で割り切れる数: {result}")


if __name__ == "__main__":
    main()
