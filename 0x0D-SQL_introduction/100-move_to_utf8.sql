-- This script updates the db, table and a field to utf-8

-- switch database
USE `hbtn_0c_0`
-- convert table to utf-8
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
