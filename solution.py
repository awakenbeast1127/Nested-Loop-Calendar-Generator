# Case Study 37: Nested Loop Calendar Generator

def generate_calendar(month, starting_weekday, number_of_days):
    if starting_weekday < 0 or starting_weekday > 6:
        raise ValueError("Starting weekday must be from 0 (Sunday) to 6 (Saturday).")
    if number_of_days not in (28, 29, 30, 31):
        raise ValueError("Number of days must be 28, 29, 30, or 31.")

    lines = [f"       {month}", "Sun Mon Tue Wed Thu Fri Sat"]
    day = 1

    for week in range(6):
        cells = []
        for weekday in range(7):
            if (week == 0 and weekday < starting_weekday) or day > number_of_days:
                cells.append("   ")
            else:
                cells.append(f"{day:>3}")
                day += 1
        lines.append(" ".join(cells))
        if day > number_of_days:
            break

    return "\n".join(lines)


def main():
    print(generate_calendar("NOVEMBER 2026", 0, 30))


if __name__ == "__main__":
    main()
