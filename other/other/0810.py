class Solution:
    def floodFill(self, image, sr, sc, newColor):
        row = len(image)
        col = len(image[0])

        move_pos = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        color = image[sr][sc]

        vis = [[0] * col for _ in range(row)]
        queue = [(sr, sc)]

        while queue:
            temp = queue.pop(0)
            vis[temp[0]][temp[1]] = 1
            image[temp[0]][temp[1]] = newColor

            for i in move_pos:
                x_index = temp[0] + i[0]
                y_index = temp[1] + i[1]

                if x_index >= 0 and y_index >= 0 and x_index < row and y_index < col and not vis[x_index][y_index] and \
                        image[x_index][y_index] == color:
                    queue.append((x_index, y_index))
                    vis[x_index][y_index] = 1
                    image[x_index][y_index] = newColor
        return image


if __name__ == '__main__':
    print(Solution().floodFill(
        [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
        1,
        1,
        2
    ))
