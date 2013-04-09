use budget;

SELECT 
    CONCAT(Category.name, ' : ',  SubCategory.name) as SCName,
    COUNT(Entry.ID) as num  
FROM 
    Entry LEFT JOIN 
    SubCategory ON Entry.SubCategoryID = SubCategory.ID LEFT JOIN 
    Category ON SubCategory.CategoryID = Category.ID 
GROUP BY 
    SCName 
ORDER BY 
    num DESC;
