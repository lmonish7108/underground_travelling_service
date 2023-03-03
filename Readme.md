Metro ticketing

Train stations and users with metro card

Fair between each station

Return journey within day 50% off 

Rewards on each return journey 1% of total transaction amount

Senior, Adult, student price fair

All transactions happening will go in json to lambda

Lambda pushes them to kinesis

Kinesis transforms and remove name and email and contact details of person and drops them to s3 bucket

From s3 bucket snowpipe picks it up

In snowflake facts table are created based on 
train station and num of journeys
Journey timings and num of journey
Passenger type and num of journeys


Step 1

Flask + SQLAlchemy container 1

MySQL container 2

Docker

Step 2
Terraform

Lambda
