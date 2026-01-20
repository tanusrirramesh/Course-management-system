
courses={}
registeredcourses=[]

def add(courseid,name):
    if courseid in courses:
        print("Course already exists!")
        return
    courses[courseid] = {"name": name,"prereqs":[]}
    print(f"Added course {courseid}: {name}")

def addPrereq(courseid,prereqid):
    if courseid==prereqid:
        print("A course cannot be its own prerequisite.")
        return
    if courseid not in courses or prereqid not in courses:
        print("One or both courses do not exist.")
        return
    if courseid in getAllPrereqs(prereqid,[]):
        print("Cannot add prerequisite: would create a cycle.")
        return
    if prereqid not in courses[courseid]["prereqs"]:
        courses[courseid]["prereqs"].append(prereqid)
        print(f"Added prerequisite {prereqid} to {courseid}")

def remove(courseid):
    if courseid in courses:
        courses.pop(courseid)
        print(f"Removed course {courseid}")
    for c in courses.values():
        if courseid in c["prereqs"]:
            c["prereqs"].remove(courseid)

def getAllPrereqs(courseid,visited):
    if courseid in visited:
        return []
    visited.append(courseid)
    prereqs=[]
    if courseid in courses:
        for j in courses[courseid]["prereqs"]:
            if j not in prereqs:
                prereqs.append(j)
            for p in getAllPrereqs(j, visited):
                if p not in prereqs:
                    prereqs.append(p)
    return prereqs

def listPrerequisites(courseid):
    return getAllPrereqs(courseid,[])

def canEnroll(courseid,compcourses):
    prereq=getAllPrereqs(courseid, [])
    return all(p in compcourses for p in prereqs)


while True:
    print("\n  Course Manager   ")
    print("1.Add Course")
    print("2.Add Prerequisite")
    print("3.Remove Course")
    print("4.List Prerequisites")
    print("5.Can Enroll?")
    print("6.Show All Courses")
    print("7.Register a Course")
    print("8.Show Registered Courses")
    print("0.Exit")

    choice=input("Enter choice: ")

    if choice=="1":
        cid=input("Enter course ID: ")
        name=input("Enter course name: ")
        add(cid,name)

    elif choice=="2":
        cid=input("Enter course ID: ")
        pre=input("Enter prerequisite course ID: ")
        addPrereq(cid,pre)

    elif choice=="3":
        cid=input("Enter course ID to remove: ")
        remove(cid)

    elif choice=="4":
        cid=input("Enter course ID: ")
        print("Prerequisites:",listPrerequisites(cid))

    elif choice=="5":
        cid = input("Enter course ID: ")
        completed = input("Enter completed courses (comma separated): ").split(",")
        completed = [c.strip() for c in completed]
        print("Can enroll?",canEnroll(cid,completed))

    elif choice=="6":
        print("All Courses:")
        for cid in courses:
            print(f"{cid} ({courses[cid]['name']}): {courses[cid]['prereqs']}")

    elif choice=="7":
        cid=input("Enter course ID to register/completed: ")
        if cid not in courses:
            print("Course does not exist.")
        elif cid in registeredcourses:
            print("Course already registered.")
        else:
            registeredcourses.append(cid)
            print(f"Registered course {cid}")

    elif choice=="8":
        print("Registered Courses:",registeredcourses)

    elif choice=="0":
        print("Exiting")
        break

    else:
        print("Invalid choice. Try again.")
