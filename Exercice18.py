############ EXERCICE 18 ############


"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


def maximum_path_sum_I(max_line):
    """

    :param max_line:
    :return:
    """
    triangle = "75 \
                 95 64 \
                 17 47 82 \
                 18 35 87 10 \
                 20 04 82 47 65 \
                 19 01 23 75 03 34 \
                 88 02 77 73 07 63 67 \
                 99 65 04 28 06 16 70 92 \
                 41 41 26 56 83 40 80 70 33 \
                 41 48 72 33 47 32 37 16 94 29 \
                 53 71 44 65 25 43 91 52 97 51 14 \
                 70 11 33 28 77 73 17 78 39 68 17 57 \
                 91 71 52 38 17 14 91 43 58 50 27 29 48 \
                 63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
                 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
    triangle_list = [int(d) for d in triangle.split()]
    penultimate_line_first_index = 0
    # get the index of the first number of the penultimate line
    for i in range(1, max_line - 1):
        penultimate_line_first_index += i
    index = penultimate_line_first_index
    line_index = max_line - 1
    for j in range(1, max_line):
        for i in range(line_index):
            if triangle_list[index + i] + triangle_list[index + i + line_index] > triangle_list[index + i] + \
                    triangle_list[index + i + (line_index + 1)]:
                triangle_list[index + i] = triangle_list[index + i] + triangle_list[index + i + line_index]
            else:
                triangle_list[index + i] = triangle_list[index + i] + triangle_list[index + i + (line_index + 1)]
            # print(triangle_list[index+i])
        index -= (line_index - 1)
        line_index -= 1
    return triangle_list[0]
