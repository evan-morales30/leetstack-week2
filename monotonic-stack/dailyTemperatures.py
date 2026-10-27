def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # stores indices of temperatures

    for index, temperature in enumerate(temperatures):
        # While stack is not empty and current temperature is warmer than the stack's top temp
        while stack and temperature > temperatures[stack[-1]]:
            stack_idx = stack.pop()
            result[stack_idx] = index - stack_idx
        stack.append(index)

    return result


def test_case(name, temperatures, expected):
    actual = dailyTemperatures(temperatures)
    status = "correct" if actual == expected else "incorrect"
    print(f"{name}: {status}")


test_case("Case 1", [73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])
test_case("Case 2", [30, 40, 50, 60], [1, 1, 1, 0])
test_case("Case 3", [30, 60, 90, 40, 50], [1, 1, 0, 1, 0])
