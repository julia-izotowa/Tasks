"""
Find the maximum depth of the mountain lakes
"""


def find_depth(relief):
    max_height = relief[0]
    min_height = relief[0]
    depth = []
    for height in relief:
        if height >= max_height:
            if max_height != min_height:
                depth.append(max_height - min_height)
            max_height = height
            min_height = height
        if height <= min_height:
            min_height = height

    return max(depth)


if __name__ == "__main__":
    print(find_depth((1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 8, 8, 2)))
    print(find_depth((1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 6, 4, 3, 2, 1, 0, 1, 2, 3, 4, 7)))
