from enum import Enum


class Status(Enum):
    REQUESTED = 0
    MISSING_INFO = 1
    PROCESSED = 2
    ACTIVATED = 3
    CANCELED = 4


status_dict = {
    0: "Requested",
    1: "Missing info",
    2: "Processed",
    3: "Activated",
    4: "Canceled",
}


def sort_statuses_by_priority(*args):
    sorted_statuses = []
    for status in status_dict.values():
        if status in args:
            sorted_statuses.append(status)
    return sorted_statuses


def get_parent_task_status(*statuses):
    sorted_statuses = sort_statuses_by_priority(*statuses)

    missing_info = status_dict[Status.MISSING_INFO.value]
    processed = status_dict[Status.PROCESSED.value]
    requested = status_dict[Status.REQUESTED.value]
    activated = status_dict[Status.ACTIVATED.value]
    canceled = status_dict[Status.CANCELED.value]

    if all(status == sorted_statuses[0] for status in sorted_statuses):
        return sorted_statuses[0]
    elif missing_info in sorted_statuses:
        return missing_info
    elif processed in sorted_statuses:
        return processed
    elif all(status in [activated, canceled] for status in sorted_statuses):
        return activated
    else:
        return requested


if __name__ == '__main__':
    tests = [
        {'response': get_parent_task_status('Processed', 'Missing info', 'Requested'), 'expected': 'Missing info'},
        {'response': get_parent_task_status('Requested', 'Processed', 'Cancelled'), 'expected': 'Processed'},
        {'response': get_parent_task_status('Requested', 'Requested', 'Requested'), 'expected': 'Requested'},
        {'response': get_parent_task_status('Activated', 'Activated', 'Canceled'), 'expected': 'Activated'},
    ]

    for i, test in enumerate(tests):
        if test['response'] is test['expected']:
            print(f"passed {i + 1}")
        else:
            print(f"failed {i + 1}")
