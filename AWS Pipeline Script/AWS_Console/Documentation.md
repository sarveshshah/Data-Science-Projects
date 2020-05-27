# Documenting Data Pipeline Process
## From Raw Data to Finished Dashboards
### Author: Sarvesh Shah | sshah@septa.org

## 1. Overview
The pipeline process consists of 3 parts

1. Where will the RAW data live?
2. Where will the processing occur?
3. Where will the processed Data live?

<li> Retreving data from CPM/CPMS
<li> Copying the data to AWS
    <ul> 
        <li> Maintain a script to write data to a <b>AWS S3 bucket</b>
        <li> Maintain a query/stored procedure to copy data from S3 that is triggered periodically
    </ul>
<li> Writing SQL queries/scripts that can create extracts for Tableau Online/ Tableau Public

## 2.   