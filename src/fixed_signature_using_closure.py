from typing import Callable


# このように特定の入出力型の関数を期待されることがあります
def load_filtered_numbers(filter_func: Callable[[int], bool]) -> list[int]:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return list(filter(filter_func, numbers))


# 特定の入出力型の関数の挙動を変えるのに、クロージャを使う例
def build_filter_func(divisor: int) -> Callable[[int], bool]:
    def filter_func(item: int) -> bool:
        return item % divisor == 0

    return filter_func


def main() -> None:
    # 2で割り切れる数をフィルタリング
    divisible_by_2 = build_filter_func(2)
    result = load_filtered_numbers(divisible_by_2)
    print(f"2で割り切れる数: {result}")

    # 3で割り切れる数をフィルタリング
    divisible_by_3 = build_filter_func(3)
    result = load_filtered_numbers(divisible_by_3)
    print(f"3で割り切れる数: {result}")


if __name__ == "__main__":
    main()