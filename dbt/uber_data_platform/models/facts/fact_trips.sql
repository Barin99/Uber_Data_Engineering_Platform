select

    ride_id,

    passenger_id,
    passenger_name,

    driver_id,
    driver_name,

    pickup_timestamp,
    dropoff_timestamp,
    booking_timestamp,

    pickup_city_id,
    dropoff_city_id,

    vehicle_make_id,
    vehicle_type_id,

    payment_method_id,
    ride_status_id,
    cancellation_reason_id,

    distance_miles,
    duration_minutes,

    base_fare,
    distance_fare,
    time_fare,
    subtotal,
    tip_amount,
    total_fare,

    surge_multiplier

from {{ ref('stg_trips') }}
