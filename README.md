# BTC-LIFO
Calculate profit/loss on BTC sales
ReadMe File
Author: Edward5767
Date: 11 April 2018
Project: LIFO calculator for Bitcoin or Precious metals

History:  Bitcoin is relatively new and there is no hand holding for those who are using it.  It is an experimental currency or savings account type investment.  Maybe even could be considered like a stock.  There can be dividends paid like stocks.  Anyway the IRS is interested in taxing profits if there are any.  Generally we are not provided with a 1099 form at the end of the year.  That being the case, I needed a way to figure out how much profit or loss there was on any sales of the coins.  I decided to use last-in and first-out accounting.

Data File:  The data file is a text document which contains a history of the transactions.  Bitcoin uses 8 decimal points.  This data has 3 items that were available when I wanted to tell my accountant what the sales were.

Date Purchase/sale, Number of BTC, price/proceeds

Each like of this data file needs these 3 items separated by commams.  The data should end with the most recent transaction and should be in chronological order.  If you have characters beyond the end of the transaction data, you will get an error.  This will occur after the script has done its work.  Don't panic over that. (error code 2)

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
ReadMe File
Author: Edward5767
Date: 11 April 2018
Project: LIFO calculator for Bitcoin or Precious metals

History:  Bitcoin is relatively new and there is no hand holding for those who are using it.  It is an experimental currency or savings account type investment.  Maybe even could be considered like a stock.  There can be dividends paid like stocks.  Anyway the IRS is interested in taxing profits if there are any.  Generally we are not provided with a 1099 form at the end of the year.  That being the case, I needed a way to figure out how much profit or loss there was on any sales of the coins.  I decided to use last-in and first-out accounting.

Data File:  The data file is a text document which contains a history of the transactions.  Bitcoin uses 8 decimal points.  This data has 3 items that were available when I wanted to tell my accountant what the sales were.

Date Purchase/sale, Number of BTC, price/proceeds

Each like of this data file needs these 3 items separated by commams.  The data should end with the most recent transaction and should be in chronological order.  If you have characters beyond the end of the transaction data, you will get an error.  This will occur after the script has done its work.  Don't panic over that. (error code 2)

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
This is a quick and dirty utility made for a specific purpose.  I have not filtered the data in any way.  The data input is very important.  Garbage in = garbage out.  I have not tested this in all situations.  I do not guarantee the results.  Feel free to offer suggestions for improvement.  Use at your own risk.  I intend to use a liberal license. 




Residual data file after the program is run:
(This is the list of unsold coins.)

BTC,Transactions,2017
date,number,proceeds
20170103,1.02997999,1051.06


Disclaimer:
This is a quick and dirty utility made for a specific purpose.  I have not filtered the data in any way.  The data input is very important.  Garbage in = garbage out.  I have not tested this in all situations.  I do not guarantee the results.  Feel free to offer suggestions for improvement.  Use at your own risk.  I intend to use a liberal license. 



