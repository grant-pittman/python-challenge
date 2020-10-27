# Py Me Up, Charlie - A Python Challenge <!-- omit in toc -->

## Table of contents <!-- omit in toc -->
- [Background](#background)
- [PyBank](#pybank)
  - [Instructions](#instructions)
  - [Results](#results)
- [PyPoll](#pypoll)
  - [Instructions](#instructions-1)
  - [Results](#results-1)


## Background

Included in this repo are two challenges to demonstrate my skills in Python scripting. Both  challenges encompass a real-world situation where these skills come in handy.


## PyBank

### Instructions

In this challenge, I am tasked to create a Python script for analyzig the financial records of my company. 

I am provided a csv dataset with with two columns: `Date` and `Profit/Losses`.

For the assignment I created a Python script that analyzes the records to calculate each of the following:

 - Total number of months included in the dataset

 - The net total amount of "Profit" and "Losses" over the entire period.

 - The average of the changes in "Profit" and "Losses" over the entire period.

 - The greatest increase in profits (date and amount) over the entire period.

 - The greatest decrease in losses (date and amount) over the entire period.

### Results

Here are the results from my effort:

```text
Financial Analysis
 ----------------------------
Total Months: 86
Total Revenue: $38,382,578.00
Average Revenue Change: $-2,315.12
Greatest Increase in Profits: Feb-2012 $1,926,159.00
Greatest Decrease in Profits: Sep-2013 $-2,196,167.00
```

## PyPoll

### Instructions

In this challenge, I am tasked with helping a small, rural town modernize its vote-counting process.

I was given a csv dataset with three columns: `Voter Id`, `County` and `Candidate`.  My task is to create a Python script that analyzes the votes and calculates each of the following:

 - The total number of votes cast

 - A complete list of candidates who received votes

 - The percentage of votes each candidate won.

 - The total number of votes each candidate won

 - The winner of the election based on the popular vote.

### Results

Here are the results that I found:

```text
Election Results
-------------------------
Total Votes: 3,521,001
-------------------------
Khan: 63.000% (2,218,231)
Correy: 20.000% (704,200)
Li: 14.000% (492,940)
O'Tooley: 3.000% (105,630)
-------------------------
Winner:  Khan
-------------------------
```

