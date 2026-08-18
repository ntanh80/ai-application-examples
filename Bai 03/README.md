# Prime Number Utilities

Module này cung cấp các hàm tiện ích để kiểm tra số nguyên tố và tính tổng các số nguyên tố trong một danh sách số nguyên.

## Functions

### `is_prime(n: int) -> bool`

Kiểm tra một số nguyên có phải là số nguyên tố hay không.

Một số nguyên tố là số nguyên lớn hơn 1 và chỉ chia hết cho 1 và chính nó.

#### Parameters

- `n` (`int`): Số nguyên cần kiểm tra.

#### Returns

- `bool`: Trả về `True` nếu `n` là số nguyên tố, ngược lại trả về `False`.

#### Raises

- `ValueError`: Nếu `n` không phải là số nguyên.

#### Example

```python
is_prime(2)
# True

is_prime(10)
# False

is_prime(17)
# True
```

### `sum_of_primes(numbers: list[int]) -> int`

Tính tổng tất cả các số nguyên tố trong một danh sách số nguyên.

Hàm sẽ kiểm tra dữ liệu đầu vào trước khi tính tổng. Đầu vào phải là một danh sách, và mọi phần tử trong danh sách phải là số nguyên.

#### Parameters

- `numbers` (`list[int]`): Danh sách các số nguyên cần kiểm tra.

#### Returns

- `int`: Tổng các số nguyên tố có trong danh sách.

#### Raises

- `TypeError`: Nếu `numbers` không phải là danh sách.
- `ValueError`: Nếu có phần tử trong `numbers` không phải là số nguyên.

#### Example

```python
sum_of_primes([1, 2, 3, 4, 5, 10])
# 10

sum_of_primes([4, 6, 8])
# 0
```

## Usage

```python
numbers = [1, 2, 3, 4, 5, 10, 11]

total = sum_of_primes(numbers)

print(total)
# 21
```

## Notes

- Các số nhỏ hơn hoặc bằng 1 không được xem là số nguyên tố.
- Số 2 là số nguyên tố chẵn duy nhất.
- Hàm `sum_of_primes` sử dụng `is_prime` để kiểm tra từng phần tử trong danh sách.
