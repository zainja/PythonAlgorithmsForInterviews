def mine_sweeper(bombs, num_rows, num_cols):
    field = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1

        row_range = range(bomb_row - 1, bomb_row + 2) # we will not go to
        # bomb_row +2 because range excludes the end part
        col_range = range(bomb_col - 1, bomb_col + 2)
        for i in row_range:
            current_i = i
            for j in col_range:
                current_j = j
                if 0 <= i < num_rows and 0 <= j < num_cols and field[i][j] \
                        != -1:
                    field[i][j] += 1
    return field


print(mine_sweeper([[0, 0], [1, 2]], 3, 4))
