use budget;

SELECT
    CONCAT(YEAR(Entry.operationDate), '-', MONTHNAME(Entry.operationDate)) AS shortDate,
    -SUM(Entry.value) as sum
FROM
    Entry
WHERE
    value < 0
GROUP BY
    shortDate
ORDER BY
   YEAR(Entry.operationDate),
   MONTH(Entry.operationDate)
;