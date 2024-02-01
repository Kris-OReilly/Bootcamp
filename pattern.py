# iterate printing '*' in increasing number up to 5 and then back to 1 using a single for loop.
# the iteration will perform 9 times 1,2,3,4,5,4,3,2,1


for i in range(1, 10):  # loop to iterate 9 times starting at 1

    if i <= 5:  # the if statement allows the loop to print from 1 star to 5 stars
        print(i * '*') 
    else:
        print((10 - i) * '*') # prints the number of stars descending from iteration 6 onwards
                              # e.g. (10-6) = 4 * '*' which will print ****

