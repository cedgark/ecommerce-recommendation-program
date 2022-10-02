# ecommerce-recommendation-program
 This program implements an e-commerce recommendation program based on item-to-item collaborative filtering

Input and Output. The input to the program involves two text files history.txt which contains the purchase history of all the customers and queries.txt which includes all the queries (shopping cart items based on which is needed to provide a recommendation).
The file history.txt is a text file describing the complete purchase history of all the customers. The first line includes three numbers:
Number of Customers Number of Items Number of Transactions
This is followed by Number of Transactions lines of text, each line containing two numbers:
Customer ID Item ID
This means the customer Customer ID bought the item Item ID. Both Customer ID and Item ID are integers starting from 1. Note that the same customer may have bought the same item multiple times.
The file queries.txt is a text file with each line containing a query, describing a list of items in the current shopping cart. Each query is composed of one or more numbers, separated by whitespace, corresponding to the item IDs in the current shopping cart. All the input files described above are assumed to be in the current folder. The program should read from these files in the current folder without any user interaction.

Reading the transaction history. The program reads in all the transactions from history.txt, and builds the customer-item purchase history table where an entry of 1 means the customer has bought the item and 0 otherwise. Prints the total number of non-zero entries (i.e. with a value of 1) in the customer-item purchase history table (“Positive entries: number”).
Precomputing item-to-item angles. The program works out the angles (in degrees) between every pair of items (excluding an item with itself). And then prints the average of all the pairwise angles (“Average angle: average angle”).

Recommendation. For each query (each line in queries.txt), the program does the following:
• Prints the query in a line “Shopping cart: query”.
• For each item Item ID in the query (in the order as it appears), find an item Match ID not in the
current shopping cart which has the minimum angle Min Angle with the item Item ID.
– If Min Angle is less than 90◦, print “Item: Item ID; match: Match ID; angle: Min Angle”.
– Otherwise, no match is accepted, and it simply prints “Item: Item ID no match”.
Note that when multiple items have the same minimum angle, the algorithm can print any one of
these. Each printed item Match ID is considered as a candidate for recommendation.
• The recommendation list is produced by combining all the candidates and ordering them in increasing order of angles. For items which are considered relevant via different shopping cart items, the minimum angle it makes with any item in the shopping cart is used in ranking, and it should only appear in the recommendation list once. If multiple candidates have the same angle, they may appear in arbitrary
order. Print “Recommend: list of recommended items”.
