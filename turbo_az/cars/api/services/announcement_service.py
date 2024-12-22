from ...models import Announcement, CarSupply


def create_announcement(
    *,
    user,
    brand,
    car_model,
    roof_type,
    color,
    fuel_type,
    engine_capacity,
    for_country,
    gearbox,
    car_supply,
    mileage_type,
    currency_type,
    owner_type,
    transmission_type,
    seat_count,
    is_crashed,
    is_damaged,
    is_colored,
    with_credit,
    barter,
    mileage,
    price,
    released_date,
    engine_power,
    vin_code,
    info
) -> Announcement:
    obj = Announcement.objects.create(
        user=user,
        brand=brand,
        car_model=car_model,
        roof_type=roof_type,
        color=color,
        fuel_type=fuel_type,
        engine_capacity=engine_capacity,
        for_country=for_country,
        gearbox=gearbox,
        mileage_type=mileage_type,
        currency_type=currency_type,
        owner_type=owner_type,
        transmission_type=transmission_type,
        seat_count=seat_count,
        is_crashed=is_crashed,
        is_damaged=is_damaged,
        is_colored=is_colored,
        with_credit=with_credit,
        barter=barter,
        mileage=mileage,
        price=price,
        released_date=released_date,
        engine_power=engine_power,
        vin_code=vin_code,
        info=info
    )

    obj.car_supply.set(car_supply) # .set m2m əlaqədə verilmiş məlumatları obyektə əlavə edir

    return obj
