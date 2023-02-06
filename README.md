## Exercise

Imagine that you are in a project with tasks. Each task has N subtasks, at least it has 1 subtask.
Both tasks and subtasks have a status, which can have the following values:

```
dictStatus = {
    0: “Requested”,
    1: “Missing info”,
    2: “Processed”,
    3: “Activated”,
    4: “Canceled”,
}
```

The exercise consists of making a function that receives N input parameters (the N values
​corresponding to the status of the subtasks, in text) and calculates the status of the general
task, also in text. To make this calculation, the following logic must be taken into account,
ordered from greater to lesser importance / weight:

- If all subtasks have the same status, the general task also has this status.
- If a subtask has a status of Missing info, the general task also has this status.
- If a subtask has a status of Processed, the general task also has this status.
- The general task state is Activated only if all sub-states are Activated or Canceled.
- In all other cases, the general task status is Requested.

#### Examples (for tasks with 3 subtasks, although it could be N subtasks):
1. Input: Requested,Requested,Requested // Output: Requested
2. Input: Activated, Activated, Canceled // Output: Activated
3. Input: Requested, Processed, Canceled // Output: Processed
4. Input: Processed, Missing info, Processed // Output: Missing info