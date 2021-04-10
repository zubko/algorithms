# dynamic programming algorithm
# src: Algorithms in a Nutshell, 2nd ed

REPLACE = 0
REMOVE = 1
INSERT = 2

def min_edit_distance(str1, str2):
    """Compute minimum edit distance converting str1 to str2"""
    len1 = len(str1)
    len2 = len(str2)

    # prepare 2-dimensional data structure
    m = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]
    op = [[-1 for j in range(len2 + 1)] for i in range(len1 + 1)]

    # setup initial costs
    for i in range(1, len1 + 1):
        m[i][0] = i
    for j in range(1, len2 + 1):
        m[0][j] = j

    # compute best
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if str1[i - 1] == str2[j - 1] else 1
            replace_cost = m[i - 1][j - 1] + cost
            remove_cost = m[i - 1][j] + 1
            insert_cost = m[i][j - 1] + 1
            costs = [replace_cost, remove_cost, insert_cost]
            m[i][j] = min(replace_cost, remove_cost, insert_cost)
            op[i][j] = costs.index(m[i][j])

    return m[len1][len2], m, op


def trace_steps(str1, str2, m, op):
    """trace back the steps"""
    ops = []
    i = len(str1)
    j = len(str2)
    while i != 0 or j != 0:
        if op[i][j] == REMOVE or j == 0:
            ops.append('remove {}-th char {} of {}'.format(i, str1[i - 1], str1))
            i = i - 1
        elif op[i][j] == INSERT or i == 0:
            ops.append('insert {}-th char {} of {}'.format(j, str2[j - 1], str2))
            j = j - 1
        else:
            if m[i - 1][j - 1] < m[i][j]:
                fmt = 'replace {}-th char of {} ({}) with {}'
                ops.append(fmt.format(i, str1, str1[i - 1], str2[j - 1]))
            i, j = i - 1, j - 1
    return ops


def test(str1, str2):
    """Run the test case and print the results"""
    min_distance, matrix, operations = min_edit_distance(str1, str2)

    print("{0} -> {1}: {2} operations:".format(str1, str2, min_distance))

    steps = trace_steps(str1, str2, matrix, operations)
    for i in range(len(steps)):
        print("   " + steps[i])

    line = "   ∅ "
    for j in range(len(str2)):
        line += str2[j] + " "
    print(line)
    for i in range(len(matrix)):
        line = f"{str1[i-1] if i > 0 else '∅'}: "
        for j in range(len(matrix[0])):
            line += str(matrix[i][j]) + " "
        print(line)
    print('--------------')


test("GCTAC", "CTCA")
test("CTCAC", "CTCA")
test("CTCAC", "CGCGAC")
test("ABCD", "EFGH")
test("ABCD", "ABCD")
test("hello world hello world", "big world world")
