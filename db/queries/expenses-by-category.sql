use budget;

SELECT
    CONCAT(Category.name, ' / ',  SubCategory.name) AS wholeCategory,
    SUM(Entry.value) AS valueSum
FROM 
    Entry LEFT JOIN
    SubCategory ON Entry.SubCategoryID = SubCategory.ID LEFT JOIN
    Category ON SubCategory.CategoryID = Category.ID 
WHERE
    value < 0
GROUP BY
    wholeCategory
ORDER BY
    valueSum;
