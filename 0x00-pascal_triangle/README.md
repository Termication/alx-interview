# Introduction

Pascal's Triangle is a triangular array of binomial coefficients. The nth row contains the coefficients of the binomial expansion of (x + y)^(n-1). Each element in the triangle is the sum of the two elements directly above it.

This function returns Pascal’s triangle up to the given number of rows n. If n <= 0, it returns an empty list.

## How Pascal's Triangle Works

Pascal’s triangle starts with a single 1 at the top. Each subsequent row starts and ends with 1, and every other element is the sum of the two elements directly above it. For example:

#### markdown

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Each row n contains n + 1 elements.
## Algorithm Explanation

    Base Case:
        If n <= 0, return an empty list.
        Otherwise, start with the first row of Pascal’s triangle, which is [1].

    Iterate through each row:
        For each new row, start with 1.
        Calculate the inner elements as the sum of two elements from the previous row.
        End each row with 1.

    Repeat until all rows are constructed.
