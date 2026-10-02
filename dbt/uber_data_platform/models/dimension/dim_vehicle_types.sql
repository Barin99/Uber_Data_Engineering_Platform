select *
from {{ source('bronze', 'map_vehicle_types') }}
