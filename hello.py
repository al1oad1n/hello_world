import datetime as dt


def greet():
    print(f"good luck have fun ROMA, current time {dt.datetime.now()}")



# if __name__ == "__main__":
#     greet()
def printer(n):
    for i in range(1,n+1):
        print(f"current number {i}") 

print("enter number:")
a = int(input())

printer(a)