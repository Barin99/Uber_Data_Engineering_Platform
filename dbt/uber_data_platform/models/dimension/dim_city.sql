select
    city_id,
    city,
    region,
    state
from {{ source('bronze', 'map_cities') }}
