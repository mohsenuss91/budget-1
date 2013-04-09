use budget;

SELECT
    CONCAT(YEAR(Entry.operationDate), '-', MONTHNAME(Entry.operationDate)) AS shortDate,
    Category.name,
    -SUM(Entry.value) as sum
FROM
    Entry LEFT JOIN 
    SubCategory ON Entry.SubcategoryID = SubCategory.ID LEFT JOIN
    Category ON SubCategory.CategoryID = Category.ID
WHERE
    value < 0
GROUP BY
    shortDate,
    Category.ID
ORDER BY
   YEAR(Entry.operationDate),
   MONTH(Entry.operationDate)
;