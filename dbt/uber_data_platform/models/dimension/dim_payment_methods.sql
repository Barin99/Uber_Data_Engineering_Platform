select *
from {{ source('bronze', 'map_payment_methods') }}
