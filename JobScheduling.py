n=int(input("number of jobs:- "))
progress=[]
avg=0
for i in range(n):
    job=input("Enter Job name ")
    progress.append(job)
    task=int(input(f"Enter number of task {job} "))
    for j in range(task):
        task_name=input("Enter task name: ")
        percentage_completed=float(input("Enter work completion in percentage:- "))
        endDate=input(f"End Date for task {t} ")
        avg = avg + percentage_completed
        progress.append((task_name,percentage_completed,endDate))
    print(f"Average of completion for job {j} : {avg/task}")
    
    
print("List of jobs: ")
print(progress)

