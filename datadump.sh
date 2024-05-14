# write a bash script that exports all the rows in the sales_data table to a file named sales_data.sql

DB_USER="root"
DB_PASS="1234"
DB_NAME="sales"

# Export the sales_data table
mysqldump -u $DB_USER -p$DB_PASS $DB_NAME sales_data > sales_data.sql