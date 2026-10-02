select *
from {{ source('bronze', 'map_ride_statuses') }}
