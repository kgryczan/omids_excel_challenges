import pandas as pd
from datetime import datetime, timedelta

path = "CH-219 Project scheduling.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=9)
test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=9)

def schedule_tasks(tasks, start_date=datetime.now().date()):
    tasks = pd.DataFrame({
        'id': tasks['Task Name'].astype(str),
        'duration': tasks['Duration (day)'],
        'predecessors': [[p.strip() for p in str(pred).split(',') if p.strip() != '-'] if not pd.isna(pred) else [] for pred in tasks['Predecessors']]
    })
    
    task_durations = dict(zip(tasks['id'], tasks['duration']))
    task_preds = dict(zip(tasks['id'], tasks['predecessors']))
    
    all_task_ids = set(tasks['id'])
    for task_id, preds in task_preds.items():
        for pred in preds:
            if pred not in all_task_ids:
                raise ValueError(f"Task {task_id} has predecessor {pred} that doesn't exist")
    
    visited = {id: False for id in tasks['id']}
    temp = {id: False for id in tasks['id']} 
    result = []
    
    def dfs(node):
        if visited[node]:
            return
        if temp[node]:
            raise ValueError(f"Cycle detected in task dependencies involving task {node}")
            
        temp[node] = True

        for pred in task_preds[node]:
            dfs(pred)
            
        temp[node] = False
        visited[node] = True
        result.append(node)
    
    for task_id in tasks['id']:
        if not visited[task_id]:
            dfs(task_id)
    
    topo_order = result
    
    dates = {}
    for id in topo_order:
        start = start_date if not task_preds[id] else max(dates[p]['end'] for p in task_preds[id])
        dates[id] = {'start': start, 'end': start + timedelta(days=task_durations[id])}
    
    return pd.DataFrame({
        'id': list(dates.keys()),
        'start_date': [dates[id]['start'] for id in dates],
        'end_date': [dates[id]['end'] - timedelta(days=1) for id in dates]
    }).sort_values('id').reset_index(drop=True)

print(schedule_tasks(input, datetime.strptime("2025-04-01", "%Y-%m-%d").date()))
