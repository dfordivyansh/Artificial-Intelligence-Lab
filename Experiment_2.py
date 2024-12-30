from collections import deque
def waterjug(x,y,z):
    visited=set()
    queue=deque([(0,0,0,[])])
    while queue:
        a,b,step,path=queue.popleft()
        if a==z:
            print(f"The waterjug is got ({a},{b})")
            print(f"Step :{step}")
            print(f"Path :{path}")
            return True
        if (a,b) in visited:
            continue
        visited.add((a,b))
        possible_moves=[
            (x,b,step+1,path+["Fill Jug 1"]),
            (a,y,step+1,path+["Fill Jug 2"]),
            (0,b,step+1,path+["Empty Jug 1"]),
            (a,0,step+1,path+["Empty Jug 2"]),
            (a-min(a,y-b),b+min(a,y-b),step+1,path+["pour Jug 1 to Jug 2"]),
            (a+min(b,x-a),b-min(b,x-a),step+1,path+["pour Jug 2 to Jug 1"])

        ]
        for actions in possible_moves:
            if (actions[0],actions[1]) not in visited:
                queue.append(actions)
    print("No Possible solution")
    return False
x=4
y=3
z=2
r=waterjug(x,y,z)