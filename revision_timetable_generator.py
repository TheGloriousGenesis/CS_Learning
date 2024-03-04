import random
from datetime import datetime, timedelta
from typing import Dict, Optional

random.seed(42)


def generate_revision_timetable(
    subjects: Dict[str, int], start_date: str, end_date: str, daily_hours: int, session_duration: Optional[int] = 1
):
    """
    Generate a simple revision timetable.

    :param subjects: Dictionary of subjects to revise with expected time to spend on each.
    :param start_date: Start date for revision in 'YYYY-MM-DD' format.
    :param end_date: End date for revision in 'YYYY-MM-DD' format.
    :param daily_hours: Number of hours to revise each day.
    :param session_duration: Number of hours a given revision slot should be.
    :return: A revision timetable as a list of tuples (date, subject, hours).
    """

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    total_days = (end_date - start_date).days + 1

    total_expected_revision_hours = sum(subjects.values())

    # Calculate total revision sessions
    total_sessions = total_days * daily_hours

    if total_expected_revision_hours > total_sessions:
        raise Exception("Expected revision hours are more than total sessions available")

    timetable = []
    current_date = start_date

    remaining_sessions = total_sessions

    for day in range(total_days):
        for hour in range(daily_hours):
            subject = pick_subject(subjects)
            if not subject:
                break
            timetable.append((current_date.strftime("%A %d %B %Y"), subject, session_duration))
            subjects[subject] -= session_duration
            remaining_sessions -= session_duration
        current_date += timedelta(days=1)

    print(f"Remaining Sessions: {remaining_sessions}")
    return timetable


def pick_subject(subjects: Dict[str, int]) -> str:
    if sum(subjects.values()) == 0:
        return ""

    filtered_dict = {key: value for key, value in subjects.items() if value > 0}
    keys = list(filtered_dict.keys())
    weights = list(filtered_dict.values())

    selected_key = random.choices(keys, weights=weights, k=1)[0]

    return selected_key


# Example usage
subjects = {"Udemy": 50, "Whizlabs": 90, "AWS": 60, "Data Science": 40}
start_date = "2024-02-01"
end_date = "2024-05-30"
daily_hours = 2
weekly_hours = {"Monday": daily_hours,
                "Tuesday": daily_hours,
                "Wednesday": daily_hours,
                "Thursday": daily_hours,
                "Friday": daily_hours,
                "Saturday": 5,
                "Sunday": 5
                }

timetable = generate_revision_timetable(subjects, start_date, end_date, daily_hours)


if __name__ == "__main__":
    for tup in timetable:
        print(tup)
