# BTC-LIFO
Calculate profit/loss on BTC sales
ReadMe File
Author: Edward5767
Date: 11 April 2018
Project: LIFO calculator for Bitcoin or Precious metals

History:

Bitcoin is relatively new and there is no hand holding for those who are using it.  It is an experimental currency or savings account type investment.  Maybe even could be considered like a stock.  There can be dividends paid like stocks.  Anyway the IRS is interested in taxing profits if there are any.  Generally we are not provided with a 1099 form at the end of the year.  That being the case, I needed a way to figure out how much profit or loss there was on any sales of the coins.  I decided to use last-in and first-out accounting.

Data File: 

The data file is a text document which contains a history of the transactions.  Bitcoin uses 8 decimal points.  This data has 3 items that were available when I wanted to tell my accountant what the sales were.

Date Purchase/sale, Number of BTC, price/proceeds

Each line of this data file needs these 3 items separated by commams.  The data should end with the most recent transaction and should be in chronological order.  If you have characters beyond the end of the transaction data, you will get an error.  This will occur after the script has done its work.  Don't panic over that. (error code 2)

Of course, you cannot sell BTC that you have not first purchased.  That means that you should not run out of BTC to sell at any time.  The data file will show the remaining unsold BTC when the script finishes and it will write out a CSV file containing the transaction data.  If a sale of coins is more than the most recent purchase, the script will divide the sale into pieces coinciding with the different lots being sold.

You may alter the name of the data file: test.txt 
You may alter the name of the output file: test.csv
The precision is set to 8 by default for bitcoin but this number may be changed also.

I have tested this script with Gold and Silver as well and Alt-coins.  These behave in a similar fashion to BTC.

I like to put two header lines at the top of the data file.  Note: no $ signs, no commas in the prices, and date in 8 digit format YYYYMMDD. Commas delimit the data items.  2 commas per line.  Errors in the format of the data produce errors by the script.  The program needs the - sign to indicate sales of coins.  

Example Data file based on historial prices:  

BTC,Transactions,2017

date,number,proceeds

20170103,3.00000000,3061.41

20170115,2.00000000,1634.52

20170310,-1.01002000,-1213.90

20170403,-.55600000,-631.16

20170429,-1.40400001,-1876.99

20170801,-1.00000000,-2787.85




Program Output:

Sale	   Number	proceeds  buy	     basis	profit	gain

20170310   -1.01002000	-1213.9	  20170115   825.45	388.45	S

20170403   -0.55600000	-631.16	  20170115   454.4	176.76	S

20170429   -0.43398000	-580.18	  20170115   354.67	225.51	S

20170429   -0.97002001	-1296.81  20170103   989.88	306.93	S

20170801   -1.00000000	-2787.85  20170103   1020.47	1767.38	S


Residual data file after the program is run:

(This is the list of unsold coins.)


BTC,Transactions,2017

date,number,proceeds

20170103,1.02997999,1051.06



Disclaimer:

This is a quick and dirty utility made for a specific purpose.  I have not filtered the data in any way.  The data input is very important.  Garbage in = garbage out.  I have not tested this in all situations.  I do not guarantee the results.  Feel free to offer suggestions for improvement.  Use at your own risk.  I intend to use a liberal license.  I do not promise to continuously improve this program.

Changes added: Copy datafile to a work.tmp file.  This enabled me to remove empty lines from the data.  This change leaves the datafile unchanged by the program.  Also the work.tmp file is removed when the script finishes.  The program will not otherwise format the data.  Each transaction is 3 pieces of data: date,number,price.  Sales are negative and buys are positive.  Sequence needs to be chronological (for LIFO accounting) with buys before sales as you can't sell BTC that you don't own. 

4 August 2018:  Added a few command line parameters.  -h, --help and -H will show help.    -3 (values of 3 to 8) are the precision of the calculations.  You may specify the name of the data file.  The default datafile name is test.txt  The default precision is 8 decimal points.  

Example:
python B2018.py datafile.txt 
python B2018.py -h
python B2018.py datafile -4

If you want to change the type of accounting, you need to change the order of the data.  For FIFO (first in - first out) the data should have all the buy data first in reverse order of most recent date to the earliest date.  This buy data is then followed by the sell data also in the same order of most recent to earliest.  
Specific Coin sales may be handled individually.  Place the buy data first followed by the sell data.  The output will show you the remaining unsold coin data and then you will need to edit your spreadsheet to include the changes.  
To incorporate a parameter to set the type of accounting without altering the data input would require the data to be sorted in a temporary data file before the program runs.  This might be done in the future as it would be more user friendly.  This might be done for FIFO accounting.  Specific coin identification needs to be done on an ongoing basis and not at the end of the year when you are thinking about tax reporting.
 
8 August 2018:  
python B2019.py datafile.txt -F         ( change data from chronological to FIFO order -F or -f )   
This option will filter the data to group the buys and sells together and reverse the order of them from recent to past for FIFO accounting.  The original datafile is unchanged.

10 Dec 2019:
Transactions can involve sale of coins that were purchased on multiple dates.  These partial transactions should add up to the correct number of coins along with a total price and total net value.  These figures are added to the printout at the appropriate places.




