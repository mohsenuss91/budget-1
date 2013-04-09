use budget;

SELECT
    (365.25/12)*(-SUM(Entry.value) /  DATEDIFF(MAX(Entry.operationDate) , MIN(Entry.operationDate) ) )
FROM
    Entry
WHERE 
    value < 0 and value > -2000 and operationDate < '2013-04-01';

