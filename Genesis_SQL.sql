SELECT adverts.category_name
FROM adverts
JOIN costs ON adverts.id = costs.id
GROUP BY adverts.category_name
HAVING AVG(costs.cost) < 500