
import logging
logging.basicConfig(level=logging.DEBUG)

def calculate(operation_type):
    operation_type=int(operation_type)
    allowed_operations=[1,2,3,4]
    checking=False
    for operation in allowed_operations:
        if operation==operation_type:
            checking=True
    if checking==False:
        logging.warn("Źle określona operacja matematyczna.") 
        exit()
    logging.info(f"podaj operację {operation_type}")
    a =float(input("Podaj składnik 1."))
    b=float(input("Podaj składnik 2."))
    if operation_type==1:
        c=a+b
        logging.info(f"dodaję {a} + {b}")
    elif operation_type==2:
        c=a-b
        logging.info(f"odejmuję {a} - {b}")
    elif operation_type==3:
        c=a*b
        logging.info(f"mnożę {a} * {b}")
    elif operation_type==4:
        c=a/b 
        logging.info(f"dzielę {a} / {b}")
    print(f"wynik to {c}")
    




# if __name__ == "__main__":
#     logging.debug("The program was called with this parameters %s" % sys.argv[1:])
#     logging.debug("First parameter is %s" % sys.argv[1])
    
operation_type =input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
calculate(operation_type)