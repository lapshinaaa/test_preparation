#include <iostream>

int sumMainDiagonal(int **arr, int rows, int columns)
{
    int sum = 0;

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < columns; ++j) {
            if (i == j) sum += arr[i][j];
        }
    }

    return sum;

}
