use budget;


SELECT SUM(sum_corr) / COUNT(sum_corr)
FROM
(
SELECT
   CONCAT(SUBSTR(sumEntry.shortDate,1,4), '-', SUBSTR(sumEntry.shortDate,5,2)) as month, 
    sumEntry.sum - IFNULL(SUM(Entry.value/depreciation),0) as sum_corr
FROM
    (SELECT
        date_format(operationDate, '%Y%m') AS shortDate,
        -SUM(Entry.value) as sum
    FROM
        Entry
    WHERE
        value < 0 and depreciation < 2
    GROUP BY
        shortDate
    ORDER BY
       YEAR(Entry.operationDate),
       MONTH(Entry.operationDate)
    ) 
    as sumEntry left join 
    Entry ON Entry.depreciation > 1 and 
             period_diff(sumEntry.shortDate, date_format(Entry.operationDate, '%Y%m')) < Entry.depreciation and
             period_diff(sumEntry.shortDate, date_format(Entry.operationDate, '%Y%m')) >= 0
GROUP BY
  sumEntry.shortDate
) as monthTable;
