# Customer Analytics for Business
---

This is the outcome of the Udemy Course *Customer Analytics for Business* from *The Click Reader*.
The course aimed to work with a transactional customer data, analysis on data to find insights for acquiring, retaining, and growing your customer base.


## Goals :snake: :dart: :bar_chart: :moneybag:

The approach and goals are as follows:
- Identify what kind of data to collect and from which sources along with the best practices
- Gain an understanding on how we can analyze such data using various statistical and graphical methods
- Make better decisions as a business by profiling and segmenting our customers using a programmatic approach using RFM (recency, frequency, and monetary value) metrics.
- Learn about STP framework (segmenting, targeting, and positioning), in order to help you acquire, retain and grow your customer base.


## Dataset :floppy_disk:

The dataset contains 541908 instances of customer transactions with 5 attributes:

- **CustomerID**: Unique ID assigned to each customer
- **InvoiceNo**: Unique number assigned for each invoice 
- **AmountSpent**: Amount spent by the customer
- **InvoiceDate**: Date of transaction
- **Country**: Name of the country where the order was placed

## Business Problem :briefcase: :rocket:

Over marketing context, mass marketing tretas all customers as one group, whereas one-to-one marketing focuses on one customer at a time. Target marketing involves directing marketing activities to those customers that are most likely to buy, and lies between both.

Approaching the STP framework, we have the segmenting (i.e. divide market into distinct groups of customers), targeting (select most attractive segments to focus your marketing on), and positioning (determine how to position your product for each target segment).

As presented in [1], the variables that go into segmentation should be easily available or accessible, avoiding variables that are difficult to measure. In this case, as we have only transactional variables, only these variables will be applied in the analytics.

So in order to follow the framework, one must start with segmenting. Traditional models, such as *RFM models*, consider the customer recency (data of most recent purchase), frequency (number of purchases), and monetary value (sales revenue) of previous purchases, which were used here as explanatory variables for segmentation. 

The segments can be identified with different sets of variables, such as geographic (e.g. region, country, population), demographic (e.g. gender, age, education), psychographic (e.g. lifestyle, personality, interest), and behavioral (e.g. user status, brand loyalty) characteristics. Here, the previous results from RFM models were used, as no other characteristics from the customers were available to be implemented in the clustering. This approach is called *post hoc* segmentation, were one uses variables/characteristics of customers to segmentation i.e. data-based. Here, is important to comment that the number of clusters was arbitrarily chosen, which is not the best approach (the best situation would be perform a silhouette coefficient analysis).

Based on clustering results, the customers were segmented into low-value, mid-value, and high-value, and future marketing can be directed to each of the segments.


References: [1] Miller, T. W. Marketing Data Science: Modeling Techniques in Predictive Analytics with R and Python.



