import os
import re
import requests
import json
import datetime
import time
import asana
import traceback


def _asana_tasks() -> str:
    # Create a client object using the provided API key.
    asana_api_key = os.getenv('ASANA_KEY')
    user_id = os.getenv('ASANA_USER')

    client = asana.Client.access_token(asana_api_key)

    # Opt into the new behavior by setting the 'Asana-Enable' header.
    client.headers.update({'Asana-Enable': 'new_goal_memberships'})

    # Get the user's workspaces.
    workspaces = client.workspaces.get_workspaces()

    # Store a list of assigned tasks.
    assigned_tasks = []

    # Iterate through each workspace.
    for workspace in workspaces:
        # Get a list of tasks assigned to the user in the workspace.
        tasks = client.tasks.get_tasks({'assignee': user_id, 'workspace': workspace['gid'], 'assignee_status': 'inbox', 'completed_since': 'now'})

        # Add each task to the assigned_tasks list.
        for task in tasks:
            assigned_tasks.append(task)


    result = f"""Current Tasks: {assigned_tasks}\n"""

    return result


def _comment_asana_task(gid, message) -> str:
    # Create a client object using the provided API key.
    asana_api_key = os.getenv('ASANA_KEY')
    user_id = os.getenv('ASANA_USER')
    client = asana.Client.access_token(asana_api_key)

    # Opt into the new behavior by setting the 'Asana-Enable' header.
    client.headers.update({'Asana-Enable': 'new_user_task_lists'})
    client.headers.update({'Asana-Enable': 'new_goal_memberships'})

    # Post a comment to the specified task ID.
    comment = client.tasks.add_comment(str(gid), {'text': message})

    result = f"""Comment on Task {gid}: {comment}\n"""

    return result

def _get_asana_task(gid) -> str:
    # Create a client object using the provided API key.
    asana_api_key = os.getenv('ASANA_KEY')
    user_id = os.getenv('ASANA_USER')
    client = asana.Client.access_token(asana_api_key)

    # Opt into the new behavior by setting the 'Asana-Enable' header.
    client.headers.update({'Asana-Enable': 'new_user_task_lists'})

    # Fetch details of the specified task ID.
    task_details = client.tasks.get_task(gid)

    result = f"""Task #{gid} Title: {task_details["name"]} Details: {task_details["notes"]} \n"""

    return result

def _complete_asana_task(gid) -> str:
    try:
        asana_api_key = os.getenv('ASANA_KEY')
        user_id = os.getenv('ASANA_USER')
        client = asana.Client.access_token(asana_api_key)
        task = client.tasks.get_task(str(gid))
        client.tasks.update_task(task["gid"], {"completed": True})
        return f"Task with gid {gid} has been completed"
    except Exception as e:
        error_traceback = traceback.format_exc()
        return f"There was an error completing the task with gid {gid}: {e}. Traceback: {error_traceback}. Please try again later."
