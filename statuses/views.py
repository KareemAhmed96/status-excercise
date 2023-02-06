from enum import Enum

from rest_framework import status as s
from rest_framework.decorators import api_view
from rest_framework.response import Response


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


def validate_subtasks(subtask_statuses):
    for subtask_status in subtask_statuses:
        if subtask_status.capitalize() not in status_dict.values():
            raise Exception(f"Invalid status was provided: "
                            f"{subtask_status}")


def sort_statuses_by_priority(statuses):
    sorted_statuses = []
    validate_subtasks(statuses)
    for status in status_dict.values():
        if status in statuses:
            sorted_statuses.append(status)
    return sorted_statuses


@api_view(['GET'], )
def get_parent_task_status(request):
    response = None
    sorted_statuses = None
    subtask_statuses = request.data.get('subtask_statuses')

    try:
        sorted_statuses = sort_statuses_by_priority(subtask_statuses)
    except Exception as e:
        return Response(data={
            "success": False,
            "errors": f"An error occurred: {str(e)}"
        }, status=s.HTTP_200_OK)

    missing_info = status_dict[Status.MISSING_INFO.value]
    processed = status_dict[Status.PROCESSED.value]
    requested = status_dict[Status.REQUESTED.value]
    activated = status_dict[Status.ACTIVATED.value]
    canceled = status_dict[Status.CANCELED.value]

    if all(status == sorted_statuses[0] for status in sorted_statuses):
        response = sorted_statuses[0]
    elif missing_info in sorted_statuses:
        response = missing_info
    elif processed in sorted_statuses:
        response = processed
    elif all(status in [activated, canceled] for status in sorted_statuses):
        response = activated
    else:
        response = requested

    return Response(data={
        "success": True,
        "parent_status": response
    }, status=s.HTTP_200_OK)
