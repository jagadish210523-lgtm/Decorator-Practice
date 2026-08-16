def log_execution(cal):
    def wrap():
        print("Start calculating....")
        cal()
        print("Finished calculation....")
    return wrap

@log_execution
def calculation():
    print("Calculating total!!!")


calculation()