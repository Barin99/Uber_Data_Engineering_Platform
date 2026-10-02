select *
from {{ source('bronze', 'map_vehicle_makes') }}
