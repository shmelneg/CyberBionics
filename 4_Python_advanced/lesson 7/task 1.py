from typing import List


def main():
    test_input = [1, 2, 14, -5, 64, 0]
    print(f'The initial list is: {test_input}')
    print(f'The type of the elements in the list above is: {type(test_input[0])}')

    result = convert(test_input)
    print(f'The result list is: {result}')
    print(f'The type of the elements in the list above is: {type(result[0])}')


def convert(lst_int: List[int]) -> List[str]:
    lst_str = []
    for i in lst_int:
        lst_str.append(str(i))
    return lst_str

if __name__ == "__main__":
    main()
