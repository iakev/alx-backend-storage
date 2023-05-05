-- script that lists all bands with Glam rock as the main style, rankde by longevity
-- Making a query with band_name and lifespan in years.
SELECT band_name, IF(ISNULL(split),YEAR(NOW()),split)- formed AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
