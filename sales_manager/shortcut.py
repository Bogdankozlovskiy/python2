from datetime import datetime


def upload_to(instance, filename):
    date = datetime.now().strftime("%Y/%m/%d")
    return f"{instance.title}/{date}/{filename}"
