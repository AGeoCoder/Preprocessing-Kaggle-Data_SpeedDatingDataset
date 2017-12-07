# -*- coding: utf-8 -*-
import csv
import random

# Author: "AGéocoder"
#
# A short preprocessing script to divide a dataset (CSV format) into a 
# training set CSV and a test set CSV for use with machine learning algorithms.
# The original dataset with speed dating experiment information was downloaded 
# from Kaggle.
# (https://www.kaggle.com/annavictoria/speed-dating-experiment)
# It had 8378 rows and about 195 columns.
#
#==========================================================================
#1) Let's gather data about the original test set.

numberOfRow = 0 #number of the row in the original dataset
number_of_no_matches = 0 #number of couples that were not a match
number_of_matches = 0 #number of couples that were a match
list_Of_Row_Numbers_of_No_Matches = [] #list of the rows that were a match
list_Of_Row_Numbers_of_Matches = [] #list of the rows that were not a match

#this opens the csv file with 'rU' because there was otherwise an error
#with the large csv file
original_file_location = 'C:\\code\\DatingData.csv'
data = open(original_file_location, 'rU') #the original data set
with data as aFile:
    csvReader = csv.reader(aFile)
    for row in csvReader:          #for every row in the dataset
        numberOfRow += 1            
        try:
            matchNumber = int(row[12]) #column 12 is 0 for no match, 1 for match
            #if it is not a match
            if (matchNumber == 0):
                number_of_no_matches += 1
                list_Of_Row_Numbers_of_No_Matches.append(numberOfRow)
            #if it is a match
            elif (matchNumber == 1):
                number_of_matches += 1
                list_Of_Row_Numbers_of_Matches.append(numberOfRow)
            else:
                print "Error, match number other than 0 or 1."
        except ValueError:
            pass
    
    print "=================================="
    print "Original data set information: "
    print "Input file location: " + original_file_location
    print
    total_number_of_data_rows = number_of_no_matches + number_of_matches
    total_number_of_data_rows_string = str(total_number_of_data_rows)
    print "Total number of data rows in original dataset is: " + total_number_of_data_rows_string
    print
    print "Number of no matches in original dataset is: " + str(number_of_no_matches)
    print "Number of matches in original dataset is: " + str(number_of_matches)
    
    #==========================================================================
    #2) Now that we have the basic information about the original data set, 
    #let's create the test set and training set.
    
    #The original dataset has 8378 rows. Using an 85%/15% training set and test
    #set distribution, we select 628 from the set of no matches and 
    #628 from the set of matches in order to make the test set comprised
    #of 50/50 no matches and matches.
    SAMPLE_NUMBER = 628
    list_of_random_no_match_rows = random.sample(list_Of_Row_Numbers_of_No_Matches, SAMPLE_NUMBER)
    list_of_random_no_match_rows.sort()
    
    list_of_random_match_rows = random.sample(list_Of_Row_Numbers_of_Matches, SAMPLE_NUMBER)
    list_of_random_match_rows.sort()    
 
    #===========================================================================
    #go through the CSV file again and create the test set by randomly selecting
    #the SAMPLE_NUMBER of matches and SAMPLE_NUMBER of no matches for a 50/50
    #test set,
    #and the training set will be comprised of all leftover rows
    
    number_of_no_matches_in_test_set = 0 #reset the number of no matches
    number_of_matches_in_test_set = 0    #reset the number of matches
    number_of_rows_in_training_set = 0

    data.seek(0) #reset the CSV iterator
    numberOfRow = 0 #reset the number of rows
    
    output_file_testSet_location = 'C:\\code\\TestSet.csv'
    output_File_Test_Set = open(output_file_testSet_location, "wb")
    writer1 = csv.writer(output_File_Test_Set, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    
    output_file_trainingSet_location = 'C:\\code\\TrainingSet.csv'
    output_File_Training_Set = open(output_file_trainingSet_location, "wb")
    writer2 = csv.writer(output_File_Training_Set, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    
    #this time when we go through the original file we will pick random samples
    #for our test set csv, and put the rest of the rows in the training set csv
    for row in csvReader:
        numberOfRow += 1
        try:
            matchNumber = int(row[12])
            if numberOfRow in list_of_random_no_match_rows:
                writer1.writerow(row)
                number_of_no_matches_in_test_set += 1
            elif numberOfRow in list_of_random_match_rows:
                writer1.writerow(row)
                number_of_matches_in_test_set += 1
            else:
                writer2.writerow(row)
                number_of_rows_in_training_set += 1
        except ValueError:
            #this should only happen with the first line with column headers
            writer1.writerow(row)
            writer2.writerow(row)
             
    #print information about the test set
    print "=================================="
    num_rows_in_test_set = number_of_no_matches_in_test_set + number_of_matches_in_test_set
    num_rows_in_test_set_string = str(num_rows_in_test_set)
    test_set_percent = num_rows_in_test_set*100.0/total_number_of_data_rows
    print "Test set information: "
    print "Output file location: " + output_file_testSet_location
    print
    print("Percentage of original data set, test set: %.2f%%" % test_set_percent)
    print "Total number of data rows in test set: " + num_rows_in_test_set_string
    print
    print "Number of no matches in test set: " + str(number_of_no_matches_in_test_set)
    print "Number of matches in test set: " + str(number_of_matches_in_test_set)
    
    #print information about the training set
    print "=================================="
    training_set_percent = number_of_rows_in_training_set*100.0/total_number_of_data_rows
    print "Training set information: "
    print "Output file location: " + output_file_trainingSet_location
    print
    print("Percentage of original data set, training set: %.2f%%" % training_set_percent)
    print "Total number of rows in training set: " + str(number_of_rows_in_training_set)
    print
    print "Number of no matches in training set: " + str(number_of_no_matches - number_of_no_matches_in_test_set)
    print "Number of matches in training set: " + str(number_of_matches - number_of_matches_in_test_set)
    print "=================================="
    
    data.close()
    output_File_Test_Set.close()
    output_File_Training_Set.close()