"""
Day 18: DateTime
================
Learn to work with dates, times, and timezones.

Key concepts:
- datetime objects
- Parsing and formatting
- Timedelta calculations
- Timezone handling
- Common patterns
"""

from datetime import datetime, date, time, timedelta
import calendar

# =============================================================================
# CONCEPT: DateTime Basics
# =============================================================================

def datetime_basics():
    """Basic datetime operations."""

    # Current date/time
    now = datetime.now()
    today = date.today()

    # Create specific date/time
    specific = datetime(2026, 1, 19, 14, 30, 0)

    # From timestamp
    from_ts = datetime.fromtimestamp(1737302400)

    return now, today, specific, from_ts


# =============================================================================
# EXAMPLES
# =============================================================================

def example_creating_datetimes():
    """Demonstrate creating datetime objects."""
    print("=== Creating DateTimes ===")

    # Current
    now = datetime.now()
    print(f"Now: {now}")

    today = date.today()
    print(f"Today: {today}")

    # Specific date/time
    dt = datetime(2026, 1, 19, 14, 30, 45)
    print(f"Specific: {dt}")

    # Date only
    d = date(2026, 1, 19)
    print(f"Date only: {d}")

    # Time only
    t = time(14, 30, 45)
    print(f"Time only: {t}")

    # Combine date and time
    combined = datetime.combine(d, t)
    print(f"Combined: {combined}")


def example_datetime_parts():
    """Demonstrate accessing datetime components."""
    print("\n=== DateTime Components ===")

    dt = datetime(2026, 1, 19, 14, 30, 45)

    print(f"DateTime: {dt}")
    print(f"Year: {dt.year}")
    print(f"Month: {dt.month}")
    print(f"Day: {dt.day}")
    print(f"Hour: {dt.hour}")
    print(f"Minute: {dt.minute}")
    print(f"Second: {dt.second}")
    print(f"Weekday: {dt.weekday()}")  # Monday=0
    print(f"Day name: {calendar.day_name[dt.weekday()]}")
    print(f"ISO weekday: {dt.isoweekday()}")  # Monday=1
    print(f"Day of year: {dt.timetuple().tm_yday}")


