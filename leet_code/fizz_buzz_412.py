from typing import List


def fizz_buzz(n: int) -> List[str]:
    count = 1
    output = []
    while count <= n:
        if count % 3 == 0 and count % 5 == 0:
            output.append("FizzBuzz")
        elif count % 3 == 0:
            output.append("Fizz")
        elif count % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(count))
        count += 1
    return output
