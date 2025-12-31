from datetime import datetime

def check_freshness(last_updated_time: datetime, max_delay_minutes: int):
    """
    last_updated_time: when the dataset was last updated (UTC)
    Returns:
      (pass_bool, delay_minutes_float)
    """
    delay_minutes = (datetime.utcnow() - last_updated_time).total_seconds() / 60.0
    return delay_minutes <= max_delay_minutes, float(delay_minutes)

