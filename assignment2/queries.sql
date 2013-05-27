-- a
select count(7) from frequency where docid = '10398_txt_earn';

-- b
select count(term) from frequency where docid = '10398_txt_earn' and count = 1;

-- c union
select count(term) from (select term from frequency where docid = '10398_txt_earn' and count = 1 UNION select term from frequency where docid = '925_txt_trade' and count = 1);
-- or differently
select count( distinct term) from frequency where (docid = '10398_txt_earn' or docid = '925_txt_trade') and count = 1;

-- d Write a SQL statement to count the number of documents containing the word “parliament”
select count(distinct docid) from frequency where term = 'parliament';

-- e Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms. (Hint: You can use the HAVING clause, or you can use a nested query. Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)
select count(7) from (select sum(count) as word_sum from frequency group by docid) where word_sum > 300;

-- f Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'. 
select count(7) from (select distinct docid from frequency where term = 'transactions' INTERSECT select distinct docid from frequency where term = 'world');
-- or with a join
select count(7) from (select distinct docid from frequency where term = 'transactions') f1 INNER JOIN (select distinct docid from frequency f2 where term = 'world') f2 ON f1.docid = f2.docid;


--g matrix multiplication
select A.row_num, B.col_num, sum(A.value*B.value) from A JOIN B ON B.row_num = A.col_num group by A.row_num, B.col_num;

-- h similarity matrix
-- in general
select A.docid, B.docid, sum(A.count*B.count) from frequency A JOIN frequency B ON A.term = B.term where A.docid < B.docid group by A.docid, B.docid;
-- for the homework
select A.docid, B.docid, sum(A.count*B.count) from frequency A JOIN frequency B ON A.term = B.term where A.docid = '10080_txt_crude' and B.docid = '17035_txt_earn' group by A.docid, B.docid;


-- g keyword search  Find the best matching document to the keyword query "washington taxes treasury".
select A.docid, B.docid, sum(A.count*B.count) siml
from frequency A JOIN 
    (SELECT 'q' as docid, 'washington' as term, 1 as count 
    UNION
    SELECT 'q' as docid, 'taxes' as term, 1 as count
    UNION 
    SELECT 'q' as docid, 'treasury' as term, 1 as count) B 
    ON A.term = B.term 
where B.docid = 'q' 
group by A.docid, B.docid
order by siml;



