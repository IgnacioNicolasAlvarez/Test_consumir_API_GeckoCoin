create table coinhistory_per_month_max_min as
select id_coin,
    extract(
        year
        from date_added
    ) as year,
    extract(
        month
        from date_added
    ) as month,
    max(current_price_usd) as max_price_usd,
    min(current_price_usd) as min_price_usd
from coinhistory
group by id_coin,
    extract(
        year
        from date_added
    ),
    extract(
        month
        from date_added
    );