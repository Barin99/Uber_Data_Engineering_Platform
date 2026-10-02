select *
from {{ source('bronze', 'map_cancellation_reasons') }}
