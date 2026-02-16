import datetime
import calendar

def format_date(date_obj):
    """Formats date as YYYY-Mon-DD (e.g., 2026-Jan-01)."""
    if isinstance(date_obj, datetime.date):
        return date_obj.strftime("%Y-%b-%d")
    return date_obj

def add_months(source_date, months):
    month = source_date.month - 1 + months
    year = source_date.year + month // 12
    month = month % 12 + 1
    day = min(source_date.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)

def count_non_sunday_days(start_date, end_date):
    """Counts total days from start_date to end_date (inclusive) minus Sundays."""
    if start_date > end_date:
        return 0

    count = 0
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() != 6:  # Sunday = 6
            count += 1
        current_date += datetime.timedelta(days=1)

    return count

def find_end_date_by_days(start_date, target_days):
    if target_days <= 0:
        return None

    current_date = start_date
    count = 0

    if current_date.weekday() != 6:
        count = 1

    while count < target_days:
        current_date += datetime.timedelta(days=1)
        if current_date.weekday() != 6:
            count += 1

    return current_date

def get_valid_date(prompt):
    while True:
        try:
            date_str = input(prompt).strip()
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid Date! Use format YYYY-MM-DD (e.g., 2025-01-20).")

def get_valid_int(prompt, allowed_values=None, min_val=0):
    while True:
        try:
            val = int(input(prompt).strip())
            if allowed_values and val not in allowed_values:
                print(f"❌ Enter one of: {allowed_values}")
                continue
            if val < min_val:
                print(f"❌ Minimum allowed is {min_val}")
                continue
            return val
        except ValueError:
            print("❌ Please enter a valid integer.")

def get_valid_float(prompt, min_val=0.0):
    while True:
        try:
            val = float(input(prompt).strip().replace(",", ""))
            if val < min_val:
                print(f"❌ Minimum allowed is {min_val}")
                continue
            return val
        except ValueError:
            print("❌ Enter a valid amount (e.g., 7000 or 70.50).")

def main():
    print("="*60)
    print("🚀 PROFESSIONAL LEASE & PAYMENT CALCULATOR 🚀")
    print("="*60)

    # Inputs
    start_date = get_valid_date("📅 Enter Lease Start Date (YYYY-MM-DD): ")
    duration_months = get_valid_int("⏳ Enter Lease Duration (18 or 24): ", allowed_values=[18, 24])
    days_paid = get_valid_int("💳 Enter Number of Days Paid: ")
    daily_amount = get_valid_float("💰 Enter Daily Payment Amount: ")
    current_date = get_valid_date("📆 Enter Current Date (YYYY-MM-DD): ")

    target_non_sunday_days = 624 if duration_months == 24 else 468
    lease_end_date = find_end_date_by_days(start_date, target_non_sunday_days)

    # Payment calculations
    if days_paid > 0:
        last_payment_date = find_end_date_by_days(start_date, days_paid)
        next_payment_date = last_payment_date + datetime.timedelta(days=1)
        if next_payment_date.weekday() == 6:
            next_payment_date += datetime.timedelta(days=1)

        # DEFAULTING COUNT calculation
        defaulting_start = last_payment_date + datetime.timedelta(days=1)
        DEFAULTING_COUNT = count_non_sunday_days(defaulting_start, current_date)

    else:
        last_payment_date = None
        next_payment_date = start_date
        if next_payment_date.weekday() == 6:
            next_payment_date += datetime.timedelta(days=1)

        DEFAULTING_COUNT = count_non_sunday_days(start_date, current_date)

    total_amount_paid = days_paid * daily_amount
    remaining_days = target_non_sunday_days - days_paid
    remaining_balance = remaining_days * daily_amount

    # Output
    print("\n" + "🏁 FINAL SUMMARY REPORT 🏁".center(60))
    print("-" * 60)

    print(f"{'Lease Start Date:':<30} {format_date(start_date)}")
    print(f"{'Lease End Date:':<30} {format_date(lease_end_date)}")
    print(f"{'Total Lease Duration:':<30} {duration_months} Months")
    print(f"{'Target Work Days:':<30} {target_non_sunday_days} (Excl. Sundays)")

    print("-" * 60)

    print(f"{'Number of Days Paid:':<30} {days_paid}")
    print(f"{'Number of Days Pending:':<30} {max(0, remaining_days)}")
    print(f"{'Last Payment Date:':<30} {format_date(last_payment_date) if last_payment_date else 'No Payments Made'}")
    print(f"{'Next Payment Date:':<30} {format_date(next_payment_date)}")
    print(f"{'DEFAULTING_COUNT:':<30} {max(0, DEFAULTING_COUNT)} Days")

    print("-" * 60)

    print(f"{'Daily Rental Rate:':<30} {daily_amount:,.2f}")
    print(f"{'Total Amount Paid:':<30} {total_amount_paid:,.2f}")
    print(f"{'Remaining Balance:':<30} {max(0, remaining_balance):,.2f}")

    print("-" * 60)
    print("✨ Calculation Complete! ✨")
    print("="*60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Operation cancelled.")
    except Exception as e:
        print(f"\n☢️ Unexpected error: {e}")
