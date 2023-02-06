from enum import Enum


class Status(Enum):
    REQUESTED = 0
    MISSING_INFO = 1
    PROCESSED = 2
    ACTIVATED = 3
    CANCELLED = 4


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


def get_parent_task_status(*args):
    count = 1
    for arg in sort_statuses_by_priority(*args):
        if arg is status_dict[Status.MISSING_INFO.value]:
            return arg
        elif arg is status_dict[Status.PROCESSED.value]:
            return arg

        count += 1
        # print(count)


if __name__ == '__main__':
    response_1 = get_parent_task_status('Processed', 'Missing info', 'Requested')
    expected_1 = 'Missing info'
    print("passed 1") if response_1 is expected_1 else print("failed 1")

    response_2 = get_parent_task_status('Requested', 'Processed', 'Cancelled')
    expected_2 = 'Processed'
    print("passed 2") if response_2 is expected_2 else print("failed 2")

    response_3 = get_parent_task_status('Requested', 'Requested', 'Requested')
    expected_3 = 'Requested'
    print("passed 3") if response_3 is expected_3 else print("failed 3")

    response_4 = get_parent_task_status('Activated', 'Activated', 'Cancelled')
    expected_4 = 'Activated'
    print("passed 4") if response_4 is expected_4 else print("failed 4")
