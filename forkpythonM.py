from multiprocessing import Process
import os
import time
G_boom_num = 1
 
def boom():
    print ("El número de proceso de la bomba es% d"% os.getpid ())
    pass
 # Función principal
def main():
    global G_boom_num
    while True:
                 # Crea una bomba (proceso hijo)
        bo = Process(target = boom)
                 # Detonar bomba ...
        bo.start()
                 # Cuenta las bombas
        G_boom_num += 1
                 print ("Crea la% dth bomba"% G_boom_num)
                 # Después de crear una bomba, hay un retraso de 2 segundos. Si quieres probar el poder de la bomba de proceso, puedes comentar la siguiente línea ...
        time.sleep(2)
 
 # Abre la entrada, inicia el programa principal
if __name__ == "__main__":
    main()
 