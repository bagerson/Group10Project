# Group10Project
Columbia Data Group Project: Ben, Ming, Vicky, Mo

### Goals

This project was an exploratory analysis to determine if stock market indexes (such as the DJIA) can predict changes in housing prices (HPI).

### Results

As described in the class presentation, we determined a weak, positive correlation nationwide between stock market indexes and HPI.  The exception being the Mid-Atlantic Division where HPI was inversely correlated with stock market indexes.

However, even showing a correlation, we could not reject the null hypothesis because the P-values for each region exceeded 0.05.  

Thus, while some correlation exists, it is impossible to draw a conclusion about causation.

Ultimately this project served as an important exploratory analysis which points to future avenues for data analysis.  Particularly: examining how time-series changes occur between indexes, and exploring geographic data at a more granular level.

### Discussion

This project recognized in the early stages that other factors, such as the Federal Reserve rate, or prime interest rate, may serve as an intermediate measure which "bridges" stock market indices and HPI.  For example, and change in the stock market may trigger the Federal Reserve to change rates, to stimulate or slow growth, which may in turn affect borrowing for home mortgages and thus demand.

In addition, the HPI data published by the Federal Government is a very rich dataset which allows for a very granular analysis of regional housing prices.  Analyzing small areas may reveal trends where the HPI is more closely linked to the stock market indices.

Group 10 approached this questions with an open mind to find out what the data revealed.  We approached the problem in a true "experimental" fashion to ensure that our results did not suffer from a bias.  We input the data to a known analysis and examined the results.  The conclusions were fruitful in that they revealed several more avenues for investigation which may in turn reveal hidden trends in the data.

### Methods

The data sets used in this project came from two sources. The HPI, and several stock market indice (DJIA, S&P500, Nasdaq..).  Ming, Mo, and Vicky tackled the cleaning and parsing of the stock market indexes.  Ben handled the HPI data.  As discussed in the class presentation overlapping data was limited to 2009-2019, although the data sets were in fact larger.  The HPI data set also included a large variety of geographic data.  Data was cleaned for the appropriate range, and the units (percent change per month) were calculated for extracted from each data set.  The stock market indices required date parsing to ensure correct indexing.

The result was several matching datasets which described a percent change per month, per geographic area.  

Version control was accomplished by having each team member code in their own repository branch.  Ming was appointed to oversee the final merge.  Output of the HPI cleaning code was written to .CSV files which were then re-imported into the Main branch final code.  The decision for this was that the ultimate code did not need to include a lengthy function for cleaning data.  Because only the .CSV files were passed to the master branch, the original code generating it is still in the individual team member's branch.


 

