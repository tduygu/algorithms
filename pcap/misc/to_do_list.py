import random


def get_choice():
    mainMenu = "== TODO LIST ==\n [1] show tasks\n [2] add task\n [3] complete task\n [4] exit"
    print(mainMenu)
    task_no = input("Your choice:")
    return task_no

def get_task_info():
    print("[ADD TASK]")
    task = input("What is the task?")
    deadline = input("What is the deadline?")
    return task, deadline

def complete_task_info(task_file):
    print("[COMPLETE TASK]")
    read_tasks(task_file)
    task_id = input("Enter id to complete")
    return task_id

def read_tasks(task_file):
    try:
        stream = open(task_file)
        stream_str = stream.read()
        if stream_str != '':
            print(f"[YOUR TASKS]\n{stream_str}")
        else:
            print("Empty list")
        stream.close()
    except Exception as e:
        print(f"Error occured: {e}")

def add_task(task_file):
    try:
        stream = open(task_file,"a")
        task_tuple = get_task_info()
        task_id = str(generate_id())
        task_str = f"{task_id} | {task_tuple[0]} | {task_tuple[1]}\n"
        stream.write(task_str)
    except Exception as e:
        print(f"Error occured: {e}")
    finally:
        stream.close()

def remove_task(task_file, task_id):
    try:
        stream = open(task_file, "r")
        lines = stream.readlines()
        new_str = ""
        print(f"{len(lines)} number of tasks")
        for line in lines:
            words = line.split("|")
            print(words)
            if len(words) > 0:
                if words[0].strip() != task_id:
                    new_str += line + "\n"
        stream.close()

        streamw = open(task_file,"w")
        streamw.write(new_str)
        streamw.close()
        # print("NEW STR")
        # print(new_str)

    except Exception as e:
        print(f"Error occured: {e}")
    finally:
        stream.close()

def generate_id():
    x = random.random()
    return x



read_tasks("newFile.txt")
task_choosen = get_choice()
if not task_choosen.isdigit() or not int(task_choosen) in range(1,5):
    print("invalid choice\n exiting")
else:
    if int(task_choosen) == 2:
        add_task("newFile.txt")
    elif int(task_choosen) == 3:
        task_id = complete_task_info("newFile.txt")
        remove_task("newFile.txt",task_id)
    read_tasks("newFile.txt")

