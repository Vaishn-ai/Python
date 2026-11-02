def calculate_available_seats(
    batches,
    active_holds,
    enrollment_counts
):
    result = []

    # Create lookup dictionaries
    holds_map = {
        item.batch_id: item.active_hold_count
        for item in active_holds
    }

    enrollment_map = {
        item.batch_id: item.enrolled_count
        for item in enrollment_counts
    }

    for batch in batches:

        capacity = batch.capacity

        active_hold = holds_map.get(batch.batch_id, 0)

        confirmed_seat = enrollment_map.get(
            batch.batch_id, 0
        )

        available_seat = max(
            0,
            capacity - active_hold - confirmed_seat
        )

        result.append(
            BatchSeatInsightResponse(
                course_id=batch.course_id,
                batch_id=batch.batch_id,
                title=batch.title,
                start_date=batch.start_date,
                end_date=batch.end_date,
                capacity=capacity,
                active_hold=active_hold,
                confirmed_seat=confirmed_seat,
                available_seat=available_seat
            )
        )

    return result



from datetime import date

async def get_available_seats():

    # Fetch data from both services
    batches = await get_course_batch_data()
    active_holds = await get_active_seat_hold()

    response = []

    # Check upcoming batches
    for batch in batches:

        if batch.start_date <= date.today():
            continue

        # Get active holds for this batch
        active_hold = sum(
            hold.active_hold
            for hold in active_holds
            if hold.batch_id == batch.batch_id
        )

        # Get confirmed enrollments from existing ledger data
        confirmed_seat = batch.enrolled_count

        # Calculate available seats
        available_seat = (
            batch.capacity - active_hold - confirmed_seat
        )

        response.append({
            "course_id": batch.course_id,
            "batch_id": batch.batch_id,
            "title": batch.title,
            "start_date": batch.start_date,
            "end_date": batch.end_date,
            "capacity": batch.capacity,
            "active_hold": active_hold,
            "confirmed_seat": confirmed_seat,
            "available_seat": max(0, available_seat)
        })

    return response