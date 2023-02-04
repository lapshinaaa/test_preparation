#include <iostream>

int calculateNegative(int *arr, int sizeOfArray)
{
    int counter = 0;

    for (int i = 0; i < sizeOfArray; ++i) {
        if (arr[i] < 0) counter++;
    }

    return counter;

}


int main()
{

    int **array;
    int rows = 0;
    int columns = 0;
    int counter_negative = 0;

    std::cin>>rows;
    std::cin>>columns;

    //Dynamically allocating rows space in heap
    array = new int*[rows];
    //Dynamically allocating column space in heap
    for(int i = 0; i < rows; i++){
        array[i] = new int[columns];
    }

    //Taking input in the array
    for(int i = 0; i < rows; i++)
    {
        for(int j = 0; j < columns; j++)
        {
            std::cin >> array[i][j];
        }
    }

    for (int i = 0; i < rows; ++i) {
        counter_negative += calculateNegative(array[i], columns);
    }

    std::cout<<counter_negative;


    return 0;
}