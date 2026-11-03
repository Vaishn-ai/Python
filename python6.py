from datetime import date, datetime

'''

def get_theme_revenue(core_response, ledger_response):

    camps = core_response["data"]["camps_data"]
    bookings = ledger_response["data"]

    result = []

    for camp in camps:

        season_id = camp["season_id"]

        effective_from = date.fromisoformat(
            camp["effective_from"]
        )

        effective_to = (
            date.fromisoformat(camp["effective_to"])
            if camp["effective_to"]
            else None
        )

        confirmed_bookings = {}

        for booking in bookings:

            created_at = datetime.fromisoformat(
                booking["created_at"].replace("Z", "+00:00")
            ).date()

            if (
                booking["status"] == "confirmed"
                and booking["season_id"] == season_id
                and created_at >= effective_from
                and (
                    effective_to is None
                    or created_at <= effective_to
                )
            ):

                confirmed_bookings[booking["booking_id"]] = booking

        enrollment_count = len(confirmed_bookings)

        weekly_price = float(camp["weekly_price"])

        total_revenue = enrollment_count * weekly_price

        result.append({
            "theme_id": camp["theme_id"],
            "theme_name": camp["theme_name"],
            "enrollment_count": enrollment_count,
            "weekly_price": weekly_price,
            "total_revenue": total_revenue
        })

    return result

'''



async def get_data_call_from_both_services(db:AsyncSession):

    core_response = await get_core_data()
    ledger_reponse = await get_core_data()




# helper function

def fetch_core_data():
    camps = core_response["camps_data"]

    result = []

    for c in camps:

        season_id = c["season_id"]
        batch_id = c["batch_id"]




def fetch_ledger_data():
    ledger = ledger_response["data"]

    result = []

    for l in ledger:

        effective_from = date.fromisoformat(l["effective_from"])
        effective_to = date.fromisoformat(l["effective_to"])

        if not effective_to:
            return None

        weekly_price = float(l['weekly_price'])


def count_weeks():

    weeks = {}

    for l in ledger:
        created_at = datetime.fromisoformat(l["created_at"].replace("Z", "+00:00")).date()

        if l["status"] != "confirmed":
            continue

        if l["season_id"] != season_id:
            continue

        if l["batch_id"] != batch_id:
            continue

        if created_at < effective_from:
            continue

        if effective_to is not None and created_at > effective_to:
            continue

        number_of_week = ((created_at - effective_from).days // 7) +1

        if number_of_week not in weeks:
            weeks[number_of_week] = set()

        weeks[number_of_week].add(l["booking_id"])

    week_data = []

    for week_number, booking_id in sorted(weeks.items()):
        enrollment_count = len(booking_id)

        total_revenue = enrollment_count * week_price

        week_data.append({
            "week": f"Week {week_number}",
            "total_revenue" : total_revenue
        })

    result.append({
        "theme_id": camp["theme_id"],
        "theme_name": camp["theme_name"],
        "batch_id": batch_id,
        "batch_name": camp["batch_name"],
        "weekly_data": weekly_data       
    })

    return result





# error resolution


async def _data(response, path):

    if response.status_code >= 400:

        print("Ledger Status:", response.status_code)
        print("Ledger Error:", response.text)

        raise ServiceUnavailableError(
            f"Ledger API Error: {response.text}"
        )

    return response.json()





# ledger.py


# return data.get("data", {}).get("camps_data", [])


# main function


from datetime import date, datetime, timedelta


def get_theme_revenue(core_response, ledger_response):

    camps = core_response["data"]["camps_data"]
    bookings = ledger_response["data"]

    result = []

    for camp in camps:

        season_id = camp["season_id"]
        batch_id = camp["batch_id"]

        effective_from = date.fromisoformat(
            camp["effective_from"]
        )

        effective_to = (
            date.fromisoformat(camp["effective_to"])
            if camp["effective_to"]
            else None
        )

        weekly_price = float(camp["weekly_price"])

        weeks = {}

        for booking in bookings:

            created_at = datetime.fromisoformat(
                booking["created_at"].replace("Z", "+00:00")
            ).date()

            if (
                booking["status"] != "confirmed"
                or booking["season_id"] != season_id
                or booking["batch_id"] != batch_id
                or created_at < effective_from
                or (
                    effective_to is not None
                    and created_at > effective_to
                )
            ):
                continue

            # Calculate week number
            week_number = (
                (created_at - effective_from).days // 7
            ) + 1

            if week_number not in weeks:
                weeks[week_number] = set()

            weeks[week_number].add(booking["booking_id"])

        weekly_data = []

        for week_number, booking_ids in sorted(weeks.items()):

            enrollment_count = len(booking_ids)

            total_revenue = enrollment_count * weekly_price

            weekly_data.append({
                "week": f"Week {week_number}",
                "enrollment_count": enrollment_count,
                "total_revenue": total_revenue
            })

        result.append({
            "theme_id": camp["theme_id"],
            "theme_name": camp["theme_name"],
            "batch_id": batch_id,
            "batch_name": camp["batch_name"],
            "weekly_data": weekly_data
        })

    return result