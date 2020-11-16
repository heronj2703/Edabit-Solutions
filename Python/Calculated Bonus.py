# A financial institution provides professional services to banks and claims charges from the
# customers based on the number of man-days provided. Internally, it has set a scheme to
# motivate and reward staff to meet and exceed targeted billable utilization and revenues by
# paying a bonus for each day claimed from customers in excess of a threshold target.

def bonus(days):
    return 325 * max(0, days - 32) + 225 * max(0, days - 40) + 50 * max(0, days - 48)