def example_formatting():
    """Demonstrate datetime formatting."""
    print("\n=== Formatting ===")

    dt = datetime(2026, 1, 19, 14, 30, 45)

    # Common formats
    print(f"ISO format: {dt.isoformat()}")
    print(f"Custom: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"US style: {dt.strftime('%m/%d/%Y')}")
    print(f"Readable: {dt.strftime('%B %d, %Y')}")
    print(f"With day: {dt.strftime('%A, %B %d, %Y')}")
    print(f"12-hour: {dt.strftime('%I:%M %p')}")

    # Format codes reference
    print("\nCommon format codes:")
    print("  %Y - 4-digit year (2026)")
    print("  %m - Month (01-12)")
    print("  %d - Day (01-31)")
    print("  %H - Hour 24h (00-23)")
    print("  %I - Hour 12h (01-12)")
    print("  %M - Minute (00-59)")
    print("  %S - Second (00-59)")
    print("  %p - AM/PM")
    print("  %A - Full weekday (Monday)")
    print("  %B - Full month (January)")


def example_parsing():
    """Demonstrate parsing datetime strings."""
    print("\n=== Parsing ===")

    # Parse various formats
    formats = [
        ("2026-01-19", "%Y-%m-%d"),
        ("01/19/2026", "%m/%d/%Y"),
        ("19-Jan-2026", "%d-%b-%Y"),
        ("January 19, 2026", "%B %d, %Y"),
        ("2026-01-19T14:30:45", "%Y-%m-%dT%H:%M:%S"),
    ]

    for date_str, fmt in formats:
        dt = datetime.strptime(date_str, fmt)
        print(f"'{date_str}' ({fmt}) -> {dt}")

    # ISO format parsing
    iso_str = "2026-01-19T14:30:45"
    dt = datetime.fromisoformat(iso_str)
    print(f"\nISO format: '{iso_str}' -> {dt}")


def example_timedelta():
    """Demonstrate timedelta calculations."""
    print("\n=== Timedelta ===")

    now = datetime(2026, 1, 19, 12, 0, 0)

    # Create timedeltas
    one_day = timedelta(days=1)
    one_week = timedelta(weeks=1)
    two_hours = timedelta(hours=2)
    complex_delta = timedelta(days=1, hours=5, minutes=30)

    print(f"Now: {now}")
    print(f"Tomorrow: {now + one_day}")
    print(f"Next week: {now + one_week}")
    print(f"2 hours ago: {now - two_hours}")
    print(f"Complex: {now + complex_delta}")

    # Calculate difference
    future = datetime(2026, 12, 31, 23, 59, 59)
    diff = future - now
    print(f"\nDays until end of year: {diff.days}")
    print(f"Total seconds: {diff.total_seconds()}")


def example_comparisons():
    """Demonstrate datetime comparisons."""
    print("\n=== Comparisons ===")

    dt1 = datetime(2026, 1, 15)
    dt2 = datetime(2026, 1, 20)
    dt3 = datetime(2026, 1, 15)

    print(f"dt1: {dt1}")
    print(f"dt2: {dt2}")

    print(f"\ndt1 < dt2: {dt1 < dt2}")
    print(f"dt1 == dt3: {dt1 == dt3}")
    print(f"dt1 != dt2: {dt1 != dt2}")

    # Check if date is in range
    target = datetime(2026, 1, 17)
    in_range = dt1 <= target <= dt2
    print(f"\n{target} between {dt1} and {dt2}: {in_range}")


def example_practical_patterns():
    """Demonstrate practical datetime patterns."""
    print("\n=== Practical Patterns ===")

    # Start/end of day
    now = datetime.now()
    start_of_day = datetime.combine(now.date(), time.min)
    end_of_day = datetime.combine(now.date(), time.max)
    print(f"Start of day: {start_of_day}")
    print(f"End of day: {end_of_day}")

    # Start/end of month
    first_of_month = now.replace(day=1)
    last_day = calendar.monthrange(now.year, now.month)[1]
    last_of_month = now.replace(day=last_day)
    print(f"\nFirst of month: {first_of_month.date()}")
    print(f"Last of month: {last_of_month.date()}")

    # Business days calculation (simple)
    def add_business_days(start, days):
        current = start
        added = 0
        while added < days:
            current += timedelta(days=1)
            if current.weekday() < 5:  # Monday-Friday
                added += 1
        return current

    start = datetime(2026, 1, 19)  # Monday
    result = add_business_days(start, 5)
    print(f"\n5 business days from {start.date()}: {result.date()}")

    # Age calculation
    def calculate_age(birthdate, reference=None):
        reference = reference or date.today()
        age = reference.year - birthdate.year
        if (reference.month, reference.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age

    birthday = date(1990, 6, 15)
    age = calculate_age(birthday, date(2026, 1, 19))
    print(f"\nAge on 2026-01-19 for DOB {birthday}: {age}")


def example_timezones():
    """Demonstrate timezone handling (basic)."""
    print("\n=== Timezones (Basic) ===")

    # Note: For production, use pytz or zoneinfo (Python 3.9+)
    print("For full timezone support, use:")
    print("  - Python 3.9+: from zoneinfo import ZoneInfo")
    print("  - Earlier: pip install pytz")

    # Basic UTC handling
    from datetime import timezone

    utc_now = datetime.now(timezone.utc)
    print(f"\nUTC now: {utc_now}")

    # Offset
    offset = timezone(timedelta(hours=-5))  # EST
    est_now = datetime.now(offset)
    print(f"EST now: {est_now}")


# =============================================================================
# EXERCISES
# =============================================================================

def exercise_1():
    """
    Exercise 1: Date Range Generator

    Create functions for generating date ranges:

    def date_range(start, end, step=1):
        '''Generate dates from start to end (inclusive).'''
        pass

    def weekly_dates(start, end, weekday):
        '''Generate all dates of a specific weekday in range.
        weekday: 0=Monday, 6=Sunday
        '''
        pass

    def monthly_dates(start, end, day):
        '''Generate same day of each month in range.
        Handle months with fewer days.
        '''
        pass

    Examples:
    list(date_range(date(2026, 1, 1), date(2026, 1, 5)))
    # [date(2026,1,1), date(2026,1,2), date(2026,1,3), date(2026,1,4), date(2026,1,5)]

    list(weekly_dates(date(2026, 1, 1), date(2026, 1, 31), 0))  # All Mondays
    """
    # YOUR CODE HERE
    pass


def exercise_2():
    """
    Exercise 2: Business Calendar

    Create a BusinessCalendar class:

    cal = BusinessCalendar(holidays=[date(2026, 1, 1), date(2026, 12, 25)])

    cal.is_business_day(date(2026, 1, 2))  # True (weekday, not holiday)
    cal.is_business_day(date(2026, 1, 3))  # False (Saturday)
    cal.is_business_day(date(2026, 1, 1))  # False (holiday)

    cal.add_business_days(date(2026, 1, 2), 5)  # Add 5 business days
    cal.business_days_between(date(2026, 1, 1), date(2026, 1, 31))  # Count
    cal.next_business_day(date(2026, 1, 3))  # Next business day after Saturday
    """
    # YOUR CODE HERE
    pass


def exercise_3():
    """
    Exercise 3: Duration Formatter

    Create functions for human-readable durations:

    def format_duration(seconds):
        '''Format seconds as human-readable duration.
        format_duration(90) -> "1 minute, 30 seconds"
        format_duration(3661) -> "1 hour, 1 minute, 1 second"
        format_duration(86400) -> "1 day"
        '''
        pass

    def parse_duration(text):
        '''Parse human-readable duration to timedelta.
        parse_duration("2 hours 30 minutes") -> timedelta(hours=2, minutes=30)
        parse_duration("1d 5h") -> timedelta(days=1, hours=5)
        '''
        pass

    def time_ago(dt):
        '''Format datetime as relative time.
        time_ago(now - timedelta(minutes=5)) -> "5 minutes ago"
        time_ago(now - timedelta(days=1)) -> "yesterday"
        time_ago(now + timedelta(hours=2)) -> "in 2 hours"
        '''
        pass
    """
    # YOUR CODE HERE
    pass


def exercise_4():
    """
    Exercise 4: Recurring Events

    Create a RecurringEvent class:

    # Daily standup at 9am
    standup = RecurringEvent(
        name="Standup",
        start_time=time(9, 0),
        recurrence="daily",
        skip_weekends=True
    )

    # Weekly team meeting
    meeting = RecurringEvent(
        name="Team Meeting",
        start_time=time(14, 0),
        recurrence="weekly",
        weekday=2  # Wednesday
    )

    # Monthly report due
    report = RecurringEvent(
        name="Monthly Report",
        start_time=time(17, 0),
        recurrence="monthly",
        day=15  # 15th of each month
    )

    # Get occurrences
    standup.occurrences(date(2026, 1, 1), date(2026, 1, 31))
    meeting.next_occurrence(date(2026, 1, 15))
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# CHALLENGE
# =============================================================================

def challenge():
    """
    Challenge: Complete DateTime Library

    Build a comprehensive datetime utility library:

    1. DateTimeRange:
       - Immutable range with start/end
       - Contains check (is datetime in range?)
       - Overlap detection
       - Intersection and union operations
       - Iteration (by day, hour, etc.)

    2. SmartParser:
       - Parse dates in multiple formats automatically
       - Handle relative dates ("tomorrow", "next week")
       - Parse ranges ("Jan 1-15", "this week")
       - Natural language ("in 3 days", "2 weeks ago")

    3. Scheduler:
       - Schedule events with recurrence rules
       - Handle exceptions (skip certain dates)
       - Conflict detection
       - Next N occurrences

    4. TimeZoneConverter:
       - Convert between timezones
       - Handle DST transitions
       - Format for different locales

    Example usage:

    # Range operations
    meeting = DateTimeRange(
        datetime(2026, 1, 19, 14, 0),
        datetime(2026, 1, 19, 15, 0)
    )
    another = DateTimeRange(
        datetime(2026, 1, 19, 14, 30),
        datetime(2026, 1, 19, 15, 30)
    )
    print(meeting.overlaps(another))  # True
    print(meeting.intersection(another))  # 14:30-15:00

    # Smart parsing
    parser = SmartParser()
    print(parser.parse("Jan 19, 2026"))
    print(parser.parse("tomorrow"))
    print(parser.parse("in 2 weeks"))
    print(parser.parse_range("Jan 1-15"))

    # Scheduling
    scheduler = Scheduler()
    scheduler.add_recurring(
        name="Standup",
        start=time(9, 0),
        duration=timedelta(minutes=15),
        recurrence="daily",
        exceptions=[date(2026, 1, 1)]
    )
    print(scheduler.next_occurrences("Standup", 5))
    print(scheduler.check_conflicts(meeting))
    """
    # YOUR CODE HERE
    pass


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("Day 18: DateTime\n")
    print("=" * 50)

    # Run examples
    example_creating_datetimes()
    example_datetime_parts()
    example_formatting()
    example_parsing()
    example_timedelta()
    example_comparisons()
    example_practical_patterns()
    example_timezones()

    print("\n" + "=" * 50)
    print("Now complete the exercises!")

    # Uncomment to test your exercises:
    # exercise_1()
    # exercise_2()
    # exercise_3()
    # exercise_4()
    # challenge()
