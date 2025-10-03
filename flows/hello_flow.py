import subprocess
from prefect import flow, task

@task
def dbt_debug():
    # We start with dbt --version (lightweight). We'll switch to dbt debug/run later.
    out = subprocess.run(["dbt", "--version"], capture_output=True, text=True, check=True)
    print(out.stdout)

@flow(name="dbt-echo")
def dbt_echo_flow():
    dbt_debug()

if __name__ == "__main__":
    dbt_echo_flow()
