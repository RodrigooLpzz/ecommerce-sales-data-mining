Homework #1 - Week 4

In this homework, I am working with a dataset that contains 50,000 rows. This exceeds the minimum requirement of 5,000, but I decided to work with the full dataset instead of a sample because my machine handles it well and it allows for a more robust cleaning and analysis.

My process:

    Initial Preview: I started by checking general info, like the number of rows and the data type of each column.

    Null Validation: I checked for standard null fields and also for different types of "hidden" nulls in the object columns. Since the dataset is from Kaggle it was mostly clean but I wanted to be sure.

    Date Conversion: I noticed that order_date was a string. I changed it to datetime because I know that leaving it as a string could be a problem for future homeworks.

    Specific Rules: Finally, I checked for specific logic:

        No negative values in numeric columns.

        Ratings must be in the 0-5 range.

        Discount percent must be between 0 and 100.

I learned a lot with this assignment. I didn't remember much about how to use Pandas to clean a dataset so this was a great way to refresh my memory and practice