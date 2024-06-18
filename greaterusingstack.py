'''FINDING NEXT GREATER NUMBER USING STACK
[1,2,16,4,3,5]
EVERY LAST ELEMENT HAS GREATER -1


top=-1
if top==-1:
    ans=-1
elif top>a[i]
    ans=top
elif top<a[i]
    pop a[i]


ans=2,16,-1,5,5,-1



def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0



def push(stack,item):
    stack.append(item)
    print("pushed item: " + item)


def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"

    return stack.pop()

top=-1
stack = create_stack()
if top==-1:
    ans=-1 
    push(stack,ans)
elif top>a[i]:
    ans=top
    push(stack,ans)
elif top<a[i]:
    pop()
    if top>a[i]:
        ans=top
        push(stack,ans)
    elif top==-1:
        ans=-1
        push(stack,ans)

push(stack, str(1))
push(stack, str(2))
push(stack, str(3))
push(stack, str(4))

print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))



arr=[12,14,2,16,5,3]
def next_greater(arr):
    n=len(arr)
    ans=[0]*n
    stack=[-1]
    for i in range(n-1,-1,-1):
         curr=arr[i]
         while s[-1].top()!=1 and stack.top()<=curr:
             stack.pop()
         ans[i]=stack.top()
         stack.append(curr)

    return ans
print(next_greater(arr))

'''













arr=[1,2,16,4,3,5]
def next_greater(arr):
    n=len(arr)
    ans=[-1]*n
    stack=[]
    for i in range(n-1,-1,-1):
         curr=arr[i]
         while stack and stack[-1]<=curr:
             stack.pop()
         if stack:
             ans[i]=stack[-1]
         stack.append(curr)

    return ans
print(next_greater(arr))

output
[2, 16, -1, 5, 5, -1]

































