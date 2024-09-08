from kubiya_sdk.workflows.stateful_workflow import StatefulWorkflow

# Define a simple workflow
workflow = StatefulWorkflow(
    "MyWorkflow",
    "test workflow description"
)

@workflow.step("step1")
def step1(state):
    return {"result": state["input"] * 2}

@workflow.step("step2")
def step2(state):
    return {"final_result": state["result"] + 1}

workflow.add_edge("step1", "step2")

# Make sure the workflow instance is exposed
# workflow_instance = workflow