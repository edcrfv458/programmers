select p.product_id, p.product_name, SUM(p.price * o.amount)
from food_product p 
       inner join food_order o 
       on p.PRODUCT_ID = o.PRODUCT_ID
where DATE_FORMAT(o.PRODUCE_DATE, '%m') = '05'
group by 1
order by 3 desc, 1
